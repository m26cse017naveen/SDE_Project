
import os
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import (
    MulticlassClassificationEvaluator,
    BinaryClassificationEvaluator
)

# --------------------------------------------------
# 1. Start Spark
# --------------------------------------------------

spark = (
    SparkSession.builder
    .appName("Distributed-NIDS-RandomForest")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

INPUT_PATH = "hdfs:///nids/raw/cicids2017/*.csv"
MODEL_PATH = "hdfs:///nids/models/random_forest_binary_v1"
RESULT_PATH = "hdfs:///nids/results/random_forest_binary_v1"

print("\n========== NIDS TRAINING STARTED ==========\n")
print("Spark application:", spark.sparkContext.applicationId)
print("Spark master:", spark.sparkContext.master)

# --------------------------------------------------
# 2. Read CIC-IDS2017 dataset from HDFS
# --------------------------------------------------

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .option("mode", "PERMISSIVE")
    .csv(INPUT_PATH)
)

# Remove leading/trailing whitespace from column names
df = df.toDF(*[c.strip() for c in df.columns])

print("Dataset columns:", len(df.columns))
print("Original records:", df.count())

# --------------------------------------------------
# 3. Identify label and remove identifier columns
# --------------------------------------------------

label_col = "Label"

if label_col not in df.columns:
    raise ValueError(
        "Label column not found. Available columns: "
        + str(df.columns)
    )

df = df.filter(
    F.col(label_col).isNotNull()
)

# Binary classification:
# BENIGN = 0
# All attacks = 1

df = df.withColumn(
    "label",
    F.when(
        F.upper(F.trim(F.col(label_col))) == "BENIGN",
        0.0
    ).otherwise(1.0)
)

# Remove columns that identify a connection rather
# than describe its traffic behaviour.
excluded = {
    "Flow ID",
    "Source IP",
    "Destination IP",
    "Timestamp",
    "Label",
    "label"
}

feature_cols = [
    c for c in df.columns
    if c not in excluded
]

if not feature_cols:
    raise ValueError("No usable feature columns found")

# Convert all selected features to numeric values.
# Replace missing, invalid and infinite values with 0.

for c in feature_cols:
    safe_col = F.col("`" + c.replace("`", "``") + "`")

    numeric_col = safe_col.cast("double")

    df = df.withColumn(
        c,
        F.when(
            numeric_col.isNull()
            | F.isnan(numeric_col)
            | (F.abs(numeric_col) == float("inf")),
            F.lit(0.0)
        ).otherwise(numeric_col)
    )

df = df.select(
    *[F.col("`" + c.replace("`", "``") + "`") for c in feature_cols],
    F.col("label")
)

df = df.persist()

print("\n========== DATASET SUMMARY ==========")
print("Total cleaned records:", df.count())
print("Number of features:", len(feature_cols))

print("\nClass distribution:")
df.groupBy("label").count().orderBy("label").show()

# --------------------------------------------------
# 4. Split data into train, validation and test
# --------------------------------------------------

train_df, val_df, test_df = df.randomSplit(
    [0.70, 0.15, 0.15],
    seed=42
)

train_df = train_df.persist()
val_df = val_df.persist()
test_df = test_df.persist()

train_count = train_df.count()

print("\nTraining records:", train_count)
print("Validation records:", val_df.count())
print("Testing records:", test_df.count())

# --------------------------------------------------
# 5. Handle class imbalance using training weights
# --------------------------------------------------

class_counts = {
    row["label"]: row["count"]
    for row in train_df.groupBy("label").count().collect()
}

benign_count = class_counts.get(0.0, 0)
attack_count = class_counts.get(1.0, 0)

if benign_count == 0 or attack_count == 0:
    raise ValueError(
        "Training split must contain both BENIGN and attack records"
    )

total = benign_count + attack_count

benign_weight = total / (2.0 * benign_count)
attack_weight = total / (2.0 * attack_count)

