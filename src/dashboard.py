
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Distributed NIDS Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# Results from the completed Random Forest training run
st.title("🛡️ Distributed Network Intrusion Detection System")
st.subheader("CIC-IDS2017 | Random Forest Classification")

st.info(
    "Model: Random Forest | Spark 3.5.9 | "
    "Distributed across Naveen and OM"
)

# Model performance
st.header("Model Performance")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Test Accuracy", "99.69%")
col2.metric("Precision", "99.69%")
col3.metric("Recall", "99.69%")
col4.metric("F1 Score", "99.69%")
col5.metric("ROC-AUC", "0.9998")

# Dataset summary
st.header("Dataset Summary")

c1, c2, c3 = st.columns(3)

c1.metric("Total Records", "2,830,743")
c2.metric("Features", "78")
c3.metric("Attack Records", "557,646")

st.subheader("Dataset Distribution")

distribution = pd.DataFrame({
    "Class": ["BENIGN", "ATTACK"],
    "Records": [2273097, 557646]
})

st.bar_chart(
    distribution.set_index("Class")
)

# Confusion matrix
st.header("Confusion Matrix")

confusion = pd.DataFrame(
    [[340092, 1105],
     [230, 83372]],
    index=["Actual BENIGN", "Actual ATTACK"],
    columns=["Predicted BENIGN", "Predicted ATTACK"]
)

st.dataframe(confusion, use_container_width=True)

st.subheader("Confusion Matrix Visualization")

st.bar_chart(confusion)

# Training details
st.header("Training Configuration")

details = {
    "Algorithm": "Random Forest Classifier",
    "Number of trees": 100,
    "Maximum tree depth": 12,
    "Number of features": 78,
    "Training records": "1,981,730",
    "Validation records": "424,214",
    "Testing records": "424,799",
    "Training framework": "Apache Spark MLlib",
    "Dataset": "CIC-IDS2017"
}

st.table(
    pd.DataFrame(
        list(details.items()),
        columns=["Parameter", "Value"]
    )
)

st.caption(
    "Results are from the completed binary classification "
    "experiment. This dashboard displays a saved results snapshot, "
    "not live network traffic."
)