train_df = train_df.withColumn(
    "classWeight",
    F.when(
        F.col("label") == 0.0,
        F.lit(benign_weight)
    ).otherwise(F.lit(attack_weight))
)

print("\nClass weights:")
print("BENIGN:", benign_weight)
print("ATTACK:", attack_weight)

# --------------------------------------------------
# 6. Feature assembly and Random Forest
# --------------------------------------------------

assembler = VectorAssembler(
    inputCols=feature_cols,
    outputCol="features",
    handleInvalid="error"
)

rf = RandomForestClassifier(
    labelCol="label",
    featuresCol="features",
    weightCol="classWeight",
    numTrees=100,
    maxDepth=12,
    maxBins=64,
    seed=42,
    featureSubsetStrategy="sqrt"
)

pipeline = Pipeline(
    stages=[assembler, rf]
)

print("\n========== TRAINING RANDOM FOREST ==========")

model = pipeline.fit(train_df)

print("\nModel training completed!")

# --------------------------------------------------
# 7. Evaluate validation and test data
# --------------------------------------------------

predictions = model.transform(test_df)

accuracy_eval = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="accuracy"
)

precision_eval = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="weightedPrecision"
)

recall_eval = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="weightedRecall"
)

f1_eval = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="f1"
)

auc_eval = BinaryClassificationEvaluator(
    labelCol="label",
    rawPredictionCol="rawPrediction",
    metricName="areaUnderROC"
)

# Validation evaluation
val_predictions = model.transform(val_df)

validation_accuracy = accuracy_eval.evaluate(val_predictions)

# Test evaluation
accuracy = accuracy_eval.evaluate(predictions)
precision = precision_eval.evaluate(predictions)
recall = recall_eval.evaluate(predictions)
f1 = f1_eval.evaluate(predictions)
auc = auc_eval.evaluate(predictions)

print("\n========== TEST RESULTS ==========")
print(f"Validation Accuracy: {validation_accuracy:.4f}")
print(f"Test Accuracy:       {accuracy:.4f}")
print(f"Weighted Precision:  {precision:.4f}")
print(f"Weighted Recall:     {recall:.4f}")
print(f"Weighted F1 Score:   {f1:.4f}")
print(f"ROC-AUC:             {auc:.4f}")

# --------------------------------------------------
# 8. Confusion matrix
# --------------------------------------------------

print("\n========== CONFUSION MATRIX ==========")

confusion = (
    predictions
    .groupBy("label", "prediction")
    .count()
    .orderBy("label", "prediction")
)

confusion.show()

# --------------------------------------------------
# 9. Save trained model and results to HDFS
# --------------------------------------------------

model.write().overwrite().save(MODEL_PATH)

metrics = [
    ("validation_accuracy", float(validation_accuracy)),
    ("test_accuracy", float(accuracy)),
    ("weighted_precision", float(precision)),
    ("weighted_recall", float(recall)),
    ("weighted_f1", float(f1)),
    ("roc_auc", float(auc)),
    ("training_records", int(train_count)),
    ("validation_records", int(val_df.count())),
    ("test_records", int(test_df.count())),
    ("feature_count", int(len(feature_cols))),
    ("random_forest_trees", 100),
    ("random_forest_max_depth", 12)
]

metrics_df = spark.createDataFrame(
    metrics,
    ["metric", "value"]
)

metrics_df.write.mode("overwrite").csv(
    RESULT_PATH + "/metrics",
    header=True
)

confusion.write.mode("overwrite").csv(
    RESULT_PATH + "/confusion_matrix",
    header=True
)

print("\nModel saved to:", MODEL_PATH)
print("Results saved to:", RESULT_PATH)

# --------------------------------------------------
# 10. Cleanup
# --------------------------------------------------

train_df.unpersist()
val_df.unpersist()
test_df.unpersist()
df.unpersist()

spark.stop()

print("\n========== NIDS TRAINING FINISHED ==========\n")
