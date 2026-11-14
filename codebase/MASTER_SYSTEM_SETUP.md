# Master System Setup and Execution Log

This document combines the two supplied master-system terminal-log files into one Markdown file for the project GitHub repository.

## Scope

- **Master machine:** Naveen's Arch Linux system (`archlinux`)
- **Master IP recorded in the logs:** `10.87.234.198`
- **Worker machine referenced in the logs:** `DHANDEPATIL` / user `om`
- **Worker IP used in the later cluster configuration and YARN logs:** `10.87.234.88`
- **Hadoop version shown:** `2.9.1`
- **Java version shown in the initial environment checks:** Java 8 (`1.8.0_45`)

> **Important:** These are historical terminal logs, not a clean installation script. They include failed commands, troubleshooting attempts, changing network addresses, and diagnostic output. Read commands before re-running them. Network addresses may change between sessions.

> **GitHub privacy check:** Before making the repository public, review the logs for internal IP addresses, machine identifiers, SSH fingerprints, usernames, hostnames, filesystem paths, and any credentials or tokens. Passwords entered at prompts are not present in terminal output, but the logs still reveal system details.

---

## Part 1 — Master system setup, networking, SSH, and Hadoop diagnostics

The following is the first supplied file, retained in its original order.

```text
[naveen@archlinux ~]$ hostname
archlinux
[naveen@archlinux ~]$ whoami
naveen
[naveen@archlinux ~]$ ip -4 addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: wlp2s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    altname wlx141333054c1b
    inet 10.87.234.198/24 brd 10.87.234.255 scope global dynamic noprefixroute wlp2s0
       valid_lft 3316sec preferred_lft 3316sec
[naveen@archlinux ~]$ ip route get 1.1.1.1
1.1.1.1 via 10.87.234.16 dev wlp2s0 src 10.87.234.198 uid 1000 
    cache 
[naveen@archlinux ~]$ sudo hostnamectl set -hostname naveen
[sudo] password for naveen: 
> hostnamectl [OPTION…] COMMAND …

Query or change system hostname.

Commands:
  [status]               Show current hostname settings
  hostname [NAME]        Get/set system hostname
  icon-name [NAME]       Get/set icon name for host
  chassis [NAME]         Get/set chassis type for host
  deployment [NAME]      Get/set deployment environment for host
  location [NAME]        Get/set location for host
  tags [TAG…]            Get/set machine tags for host

Options:
  -h --help              Show this help
     --version           Show package version
     --no-ask-password   Do not prompt for password
  -H --host=[USER@]HOST  Operate on remote host
  -M --machine=CONTAINER Operate on local container
     --transient         Only set transient hostname
     --static            Only set static hostname
     --pretty            Only set pretty hostname
     --json=FORMAT       Generate JSON output (pretty, short, or off)
  -j                     Equivalent to --json=pretty (on TTY) or --json=short (otherwise)

See the hostnamectl(1) man page for details.
[naveen@archlinux ~]$ hostname
archlinux
[naveen@archlinux ~]$ hostname
archlinux
[naveen@archlinux ~]$ ^[[200~sudo pacman -S --needed openssh~
bash: $'\E[200~sudo': command not found
[naveen@archlinux ~]$ sudo pacman -S --needed openssh
[sudo] password for naveen: 
warning: openssh-10.6p1-3 is up to date -- skipping
 there is nothing to do
[naveen@archlinux ~]$ sudo systemctl enable --now sshd
[naveen@archlinux ~]$ sudo systemctl status sshd
● sshd.service - OpenSSH Daemon
     Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled; preset: disabled)
     Active: active (running) since Sat 2026-11-14 20:52:36 IST; 5h 10min left
 Invocation: 361cdf5aad5149e49cc765b8f263aba3
       Docs: man:sshd(8)
             man:sshd_config(5)
   Main PID: 731 (sshd)
      Tasks: 1 (limit: 18285)
     Memory: 1.8M (peak: 2.4M)
        CPU: 9ms
     CGroup: /system.slice/sshd.service
             └─731 "sshd: /usr/bin/sshd -D [listener] 0 of 10-100 startups"

Nov 14 20:52:35 archlinux systemd[1]: Starting OpenSSH Daemon...
Nov 14 20:52:36 archlinux sshd[731]: Server listening on 0.0.0.0 port 22.
Nov 14 20:52:36 archlinux sshd[731]: Server listening on :: port 22.
Nov 14 20:52:36 archlinux systemd[1]: Started OpenSSH Daemon.
[naveen@archlinux ~]$ sudo sshd -t
[naveen@archlinux ~]$ hostname
archlinux
[naveen@archlinux ~]$ whoami 
naveen
[naveen@archlinux ~]$ ip -4 -br addr
lo               UNKNOWN        127.0.0.1/8 
wlp2s0           UP             10.87.234.198/24 
[naveen@archlinux ~]$ ip route get 1.1.1.1
1.1.1.1 via 10.87.234.16 dev wlp2s0 src 10.87.234.198 uid 1000 
    cache 
[naveen@archlinux ~]$ sudo nano /etc/hosts
[naveen@archlinux ~]$ sudo nano /etc/hosts
[naveen@archlinux ~]$ sudo nano /etc/hosts
[naveen@archlinux ~]$ ping -c 4 om
PING om (172.31.64.1) 56(84) bytes of data.
64 bytes from om (172.31.64.1): icmp_seq=1 ttl=253 time=46.2 ms
64 bytes from om (172.31.64.1): icmp_seq=2 ttl=253 time=29.6 ms
64 bytes from om (172.31.64.1): icmp_seq=3 ttl=253 time=34.3 ms
64 bytes from om (172.31.64.1): icmp_seq=4 ttl=253 time=13.8 ms

--- om ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3006ms
rtt min/avg/max/mdev = 13.767/30.976/46.245/11.641 ms
[naveen@archlinux ~]$ hostname -I
hostname: invalid option -- 'I'
Try 'hostname --help' or 'hostname --usage' for more information.
[naveen@archlinux ~]$ whoami
naveen
[naveen@archlinux ~]$ hostname
archlinux
[naveen@archlinux ~]$ hostname -I
hostname: invalid option -- 'I'
Try 'hostname --help' or 'hostname --usage' for more information.
[naveen@archlinux ~]$ hostname -l
hostname: invalid option -- 'l'
Try 'hostname --help' or 'hostname --usage' for more information.
[naveen@archlinux ~]$ whoami
hostname
hostname -I
ip route get 8.8.8.8
java -version
hadoop version
echo $HADOOP_HOME
echo $JAVA_HOME
naveen
archlinux
hostname: invalid option -- 'I'
Try 'hostname --help' or 'hostname --usage' for more information.
8.8.8.8 via 10.87.234.16 dev wlp2s0 src 10.87.234.198 uid 1000 
    cache 
java version "1.8.0_45"
Java(TM) SE Runtime Environment (build 1.8.0_45-b14)
Java HotSpot(TM) 64-Bit Server VM (build 25.45-b02, mixed mode)
Hadoop 2.9.1
Subversion https://github.com/apache/hadoop.git -r e30710aea4e6e55e69372929106cf119af06fd0e
Compiled by root on 2018-04-16T09:33Z
Compiled with protoc 2.5.0
From source with checksum 7d6d2b655115c6cc336d662cc2b919bd
This command was run using /home/naveen/hadoop-2.9.1/share/hadoop/common/hadoop-common-2.9.1.jar
/home/naveen/hadoop-2.9.1
/home/naveen/jdk-8u45-linux-x64/jdk1.8.0_45
[naveen@archlinux ~]$ ip -4 addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: wlp2s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    altname wlx141333054c1b
    inet 10.87.234.198/24 brd 10.87.234.255 scope global dynamic noprefixroute wlp2s0
       valid_lft 3444sec preferred_lft 3444sec
[naveen@archlinux ~]$ ping -c 4 10.87.234.198
PING 10.87.234.198 (10.87.234.198) 56(84) bytes of data.
64 bytes from 10.87.234.198: icmp_seq=1 ttl=64 time=0.032 ms
64 bytes from 10.87.234.198: icmp_seq=2 ttl=64 time=0.081 ms
64 bytes from 10.87.234.198: icmp_seq=3 ttl=64 time=0.058 ms
64 bytes from 10.87.234.198: icmp_seq=4 ttl=64 time=0.041 ms

--- 10.87.234.198 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3057ms
rtt min/avg/max/mdev = 0.032/0.053/0.081/0.018 ms
[naveen@archlinux ~]$ ip -4 addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: wlp2s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    altname wlx141333054c1b
    inet 10.87.234.198/24 brd 10.87.234.255 scope global dynamic noprefixroute wlp2s0
       valid_lft 3259sec preferred_lft 3259sec
[naveen@archlinux ~]$ sudo systemctl enable --now sshd
[sudo] password for naveen: 
Sorry, try again.
[sudo] password for naveen: 
[naveen@archlinux ~]$ sudo systemctl status sshd
● sshd.service - OpenSSH Daemon
     Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled; preset: disabled)
     Active: active (running) since Sat 2026-11-14 20:52:36 IST; 2h 54min left
 Invocation: 361cdf5aad5149e49cc765b8f263aba3
       Docs: man:sshd(8)
             man:sshd_config(5)
   Main PID: 731 (sshd)
      Tasks: 1 (limit: 18285)
     Memory: 1.8M (peak: 2.4M)
        CPU: 10ms
     CGroup: /system.slice/sshd.service
             └─731 "sshd: /usr/bin/sshd -D [listener] 0 of 10-100 startups"

Nov 14 20:52:35 archlinux systemd[1]: Starting OpenSSH Daemon...
Nov 14 20:52:36 archlinux sshd[731]: Server listening on 0.0.0.0 port 22.
Nov 14 20:52:36 archlinux sshd[731]: Server listening on :: port 22.
Nov 14 20:52:36 archlinux systemd[1]: Started OpenSSH Daemon.
[naveen@archlinux ~]$ ping -c 4 10.132.11.245
PING 10.132.11.245 (10.132.11.245) 56(84) bytes of data.

--- 10.132.11.245 ping statistics ---
4 packets transmitted, 0 received, 100% packet loss, time 3078ms

[naveen@archlinux ~]$ ip -4 -br addr
lo               UNKNOWN        127.0.0.1/8 
wlp2s0           UP             10.87.234.198/24 
[naveen@archlinux ~]$ ip -4 addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: wlp2s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    altname wlx141333054c1b
    inet 10.87.234.198/24 brd 10.87.234.255 scope global dynamic noprefixroute wlp2s0
       valid_lft 3506sec preferred_lft 3506sec
[naveen@archlinux ~]$ ip route
default via 10.87.234.16 dev wlp2s0 proto dhcp src 10.87.234.198 metric 600 
10.87.234.0/24 dev wlp2s0 proto kernel scope link src 10.87.234.198 metric 600 
[naveen@archlinux ~]$ ping -c 4 192.168.43.100
PING 192.168.43.100 (192.168.43.100) 56(84) bytes of data.

--- 192.168.43.100 ping statistics ---
4 packets transmitted, 0 received, 100% packet loss, time 3082ms

[naveen@archlinux ~]$ mkdir -p ~/cluster-reset-backup

sudo cp -a /etc/hosts ~/cluster-reset-backup/hosts.backup
sudo cp -a /etc/hostname ~/cluster-reset-backup/hostname.backup 2>/dev/null || true

cp -a ~/.ssh ~/cluster-reset-backup/ssh.backup 2>/dev/null || true

hostnamectl status
[sudo] password for naveen: 
  Static hostname: archlinux
        Icon name: computer-laptop
          Chassis: laptop 💻
Chassis Asset Tag:  No  Asset  Tag
       Machine ID: bfabb92a9aac4c38b5599735815dc7a1
          Boot ID: f7482e852d8e4bcfa95c0c576e1cbe1e
 Operating System: Arch Linux    
           Kernel: Linux 7.2.15-arch1-1
     Architecture: x86-64
  Hardware Vendor: ASUSTeK COMPUTER INC.
   Hardware Model: ROG Strix G713IC_G713IC
 Hardware Version: 1.0
 Firmware Version: G713IC.312
    Firmware Date: Fri 2021-11-26
     Firmware Age: 4y 11month 2w 4d                
[naveen@archlinux ~]$ sudo nano /etc/hosts
[naveen@archlinux ~]$ hostnamectl status
  Static hostname: archlinux
        Icon name: computer-laptop
          Chassis: laptop 💻
Chassis Asset Tag:  No  Asset  Tag
       Machine ID: bfabb92a9aac4c38b5599735815dc7a1
          Boot ID: f7482e852d8e4bcfa95c0c576e1cbe1e
 Operating System: Arch Linux    
           Kernel: Linux 7.2.15-arch1-1
     Architecture: x86-64
  Hardware Vendor: ASUSTeK COMPUTER INC.
   Hardware Model: ROG Strix G713IC_G713IC
 Hardware Version: 1.0
 Firmware Version: G713IC.312
    Firmware Date: Fri 2021-11-26
     Firmware Age: 4y 11month 2w 4d                
[naveen@archlinux ~]$ sudo nano /etc/hosts
[naveen@archlinux ~]$ ls -la ~/.ssh
cat ~/.ssh/config 2>/dev/null
total 40
drwx------  2 naveen naveen 4096 Nov 11 23:53 .
drwx------ 21 naveen naveen 4096 Nov 14 18:09 ..
-rw-------  1 naveen naveen 1140 Nov 11 22:26 authorized_keys
-rw-------  1 naveen naveen  411 Nov 11 23:52 id_ed25519
-rw-r--r--  1 naveen naveen   98 Nov 11 23:52 id_ed25519.pub
-rw-------  1 naveen naveen 2602 Nov 11 22:25 id_rsa
-rw-r--r--  1 naveen naveen  570 Nov 11 22:25 id_rsa.pub
-rw-------  1 naveen naveen 5562 Nov 11 23:53 known_hosts
-rw-------  1 naveen naveen 2867 Nov 11 23:40 known_hosts.old
[naveen@archlinux ~]$ ls -l ~/.ssh/config
ls: cannot access '/home/naveen/.ssh/config': No such file or directory
[naveen@archlinux ~]$ ssh-keygen -lf ~/.ssh/authorized_keys
3072 SHA256:+Ae4mjs8LQ02sGtemtyKQJZt+wnjq6zVDhJPxrHkM4A naveen@archlinux (RSA)
3072 SHA256:xyWtCVWAk+KVNoVOhwf1bZByvWfJ+FrgQis4feVA4gA naveen@archlinux (RSA)
[naveen@archlinux ~]$ ssh-keygen -lf ~/.ssh/id_ed25519.pub
256 SHA256:ZyHqyGtgvtXOwM3H8nH7dE3lTJQntBRd6Q6aSK5phH4 naveen@archlinux (ED25519)
[naveen@archlinux ~]$ V
bash: V: command not found
[naveen@archlinux ~]$ ssh-keygen -lf ~/.ssh/id_rsa.pub
3072 SHA256:xyWtCVWAk+KVNoVOhwf1bZByvWfJ+FrgQis4feVA4gA naveen@archlinux (RSA)
[naveen@archlinux ~]$ cat /etc/hosts
# Static table lookup for hostnames.
# See hosts(5) for details.
127.0.0.1        localhost
::1              localhost
172.31.118.145 archlinux
172.31.76.25 DHANDEPATIL
172.31.111.173 DHANDEPATIL
[naveen@archlinux ~]$ sudo systemctl status sshd
● sshd.service - OpenSSH Daemon
     Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled; preset: disabled)
     Active: active (running) since Sat 2026-11-14 20:52:36 IST; 2h 38min left
 Invocation: 361cdf5aad5149e49cc765b8f263aba3
       Docs: man:sshd(8)
             man:sshd_config(5)
   Main PID: 731 (sshd)
      Tasks: 1 (limit: 18285)
     Memory: 1.8M (peak: 2.4M)
        CPU: 10ms
     CGroup: /system.slice/sshd.service
             └─731 "sshd: /usr/bin/sshd -D [listener] 0 of 10-100 startups"

Nov 14 20:52:35 archlinux systemd[1]: Starting OpenSSH Daemon...
Nov 14 20:52:36 archlinux sshd[731]: Server listening on 0.0.0.0 port 22.
Nov 14 20:52:36 archlinux sshd[731]: Server listening on :: port 22.
Nov 14 20:52:36 archlinux systemd[1]: Started OpenSSH Daemon.
[naveen@archlinux ~]$ sudo nano /etc/hosts
[sudo] password for naveen: 
[naveen@archlinux ~]$ cat /etc/hosts
hostname
# Static table lookup for hostnames.
# See hosts(5) for details.
127.0.0.1        localhost
::1              localhost
172.31.118.145 archlinux
172.31.76.25 DHANDEPATIL
172.31.111.173 DHANDEPATIL
archlinux
[naveen@archlinux ~]$ hostname
whoami
ip -4 -br addr
ip route get 1.1.1.1
archlinux
naveen
lo               UNKNOWN        127.0.0.1/8 
wlp2s0           UP             10.87.234.198/24 
1.1.1.1 via 10.87.234.16 dev wlp2s0 src 10.87.234.198 uid 1000 
    cache 
[naveen@archlinux ~]$ sudo pacman -S --needed openssh
warning: openssh-10.6p1-3 is up to date -- skipping
 there is nothing to do
[naveen@archlinux ~]$ sudo systemctl enable --now sshd
[naveen@archlinux ~]$ sudo systemctl is-active sshd^C
[naveen@archlinux ~]$ ^[[200~sudo systemctl is-active sshd~
bash: $'\E[200~sudo': command not found
[naveen@archlinux ~]$ sudo systemctl is-active sshd
active
[naveen@archlinux ~]$ ping -c 4 172.31.87.3
PING 172.31.87.3 (172.31.87.3) 56(84) bytes of data.

--- 172.31.87.3 ping statistics ---
4 packets transmitted, 0 received, 100% packet loss, time 3086ms

[naveen@archlinux ~]$ ip -4 -br addr
lo               UNKNOWN        127.0.0.1/8 
wlp2s0           UP             10.87.234.198/24 
[naveen@archlinux ~]$ ip route
default via 10.87.234.16 dev wlp2s0 proto dhcp src 10.87.234.198 metric 600 
10.87.234.0/24 dev wlp2s0 proto kernel scope link src 10.87.234.198 metric 600 
[naveen@archlinux ~]$ V
bash: V: command not found
[naveen@archlinux ~]$ ip route get 10.87.234.198
local 10.87.234.198 dev lo src 10.87.234.198 uid 1000 
    cache <local> 
[naveen@archlinux ~]$ nmcli connection show --active
NAME                    UUID                                  TYPE      DEVICE 
Dyson Sphere Tutorial   85adaa5d-6df8-4bf8-9a35-710e15e0ab32  wifi      wlp2s0 
lo                      1aafe971-7c47-457d-9f76-afb50b893f09  loopback  lo     
[naveen@archlinux ~]$ ip route
default via 10.87.234.16 dev wlp2s0 proto dhcp src 10.87.234.198 metric 600 
10.87.234.0/24 dev wlp2s0 proto kernel scope link src 10.87.234.198 metric 600 
[naveen@archlinux ~]$ ping -c 4 10.87.234.87
PING 10.87.234.87 (10.87.234.87) 56(84) bytes of data.
64 bytes from 10.87.234.87: icmp_seq=1 ttl=64 time=99.8 ms
64 bytes from 10.87.234.87: icmp_seq=2 ttl=64 time=67.1 ms
64 bytes from 10.87.234.87: icmp_seq=3 ttl=64 time=27.6 ms
64 bytes from 10.87.234.87: icmp_seq=4 ttl=64 time=29.1 ms

--- 10.87.234.87 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3007ms
rtt min/avg/max/mdev = 27.632/55.895/99.819/29.885 ms
[naveen@archlinux ~]$ sudo systemctl is-active sshd
[sudo] password for naveen: 
active
[naveen@archlinux ~]$ ssh om@10.87.234.87

ssh: connect to host 10.87.234.87 port 22: Connection timed out
[naveen@archlinux ~]$ 
[naveen@archlinux ~]$ ssh om@10.87.234.87
^C
[naveen@archlinux ~]$ sudo pacman -S --needed openbsd-netcat
[sudo] password for naveen: 
resolving dependencies...
looking for conflicting packages...

Packages (1) openbsd-netcat-1.239_1-1

Total Download Size:   0.02 MiB
Total Installed Size:  0.05 MiB

:: Proceed with installation? [Y/n] y
:: Retrieving packages...
 openbsd-netcat-1.239_1-1-x86_64                                                                     25.5 KiB  14.9 KiB/s 00:02 [#############################################################################] 100%
(1/1) checking keys in keyring                                                                                                  [#############################################################################] 100%
(1/1) checking package integrity                                                                                                [#############################################################################] 100%
(1/1) loading package files                                                                                                     [#############################################################################] 100%
(1/1) checking for file conflicts                                                                                               [#############################################################################] 100%
(1/1) checking available disk space                                                                                             [#############################################################################] 100%
:: Processing package changes...
(1/1) installing openbsd-netcat                                                                                                 [#############################################################################] 100%
:: Running post-transaction hooks...
(1/1) Arming ConditionNeedsUpdate...
[naveen@archlinux ~]$ nc -vz -w 5 10.87.234.87 22
nc: connect to 10.87.234.87 port 22 (tcp) timed out: Operation now in progress
[naveen@archlinux ~]$ nc -vz -w 5 10.87.234.87 22
Connection to 10.87.234.87 22 port [tcp/ssh] succeeded!
[naveen@archlinux ~]$ ssh om@10.87.234.87
The authenticity of host '10.87.234.87 (10.87.234.87)' can't be established.
ED25519 key fingerprint is: SHA256:lTEs5ZQ3qB2WdVYwENCsWfqiJ475S/FNTGvsjbH/u1A
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:6: 172.31.76.25
    ~/.ssh/known_hosts:10: dhandepatil
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.87.234.87' (ED25519) to the list of known hosts.
om@10.87.234.87's password: 
(base) [om@DHANDEPATIL ~]$ hostname
DHANDEPATIL
(base) [om@DHANDEPATIL ~]$ whoami
om
(base) [om@DHANDEPATIL ~]$ exit 
logout
Connection to 10.87.234.87 closed.
[naveen@archlinux ~]$ hostname
whoami
hostnamectl status
archlinux
naveen
  Static hostname: archlinux
        Icon name: computer-laptop
          Chassis: laptop 💻
Chassis Asset Tag:  No  Asset  Tag
       Machine ID: bfabb92a9aac4c38b5599735815dc7a1
          Boot ID: f7482e852d8e4bcfa95c0c576e1cbe1e
 Operating System: Arch Linux    
           Kernel: Linux 7.2.15-arch1-1
     Architecture: x86-64
  Hardware Vendor: ASUSTeK COMPUTER INC.
   Hardware Model: ROG Strix G713IC_G713IC
 Hardware Version: 1.0
 Firmware Version: G713IC.312
    Firmware Date: Fri 2021-11-26
     Firmware Age: 4y 11month 2w 4d                
[naveen@archlinux ~]$ V
bash: V: command not found
[naveen@archlinux ~]$ ip -4 -br addr
lo               UNKNOWN        127.0.0.1/8 
wlp2s0           UP             10.87.234.198/24 
[naveen@archlinux ~]$ ip route
default via 10.87.234.16 dev wlp2s0 proto dhcp src 10.87.234.198 metric 600 
10.87.234.0/24 dev wlp2s0 proto kernel scope link src 10.87.234.198 metric 600 
[naveen@archlinux ~]$ ip route get 1.1.1.1
1.1.1.1 via 10.87.234.16 dev wlp2s0 src 10.87.234.198 uid 1000 
    cache 
[naveen@archlinux ~]$ sudo systemctl status sshd
[sudo] password for naveen: 
● sshd.service - OpenSSH Daemon
     Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled; preset: disabled)
     Active: active (running) since Sat 2026-11-14 20:52:36 IST; 2h 3min left
 Invocation: 361cdf5aad5149e49cc765b8f263aba3
       Docs: man:sshd(8)
             man:sshd_config(5)
   Main PID: 731 (sshd)
      Tasks: 1 (limit: 18285)
     Memory: 1.8M (peak: 2.4M)
        CPU: 10ms
     CGroup: /system.slice/sshd.service
             └─731 "sshd: /usr/bin/sshd -D [listener] 0 of 10-100 startups"

Nov 14 20:52:35 archlinux systemd[1]: Starting OpenSSH Daemon...
Nov 14 20:52:36 archlinux sshd[731]: Server listening on 0.0.0.0 port 22.
Nov 14 20:52:36 archlinux sshd[731]: Server listening on :: port 22.
Nov 14 20:52:36 archlinux systemd[1]: Started OpenSSH Daemon.
[naveen@archlinux ~]$ sudo ss -ltnp | grep ':22'
LISTEN 0      128          0.0.0.0:22        0.0.0.0:*    users:(("sshd",pid=731,fd=6))
LISTEN 0      128             [::]:22           [::]:*    users:(("sshd",pid=731,fd=7))
[naveen@archlinux ~]$ java -version
java version "1.8.0_45"
Java(TM) SE Runtime Environment (build 1.8.0_45-b14)
Java HotSpot(TM) 64-Bit Server VM (build 25.45-b02, mixed mode)
[naveen@archlinux ~]$ readlink -f "$(which java)"
/home/naveen/jdk-8u45-linux-x64/jdk1.8.0_45/bin/java
[naveen@archlinux ~]$ V
bash: V: command not found
[naveen@archlinux ~]$ V
bash: V: command not found
[naveen@archlinux ~]$ echo $JAVA_HOME
/home/naveen/jdk-8u45-linux-x64/jdk1.8.0_45
[naveen@archlinux ~]$ ls -ld /home/naveen/hadoop-2.9.1
drwxr-xr-x 10 naveen naveen 4096 Nov 11 22:35 /home/naveen/hadoop-2.9.1
[naveen@archlinux ~]$ /home/naveen/hadoop-2.9.1/bin/hadoop version
Hadoop 2.9.1
Subversion https://github.com/apache/hadoop.git -r e30710aea4e6e55e69372929106cf119af06fd0e
Compiled by root on 2018-04-16T09:33Z
Compiled with protoc 2.5.0
From source with checksum 7d6d2b655115c6cc336d662cc2b919bd
This command was run using /home/naveen/hadoop-2.9.1/share/hadoop/common/hadoop-common-2.9.1.jar
[naveen@archlinux ~]$ echo $HADOOP_HOME
/home/naveen/hadoop-2.9.1
[naveen@archlinux ~]$ df -h
Filesystem      Size  Used Avail Use% Mounted on
dev             7.5G     0  7.5G   0% /dev
run             7.6G  1.6M  7.6G   1% /run
efivarfs        128K   43K   81K  35% /sys/firmware/efi/efivars
/dev/nvme0n1p8   59G   17G   40G  30% /
tmpfs           7.6G     0  7.6G   0% /dev/shm
none            1.0M     0  1.0M   0% /run/credentials/systemd-journald.service
tmpfs           7.6G   82M  7.5G   2% /tmp
/dev/nvme0n1p1  256M  220M   37M  86% /boot
tmpfs           1.6G  108K  1.6G   1% /run/user/1000
[naveen@archlinux ~]$ sudo nft list ruleset
# Warning: table ip filter is managed by iptables-nft, do not touch!
table ip filter {
	chain ufw-before-logging-input {
	}

	chain ufw-before-logging-output {
	}

	chain ufw-before-logging-forward {
	}

	chain ufw-before-input {
		iifname "lo" counter packets 11755 bytes 919669 accept
		xt match "conntrack" counter packets 159755 bytes 183843494 accept
		xt match "conntrack" counter packets 3 bytes 168 jump ufw-logging-deny
		xt match "conntrack" counter packets 3 bytes 168 drop
		ip protocol icmp xt match "icmp" counter packets 0 bytes 0 accept
		ip protocol icmp xt match "icmp" counter packets 0 bytes 0 accept
		ip protocol icmp xt match "icmp" counter packets 0 bytes 0 accept
		ip protocol icmp xt match "icmp" counter packets 1 bytes 84 accept
		udp sport 67 udp dport 68 counter packets 1 bytes 348 accept
		counter packets 303 bytes 83073 jump ufw-not-local
		ip daddr 224.0.0.251 udp dport 5353 counter packets 62 bytes 5288 accept
		ip daddr 239.255.255.250 udp dport 1900 counter packets 190 bytes 38000 accept
		counter packets 51 bytes 39785 jump ufw-user-input
	}

	chain ufw-before-output {
		oifname "lo" counter packets 11755 bytes 919669 accept
		xt match "conntrack" counter packets 49585 bytes 14303078 accept
		counter packets 3145 bytes 1125218 jump ufw-user-output
	}

	chain ufw-before-forward {
		xt match "conntrack" counter packets 0 bytes 0 accept
		ip protocol icmp xt match "icmp" counter packets 0 bytes 0 accept
		ip protocol icmp xt match "icmp" counter packets 0 bytes 0 accept
		ip protocol icmp xt match "icmp" counter packets 0 bytes 0 accept
		ip protocol icmp xt match "icmp" counter packets 0 bytes 0 accept
		counter packets 0 bytes 0 jump ufw-user-forward
	}

	chain ufw-after-input {
		udp dport 137 counter packets 0 bytes 0 jump ufw-skip-to-policy-input
		udp dport 138 counter packets 0 bytes 0 jump ufw-skip-to-policy-input
		tcp dport 139 counter packets 0 bytes 0 jump ufw-skip-to-policy-input
		tcp dport 445 counter packets 0 bytes 0 jump ufw-skip-to-policy-input
		udp dport 67 counter packets 6 bytes 1943 jump ufw-skip-to-policy-input
		udp dport 68 counter packets 0 bytes 0 jump ufw-skip-to-policy-input
		xt match "addrtype" counter packets 0 bytes 0 jump ufw-skip-to-policy-input
	}

	chain ufw-after-output {
	}

	chain ufw-after-forward {
	}

	chain ufw-after-logging-input {
		limit rate 3/minute burst 10 packets counter packets 38 bytes 32032 xt target "LOG"
	}

	chain ufw-after-logging-output {
	}

	chain ufw-after-logging-forward {
		limit rate 3/minute burst 10 packets counter packets 0 bytes 0 xt target "LOG"
	}

	chain ufw-reject-input {
	}

	chain ufw-reject-output {
	}

	chain ufw-reject-forward {
	}

	chain ufw-track-input {
	}

	chain ufw-track-output {
		ip protocol tcp xt match "conntrack" counter packets 574 bytes 34960 accept
		ip protocol udp xt match "conntrack" counter packets 2529 bytes 1087842 accept
	}

	chain ufw-track-forward {
	}

	chain INPUT {
		type filter hook input priority filter; policy drop;
		counter packets 171818 bytes 184846836 jump ufw-before-logging-input
		counter packets 171818 bytes 184846836 jump ufw-before-input
		counter packets 51 bytes 39785 jump ufw-after-input
		counter packets 45 bytes 37842 jump ufw-after-logging-input
		counter packets 45 bytes 37842 jump ufw-reject-input
		counter packets 45 bytes 37842 jump ufw-track-input
	}

	chain OUTPUT {
		type filter hook output priority filter; policy accept;
		counter packets 64485 bytes 16347965 jump ufw-before-logging-output
		counter packets 64485 bytes 16347965 jump ufw-before-output
		counter packets 3145 bytes 1125218 jump ufw-after-output
		counter packets 3145 bytes 1125218 jump ufw-after-logging-output
		counter packets 3145 bytes 1125218 jump ufw-reject-output
		counter packets 3145 bytes 1125218 jump ufw-track-output
	}

	chain FORWARD {
		type filter hook forward priority filter; policy drop;
		counter packets 0 bytes 0 jump ufw-before-logging-forward
		counter packets 0 bytes 0 jump ufw-before-forward
		counter packets 0 bytes 0 jump ufw-after-forward
		counter packets 0 bytes 0 jump ufw-after-logging-forward
		counter packets 0 bytes 0 jump ufw-reject-forward
		counter packets 0 bytes 0 jump ufw-track-forward
	}

	chain ufw-logging-deny {
		xt match "conntrack" limit rate 3/minute burst 10 packets counter packets 3 bytes 168 return
		limit rate 3/minute burst 10 packets counter packets 0 bytes 0 xt target "LOG"
	}

	chain ufw-logging-allow {
		limit rate 3/minute burst 10 packets counter packets 0 bytes 0 xt target "LOG"
	}

	chain ufw-skip-to-policy-input {
		counter packets 6 bytes 1943 drop
	}

	chain ufw-skip-to-policy-output {
		counter packets 0 bytes 0 accept
	}

	chain ufw-skip-to-policy-forward {
		counter packets 0 bytes 0 drop
	}

	chain ufw-not-local {
		xt match "addrtype" counter packets 2 bytes 2152 return
		xt match "addrtype" counter packets 295 bytes 78978 return
		xt match "addrtype" counter packets 6 bytes 1943 return
		limit rate 3/minute burst 10 packets counter packets 0 bytes 0 jump ufw-logging-deny
		counter packets 0 bytes 0 drop
	}

	chain ufw-user-input {
		ip saddr 172.31.76.25 tcp dport 22 counter packets 0 bytes 0 accept
		ip saddr 172.31.111.173 tcp dport 22 counter packets 0 bytes 0 accept
	}

	chain ufw-user-output {
	}

	chain ufw-user-forward {
	}

	chain ufw-user-logging-input {
	}

	chain ufw-user-logging-output {
	}

	chain ufw-user-logging-forward {
	}

	chain ufw-user-limit {
		limit rate 3/minute burst 5 packets counter packets 0 bytes 0 xt target "LOG"
		counter packets 0 bytes 0 xt target "REJECT"
	}

	chain ufw-user-limit-accept {
		counter packets 0 bytes 0 accept
	}
}
# Warning: table ip6 filter is managed by iptables-nft, do not touch!
table ip6 filter {
	chain ufw6-before-logging-input {
	}

	chain ufw6-before-logging-output {
	}

	chain ufw6-before-logging-forward {
	}

	chain ufw6-before-input {
		iifname "lo" counter packets 20 bytes 1400 accept
		xt match "rt" counter packets 0 bytes 0 drop
		xt match "conntrack" counter packets 119070 bytes 155640241 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		xt match "conntrack" counter packets 0 bytes 0 jump ufw6-logging-deny
		xt match "conntrack" counter packets 0 bytes 0 drop
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" xt match "hl" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" xt match "hl" counter packets 10 bytes 1280 accept
		meta l4proto ipv6-icmp xt match "icmp6" xt match "hl" counter packets 51 bytes 3672 accept
		meta l4proto ipv6-icmp xt match "icmp6" xt match "hl" counter packets 5 bytes 336 accept
		meta l4proto ipv6-icmp xt match "icmp6" xt match "hl" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" xt match "hl" counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" xt match "hl" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" xt match "hl" counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" xt match "hl" counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" xt match "hl" counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" xt match "hl" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 ip6 daddr fe80::/10 udp sport 547 udp dport 546 counter packets 0 bytes 0 accept
		ip6 daddr ff02::fb udp dport 5353 counter packets 0 bytes 0 accept
		ip6 daddr ff02::f udp dport 1900 counter packets 0 bytes 0 accept
		counter packets 13 bytes 11050 jump ufw6-user-input
	}

	chain ufw6-before-output {
		oifname "lo" counter packets 20 bytes 1400 accept
		xt match "rt" counter packets 0 bytes 0 drop
		xt match "conntrack" counter packets 74410 bytes 13437853 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" xt match "hl" counter packets 18 bytes 864 accept
		meta l4proto ipv6-icmp xt match "icmp6" xt match "hl" counter packets 51 bytes 3272 accept
		meta l4proto ipv6-icmp xt match "icmp6" xt match "hl" counter packets 10 bytes 720 accept
		meta l4proto ipv6-icmp xt match "icmp6" xt match "hl" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" xt match "hl" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" xt match "hl" counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" counter packets 33 bytes 3408 accept
		meta l4proto ipv6-icmp xt match "icmp6" xt match "hl" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" xt match "hl" counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" xt match "hl" counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" xt match "hl" counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" xt match "hl" counter packets 0 bytes 0 accept
		counter packets 718 bytes 546916 jump ufw6-user-output
	}

	chain ufw6-before-forward {
		xt match "rt" counter packets 0 bytes 0 drop
		xt match "conntrack" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		counter packets 0 bytes 0 jump ufw6-user-forward
	}

	chain ufw6-after-input {
		udp dport 137 counter packets 0 bytes 0 jump ufw6-skip-to-policy-input
		udp dport 138 counter packets 0 bytes 0 jump ufw6-skip-to-policy-input
		tcp dport 139 counter packets 0 bytes 0 jump ufw6-skip-to-policy-input
		tcp dport 445 counter packets 0 bytes 0 jump ufw6-skip-to-policy-input
		udp dport 546 counter packets 0 bytes 0 jump ufw6-skip-to-policy-input
		udp dport 547 counter packets 0 bytes 0 jump ufw6-skip-to-policy-input
	}

	chain ufw6-after-output {
	}

	chain ufw6-after-forward {
	}

	chain ufw6-after-logging-input {
	}

	chain ufw6-after-logging-output {
	}

	chain ufw6-after-logging-forward {
	}

	chain ufw6-reject-input {
	}

	chain ufw6-reject-output {
	}

	chain ufw6-reject-forward {
	}

	chain ufw6-track-input {
	}

	chain ufw6-track-output {
		meta l4proto tcp xt match "conntrack" counter packets 146 bytes 11680 accept
		meta l4proto udp xt match "conntrack" counter packets 562 bytes 534276 accept
	}

	chain ufw6-track-forward {
	}

	chain INPUT {
		type filter hook input priority filter; policy drop;
		counter packets 119169 bytes 155657979 jump ufw6-before-logging-input
		counter packets 119169 bytes 155657979 jump ufw6-before-input
		counter packets 13 bytes 11050 jump ufw6-after-input
		counter packets 13 bytes 11050 jump ufw6-after-logging-input
		counter packets 13 bytes 11050 jump ufw6-reject-input
		counter packets 13 bytes 11050 jump ufw6-track-input
	}

	chain OUTPUT {
		type filter hook output priority filter; policy accept;
		counter packets 75260 bytes 13994433 jump ufw6-before-logging-output
		counter packets 75260 bytes 13994433 jump ufw6-before-output
		counter packets 718 bytes 546916 jump ufw6-after-output
		counter packets 718 bytes 546916 jump ufw6-after-logging-output
		counter packets 718 bytes 546916 jump ufw6-reject-output
		counter packets 718 bytes 546916 jump ufw6-track-output
	}

	chain FORWARD {
		type filter hook forward priority filter; policy drop;
		counter packets 0 bytes 0 jump ufw6-before-logging-forward
		counter packets 0 bytes 0 jump ufw6-before-forward
		counter packets 0 bytes 0 jump ufw6-after-forward
		counter packets 0 bytes 0 jump ufw6-after-logging-forward
		counter packets 0 bytes 0 jump ufw6-reject-forward
		counter packets 0 bytes 0 jump ufw6-track-forward
	}

	chain ufw6-logging-deny {
	}

	chain ufw6-logging-allow {
	}

	chain ufw6-skip-to-policy-input {
		counter packets 0 bytes 0 drop
	}

	chain ufw6-skip-to-policy-output {
		counter packets 0 bytes 0 accept
	}

	chain ufw6-skip-to-policy-forward {
		counter packets 0 bytes 0 drop
	}

	chain ufw6-user-input {
	}

	chain ufw6-user-output {
	}

	chain ufw6-user-forward {
	}

	chain ufw6-user-logging-input {
	}

	chain ufw6-user-logging-output {
	}

	chain ufw6-user-logging-forward {
	}

	chain ufw6-user-limit {
	}

	chain ufw6-user-limit-accept {
	}
}
[naveen@archlinux ~]$ sudo iptables -S
-P INPUT DROP
-P FORWARD DROP
-P OUTPUT ACCEPT
-N ufw-after-forward
-N ufw-after-input
-N ufw-after-logging-forward
-N ufw-after-logging-input
-N ufw-after-logging-output
-N ufw-after-output
-N ufw-before-forward
-N ufw-before-input
-N ufw-before-logging-forward
-N ufw-before-logging-input
-N ufw-before-logging-output
-N ufw-before-output
-N ufw-logging-allow
-N ufw-logging-deny
-N ufw-not-local
-N ufw-reject-forward
-N ufw-reject-input
-N ufw-reject-output
-N ufw-skip-to-policy-forward
-N ufw-skip-to-policy-input
-N ufw-skip-to-policy-output
-N ufw-track-forward
-N ufw-track-input
-N ufw-track-output
-N ufw-user-forward
-N ufw-user-input
-N ufw-user-limit
-N ufw-user-limit-accept
-N ufw-user-logging-forward
-N ufw-user-logging-input
-N ufw-user-logging-output
-N ufw-user-output
-A INPUT -j ufw-before-logging-input
-A INPUT -j ufw-before-input
-A INPUT -j ufw-after-input
-A INPUT -j ufw-after-logging-input
-A INPUT -j ufw-reject-input
-A INPUT -j ufw-track-input
-A FORWARD -j ufw-before-logging-forward
-A FORWARD -j ufw-before-forward
-A FORWARD -j ufw-after-forward
-A FORWARD -j ufw-after-logging-forward
-A FORWARD -j ufw-reject-forward
-A FORWARD -j ufw-track-forward
-A OUTPUT -j ufw-before-logging-output
-A OUTPUT -j ufw-before-output
-A OUTPUT -j ufw-after-output
-A OUTPUT -j ufw-after-logging-output
-A OUTPUT -j ufw-reject-output
-A OUTPUT -j ufw-track-output
-A ufw-after-input -p udp -m udp --dport 137 -j ufw-skip-to-policy-input
-A ufw-after-input -p udp -m udp --dport 138 -j ufw-skip-to-policy-input
-A ufw-after-input -p tcp -m tcp --dport 139 -j ufw-skip-to-policy-input
-A ufw-after-input -p tcp -m tcp --dport 445 -j ufw-skip-to-policy-input
-A ufw-after-input -p udp -m udp --dport 67 -j ufw-skip-to-policy-input
-A ufw-after-input -p udp -m udp --dport 68 -j ufw-skip-to-policy-input
-A ufw-after-input -m addrtype --dst-type BROADCAST -j ufw-skip-to-policy-input
-A ufw-after-logging-forward -m limit --limit 3/min --limit-burst 10 -j LOG --log-prefix "[UFW BLOCK] "
-A ufw-after-logging-input -m limit --limit 3/min --limit-burst 10 -j LOG --log-prefix "[UFW BLOCK] "
-A ufw-before-forward -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
-A ufw-before-forward -p icmp -m icmp --icmp-type 3 -j ACCEPT
-A ufw-before-forward -p icmp -m icmp --icmp-type 11 -j ACCEPT
-A ufw-before-forward -p icmp -m icmp --icmp-type 12 -j ACCEPT
-A ufw-before-forward -p icmp -m icmp --icmp-type 8 -j ACCEPT
-A ufw-before-forward -j ufw-user-forward
-A ufw-before-input -i lo -j ACCEPT
-A ufw-before-input -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
-A ufw-before-input -m conntrack --ctstate INVALID -j ufw-logging-deny
-A ufw-before-input -m conntrack --ctstate INVALID -j DROP
-A ufw-before-input -p icmp -m icmp --icmp-type 3 -j ACCEPT
-A ufw-before-input -p icmp -m icmp --icmp-type 11 -j ACCEPT
-A ufw-before-input -p icmp -m icmp --icmp-type 12 -j ACCEPT
-A ufw-before-input -p icmp -m icmp --icmp-type 8 -j ACCEPT
-A ufw-before-input -p udp -m udp --sport 67 --dport 68 -j ACCEPT
-A ufw-before-input -j ufw-not-local
-A ufw-before-input -d 224.0.0.251/32 -p udp -m udp --dport 5353 -j ACCEPT
-A ufw-before-input -d 239.255.255.250/32 -p udp -m udp --dport 1900 -j ACCEPT
-A ufw-before-input -j ufw-user-input
-A ufw-before-output -o lo -j ACCEPT
-A ufw-before-output -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
-A ufw-before-output -j ufw-user-output
-A ufw-logging-allow -m limit --limit 3/min --limit-burst 10 -j LOG --log-prefix "[UFW ALLOW] "
-A ufw-logging-deny -m conntrack --ctstate INVALID -m limit --limit 3/min --limit-burst 10 -j RETURN
-A ufw-logging-deny -m limit --limit 3/min --limit-burst 10 -j LOG --log-prefix "[UFW BLOCK] "
-A ufw-not-local -m addrtype --dst-type LOCAL -j RETURN
-A ufw-not-local -m addrtype --dst-type MULTICAST -j RETURN
-A ufw-not-local -m addrtype --dst-type BROADCAST -j RETURN
-A ufw-not-local -m limit --limit 3/min --limit-burst 10 -j ufw-logging-deny
-A ufw-not-local -j DROP
-A ufw-skip-to-policy-forward -j DROP
-A ufw-skip-to-policy-input -j DROP
-A ufw-skip-to-policy-output -j ACCEPT
-A ufw-track-output -p tcp -m conntrack --ctstate NEW -j ACCEPT
-A ufw-track-output -p udp -m conntrack --ctstate NEW -j ACCEPT
-A ufw-user-input -s 172.31.76.25/32 -p tcp -m tcp --dport 22 -j ACCEPT
-A ufw-user-input -s 172.31.111.173/32 -p tcp -m tcp --dport 22 -j ACCEPT
-A ufw-user-limit -m limit --limit 3/min -j LOG --log-prefix "[UFW LIMIT BLOCK] "
-A ufw-user-limit -j REJECT --reject-with icmp-port-unreachable
-A ufw-user-limit-accept -j ACCEPT
[naveen@archlinux ~]$ ssh om@10.87.234.88
The authenticity of host '10.87.234.88 (10.87.234.88)' can't be established.
ED25519 key fingerprint is: SHA256:lTEs5ZQ3qB2WdVYwENCsWfqiJ475S/FNTGvsjbH/u1A
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:6: 172.31.76.25
    ~/.ssh/known_hosts:10: dhandepatil
    ~/.ssh/known_hosts:11: 10.87.234.87
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes 
Warning: Permanently added '10.87.234.88' (ED25519) to the list of known hosts.
om@10.87.234.88's password: 
(base) [om@DHANDEPATIL ~]$ getent hosts archlinux
getent hosts DHANDEPATIL
172.31.118.145  archlinux
172.31.76.25    DHANDEPATIL
172.31.111.173  DHANDEPATIL
(base) [om@DHANDEPATIL ~]$ exit
logout
Connection to 10.87.234.88 closed.
[naveen@archlinux ~]$ cd ~/hadoop-2.9.1

echo "===== HOSTNAME ====="
hostname

echo "===== JAVA VERSION ====="
java -version

echo "===== HADOOP VERSION ====="
bin/hadoop version

echo "===== HADOOP CONFIGURATION ====="
for f in core-site.xml hdfs-site.xml mapred-site.xml yarn-site.xml hadoop-env.sh workers slaves; do
    if [ -f "etc/hadoop/$f" ]; then
        echo "===== $f ====="
        cat "etc/hadoop/$f"
    fi
done

echo "===== HDFS DATA DIRECTORIES ====="
find ~/hadoop-2.9.1 -maxdepth 5 -type d \( -name current -o -name name -o -name data \) 2>/dev/null

echo "===== HDFS CONFIGURED ADDRESS ====="
bin/hdfs getconf -confKey fs.defaultFS
===== HOSTNAME =====
archlinux
===== JAVA VERSION =====
java version "1.8.0_45"
Java(TM) SE Runtime Environment (build 1.8.0_45-b14)
Java HotSpot(TM) 64-Bit Server VM (build 25.45-b02, mixed mode)
===== HADOOP VERSION =====
Hadoop 2.9.1
Subversion https://github.com/apache/hadoop.git -r e30710aea4e6e55e69372929106cf119af06fd0e
Compiled by root on 2018-04-16T09:33Z
Compiled with protoc 2.5.0
From source with checksum 7d6d2b655115c6cc336d662cc2b919bd
This command was run using /home/naveen/hadoop-2.9.1/share/hadoop/common/hadoop-common-2.9.1.jar
===== HADOOP CONFIGURATION =====
===== core-site.xml =====
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!--
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. See accompanying LICENSE file.
-->

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://localhost:50000</value>
</property>
</configuration>
===== hdfs-site.xml =====
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!--
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. See accompanying LICENSE file.
-->

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.namenode.name.dir</name>
<value>/home/naveen/hadoop2-dir/namenode-dir</value>
</property>
<property>
<name>dfs.datanode.data.dir</name>
<value>/home/naveen/hadoop2-dir/datanode-dir</value>
</property>
</configuration>
===== mapred-site.xml =====
<configuration>
<property>
<name>mapreduce.framework.name</name>
<value>yarn</value>
</property>
</configuration>
===== yarn-site.xml =====
<?xml version="1.0"?>
<!--
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. See accompanying LICENSE file.
-->
<configuration>
<property>
<name>yarn.nodemanager.aux-services</name> <value>mapreduce_shuffle</value>
</property>
<property>
<name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name> <value>org.apache.hadoop.mapred.ShuffleHandler</value>
</property>
<property>
<description>The hostname of the RM.</description>
<name>yarn.resourcemanager.hostname</name>
<value>localhost</value>
</property>
<property>
<description>The address of the applications manager interface in the RM.</description>
<name>yarn.resourcemanager.address</name>
<value>{yarn.resourcemanager.hostname}:8032</value>
</property>
</configuration>
===== hadoop-env.sh =====
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
export JAVA_HOME=/home/naveen/jdk-8u45-linux-x64/jdk1.8.0_45
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Set Hadoop-specific environment variables here.

# The only required environment variable is JAVA_HOME.  All others are
# optional.  When running a distributed configuration it is best to
# set JAVA_HOME in this file, so that it is correctly defined on
# remote nodes.

# The java implementation to use.
export JAVA_HOME=${JAVA_HOME}

# The jsvc implementation to use. Jsvc is required to run secure datanodes
# that bind to privileged ports to provide authentication of data transfer
# protocol.  Jsvc is not required if SASL is configured for authentication of
# data transfer protocol using non-privileged ports.
#export JSVC_HOME=${JSVC_HOME}

export HADOOP_CONF_DIR=${HADOOP_CONF_DIR:-"/etc/hadoop"}

# Extra Java CLASSPATH elements.  Automatically insert capacity-scheduler.
for f in $HADOOP_HOME/contrib/capacity-scheduler/*.jar; do
  if [ "$HADOOP_CLASSPATH" ]; then
    export HADOOP_CLASSPATH=$HADOOP_CLASSPATH:$f
  else
    export HADOOP_CLASSPATH=$f
  fi
done

# The maximum amount of heap to use, in MB. Default is 1000.
#export HADOOP_HEAPSIZE=
#export HADOOP_NAMENODE_INIT_HEAPSIZE=""

# Enable extra debugging of Hadoop's JAAS binding, used to set up
# Kerberos security.
# export HADOOP_JAAS_DEBUG=true

# Extra Java runtime options.  Empty by default.
# For Kerberos debugging, an extended option set logs more invormation
# export HADOOP_OPTS="-Djava.net.preferIPv4Stack=true -Dsun.security.krb5.debug=true -Dsun.security.spnego.debug"
export HADOOP_OPTS="$HADOOP_OPTS -Djava.net.preferIPv4Stack=true"

# Command specific options appended to HADOOP_OPTS when specified
export HADOOP_NAMENODE_OPTS="-Dhadoop.security.logger=${HADOOP_SECURITY_LOGGER:-INFO,RFAS} -Dhdfs.audit.logger=${HDFS_AUDIT_LOGGER:-INFO,NullAppender} $HADOOP_NAMENODE_OPTS"
export HADOOP_DATANODE_OPTS="-Dhadoop.security.logger=ERROR,RFAS $HADOOP_DATANODE_OPTS"

export HADOOP_SECONDARYNAMENODE_OPTS="-Dhadoop.security.logger=${HADOOP_SECURITY_LOGGER:-INFO,RFAS} -Dhdfs.audit.logger=${HDFS_AUDIT_LOGGER:-INFO,NullAppender} $HADOOP_SECONDARYNAMENODE_OPTS"

export HADOOP_NFS3_OPTS="$HADOOP_NFS3_OPTS"
export HADOOP_PORTMAP_OPTS="-Xmx512m $HADOOP_PORTMAP_OPTS"

# The following applies to multiple commands (fs, dfs, fsck, distcp etc)
export HADOOP_CLIENT_OPTS="$HADOOP_CLIENT_OPTS"
# set heap args when HADOOP_HEAPSIZE is empty
if [ "$HADOOP_HEAPSIZE" = "" ]; then
  export HADOOP_CLIENT_OPTS="-Xmx512m $HADOOP_CLIENT_OPTS"
fi
#HADOOP_JAVA_PLATFORM_OPTS="-XX:-UsePerfData $HADOOP_JAVA_PLATFORM_OPTS"

# On secure datanodes, user to run the datanode as after dropping privileges.
# This **MUST** be uncommented to enable secure HDFS if using privileged ports
# to provide authentication of data transfer protocol.  This **MUST NOT** be
# defined if SASL is configured for authentication of data transfer protocol
# using non-privileged ports.
export HADOOP_SECURE_DN_USER=${HADOOP_SECURE_DN_USER}

# Where log files are stored.  $HADOOP_HOME/logs by default.
#export HADOOP_LOG_DIR=${HADOOP_LOG_DIR}/$USER

# Where log files are stored in the secure data environment.
#export HADOOP_SECURE_DN_LOG_DIR=${HADOOP_LOG_DIR}/${HADOOP_HDFS_USER}

###
# HDFS Mover specific parameters
###
# Specify the JVM options to be used when starting the HDFS Mover.
# These options will be appended to the options specified as HADOOP_OPTS
# and therefore may override any similar flags set in HADOOP_OPTS
#
# export HADOOP_MOVER_OPTS=""

###
# Router-based HDFS Federation specific parameters
# Specify the JVM options to be used when starting the RBF Routers.
# These options will be appended to the options specified as HADOOP_OPTS
# and therefore may override any similar flags set in HADOOP_OPTS
#
# export HADOOP_DFSROUTER_OPTS=""
###

###
# Advanced Users Only!
###

# The directory where pid files are stored. /tmp by default.
# NOTE: this should be set to a directory that can only be written to by 
#       the user that will run the hadoop daemons.  Otherwise there is the
#       potential for a symlink attack.
export HADOOP_PID_DIR=${HADOOP_PID_DIR}
export HADOOP_SECURE_DN_PID_DIR=${HADOOP_PID_DIR}

# A string representing this instance of hadoop. $USER by default.
export HADOOP_IDENT_STRING=$USER
===== slaves =====
localhost
===== HDFS DATA DIRECTORIES =====
/home/naveen/hadoop-2.9.1/share/hadoop/tools/resourceestimator/data
===== HDFS CONFIGURED ADDRESS =====
hdfs://localhost:50000
[naveen@archlinux hadoop-2.9.1]$ ^C
[naveen@archlinux hadoop-2.9.1]$ hostname
ip -4 -br addr

ls -lah /home/naveen/hadoop2-dir/namenode-dir
ls -lah /home/naveen/hadoop2-dir/datanode-dir

find /home/naveen/hadoop2-dir/namenode-dir \
  -name VERSION -o -name 'fsimage_*'

jps
archlinux
lo               UNKNOWN        127.0.0.1/8 
wlp2s0           UP             10.87.234.198/24 
total 12K
drwxr-xr-x 3 naveen naveen 4.0K Nov 12 00:00 .
drwxr-xr-x 4 naveen naveen 4.0K Nov 11 02:52 ..
drwxr-xr-x 2 naveen naveen 4.0K Nov 11 23:36 current
total 12K
drwx------ 3 naveen naveen 4.0K Nov 12 00:00 .
drwxr-xr-x 4 naveen naveen 4.0K Nov 11 02:52 ..
drwxr-xr-x 3 naveen naveen 4.0K Nov 11 22:35 current
/home/naveen/hadoop2-dir/namenode-dir/current/VERSION
/home/naveen/hadoop2-dir/namenode-dir/current/fsimage_0000000000000000004
/home/naveen/hadoop2-dir/namenode-dir/current/fsimage_0000000000000000002.md5
/home/naveen/hadoop2-dir/namenode-dir/current/fsimage_0000000000000000004.md5
/home/naveen/hadoop2-dir/namenode-dir/current/fsimage_0000000000000000002
21097 Jps
[naveen@archlinux hadoop-2.9.1]$ ^C
[naveen@archlinux hadoop-2.9.1]$ echo "===== NAMENODE VERSION ====="
cat /home/naveen/hadoop2-dir/namenode-dir/current/VERSION

echo "===== DATANODE VERSION ====="
cat /home/naveen/hadoop2-dir/datanode-dir/current/VERSION
===== NAMENODE VERSION =====
#Wed Nov 11 22:34:10 IST 2026
namespaceID=1112240913
clusterID=CID-a36cb08a-817c-421c-b9ec-e9485046d5bb
cTime=1794416650190
storageType=NAME_NODE
blockpoolID=BP-1383357140-10.87.234.198-1794416650190
layoutVersion=-63
===== DATANODE VERSION =====
#Wed Nov 11 22:35:22 IST 2026
storageID=DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf
clusterID=CID-a36cb08a-817c-421c-b9ec-e9485046d5bb
cTime=0
datanodeUuid=6063523e-a8cf-4171-a32f-93e13e6ec74e
storageType=DATA_NODE
layoutVersion=-57
[naveen@archlinux hadoop-2.9.1]$ cd ~/hadoop-2.9.1

cp -r etc/hadoop etc/hadoop-backup-$(date +%F-%H%M%S)
[naveen@archlinux hadoop-2.9.1]$ nano etc/hadoop/core-site.xml
[naveen@archlinux hadoop-2.9.1]$ nano etc/hadoop/hdfs-site.xml
[naveen@archlinux hadoop-2.9.1]$ nano etc/hadoop/mapred-site.xml
[naveen@archlinux hadoop-2.9.1]$ nano etc/hadoop/yarn-site.xml
[naveen@archlinux hadoop-2.9.1]$ echo -e "archlinux\nDHANDEPATIL" > etc/hadoop/slaves
[naveen@archlinux hadoop-2.9.1]$ V
bash: V: command not found
[naveen@archlinux hadoop-2.9.1]$ grep JAVA_HOME etc/hadoop/hadoop-env.sh
export JAVA_HOME=/home/naveen/jdk-8u45-linux-x64/jdk1.8.0_45
# The only required environment variable is JAVA_HOME.  All others are
# set JAVA_HOME in this file, so that it is correctly defined on
export JAVA_HOME=${JAVA_HOME}
[naveen@archlinux hadoop-2.9.1]$ cd ~/hadoop-2.9.1

echo "===== CORE SITE ====="
cat etc/hadoop/core-site.xml

echo "===== HDFS SITE ====="
cat etc/hadoop/hdfs-site.xml

echo "===== YARN SITE ====="
cat etc/hadoop/yarn-site.xml

echo "===== WORKERS ====="
cat etc/hadoop/slaves

echo "===== HADOOP JAVA ====="
grep JAVA_HOME etc/hadoop/hadoop-env.sh
===== CORE SITE =====
<?xml version="1.0"?>
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://archlinux:9000</value>
    </property>
</configuration>
===== HDFS SITE =====
<?xml version="1.0"?>
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>2</value>
    </property>

    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:///home/naveen/hadoop2-dir/namenode-dir</value>
    </property>

    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:///home/naveen/hadoop2-dir/datanode-dir</value>
    </property>
</configuration>
===== YARN SITE =====
<?xml version="1.0"?>
<configuration>
    <property>
        <name>yarn.resourcemanager.hostname</name>
        <value>archlinux</value>
    </property>

    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>

    <property>
        <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
        <value>org.apache.hadoop.mapred.ShuffleHandler</value>
    </property>
</configuration>
===== WORKERS =====
archlinux
DHANDEPATIL
===== HADOOP JAVA =====
export JAVA_HOME=/home/naveen/jdk-8u45-linux-x64/jdk1.8.0_45
# The only required environment variable is JAVA_HOME.  All others are
# set JAVA_HOME in this file, so that it is correctly defined on
export JAVA_HOME=${JAVA_HOME}
[naveen@archlinux hadoop-2.9.1]$ V
bash: V: command not found
[naveen@archlinux hadoop-2.9.1]$ sudo cp /etc/hosts /etc/hosts.backup
sudo nano /etc/hosts
[sudo] password for naveen: 
[naveen@archlinux hadoop-2.9.1]$ getent hosts archlinux
getent hosts DHANDEPATIL
2409:40d4:242b:85be:de0:2964:6baf:879a archlinux
fe80::39ed:dd92:cb5d:2640 archlinux
172.31.76.25    DHANDEPATIL
172.31.111.173  DHANDEPATIL
10.87.234.88    DHANDEPATIL
[naveen@archlinux hadoop-2.9.1]$ 
Display all 3018 possibilities? (y or n)
[naveen@archlinux hadoop-2.9.1]$ sudo nano /etc/hosts
[naveen@archlinux hadoop-2.9.1]$ getent ahostsv4 archlinux
getent ahostsv4 DHANDEPATIL
10.87.234.198   STREAM archlinux
10.87.234.198   DGRAM  
10.87.234.198   RAW    
10.87.234.88    STREAM DHANDEPATIL
10.87.234.88    DGRAM  
10.87.234.88    RAW    
[naveen@archlinux hadoop-2.9.1]$ ping -c 3 archlinux
ping -c 3 DHANDEPATIL
PING archlinux (10.87.234.198) 56(84) bytes of data.
64 bytes from archlinux (10.87.234.198): icmp_seq=1 ttl=64 time=0.072 ms
64 bytes from archlinux (10.87.234.198): icmp_seq=2 ttl=64 time=0.075 ms
64 bytes from archlinux (10.87.234.198): icmp_seq=3 ttl=64 time=0.078 ms

--- archlinux ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2056ms
rtt min/avg/max/mdev = 0.072/0.075/0.078/0.002 ms
PING DHANDEPATIL (10.87.234.88) 56(84) bytes of data.
64 bytes from DHANDEPATIL (10.87.234.88): icmp_seq=1 ttl=64 time=222 ms
64 bytes from DHANDEPATIL (10.87.234.88): icmp_seq=2 ttl=64 time=255 ms
64 bytes from DHANDEPATIL (10.87.234.88): icmp_seq=3 ttl=64 time=27.8 ms

--- DHANDEPATIL ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
rtt min/avg/max/mdev = 27.814/168.055/254.547/100.062 ms
[naveen@archlinux hadoop-2.9.1]$ sudo systemctl enable --now sshd
systemctl status sshd --no-pager
● sshd.service - OpenSSH Daemon
     Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled; preset: disabled)
     Active: active (running) since Sat 2026-11-14 20:52:36 IST; 1h 28min left
 Invocation: 361cdf5aad5149e49cc765b8f263aba3
       Docs: man:sshd(8)
             man:sshd_config(5)
   Main PID: 731 (sshd)
      Tasks: 1 (limit: 18285)
     Memory: 1.8M (peak: 2.4M)
        CPU: 10ms
     CGroup: /system.slice/sshd.service
             └─731 "sshd: /usr/bin/sshd -D [listener] 0 of 10-100 startups"

Nov 14 20:52:35 archlinux systemd[1]: Starting OpenSSH Daemon...
Nov 14 20:52:36 archlinux sshd[731]: Server listening on 0.0.0.0 port 22.
Nov 14 20:52:36 archlinux sshd[731]: Server listening on :: port 22.
Nov 14 20:52:36 archlinux systemd[1]: Started OpenSSH Daemon.
[naveen@archlinux hadoop-2.9.1]$ sudo ufw status verbose
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW IN    172.31.76.25              
22/tcp                     ALLOW IN    172.31.111.173            

[naveen@archlinux hadoop-2.9.1]$ sudo ufw allow from 10.87.234.88 to any port 22 proto tcp
Rule added
[naveen@archlinux hadoop-2.9.1]$ mkdir -p ~/.ssh
chmod 700 ~/.ssh

ssh-keygen -t ed25519 -N "" -f ~/.ssh/id_ed25519
Generating public/private ed25519 key pair.
/home/naveen/.ssh/id_ed25519 already exists.
Overwrite (y/n)? n
[naveen@archlinux hadoop-2.9.1]$ ssh-copy-id om@DHANDEPATIL
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: ssh-add -L
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 2 key(s) remain to be installed -- if you are prompted now it is to install the new keys
om@dhandepatil's password: 

Number of key(s) added: 2

Now try logging into the machine, with: "ssh 'om@DHANDEPATIL'"
and check to make sure that only the key(s) you wanted were added.

[naveen@archlinux hadoop-2.9.1]$ V
bash: V: command not found
[naveen@archlinux hadoop-2.9.1]$ ssh om@DHANDEPATIL
(base) [om@DHANDEPATIL ~]$ hostname
whoami
DHANDEPATIL
om
(base) [om@DHANDEPATIL ~]$ exit
logout
Connection to dhandepatil closed.
[naveen@archlinux hadoop-2.9.1]$ nano ~/.ssh/config
[naveen@archlinux hadoop-2.9.1]$ chmod 600 ~/.ssh/config
[naveen@archlinux hadoop-2.9.1]$ ssh DHANDEPATIL
(base) [om@DHANDEPATIL ~]$ exit
logout
Connection to 10.87.234.88 closed.
[naveen@archlinux hadoop-2.9.1]$ ssh naveen@archlinux
The authenticity of host 'archlinux (10.87.234.198)' can't be established.
ED25519 key fingerprint is: SHA256:jLNrmMJpSy3SIDZ80GFOS/Zq1HrPaQLwhQP9r7/m6x8
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:1: localhost
    ~/.ssh/known_hosts:5: 0.0.0.0
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'archlinux' (ED25519) to the list of known hosts.
[naveen@archlinux ~]$ V
-bash: V: command not found
[naveen@archlinux ~]$ export HADOOP_CONF_DIR=${HADOOP_CONF_DIR:-"/etc/hadoop"}
[naveen@archlinux ~]$ cd ~/hadoop-2.9.1

echo "JAVA:"
java -version

echo "HADOOP HOME:"
echo $HADOOP_HOME

echo "HADOOP CONF:"
echo $HADOOP_CONF_DIR

echo "HDFS ADDRESS:"
bin/hdfs getconf -confKey fs.defaultFS

echo "REPLICATION:"
bin/hdfs getconf -confKey dfs.replication

echo "NAMENODE DIRECTORY:"
bin/hdfs getconf -confKey dfs.namenode.name.dir

echo "DATANODE DIRECTORY:"
bin/hdfs getconf -confKey dfs.datanode.data.dir
JAVA:
java version "1.8.0_45"
Java(TM) SE Runtime Environment (build 1.8.0_45-b14)
Java HotSpot(TM) 64-Bit Server VM (build 25.45-b02, mixed mode)
HADOOP HOME:
/home/naveen/hadoop-2.9.1
HADOOP CONF:
/etc/hadoop
HDFS ADDRESS:
file:///
REPLICATION:
3
NAMENODE DIRECTORY:
file:///tmp/hadoop-naveen/dfs/name
DATANODE DIRECTORY:
file:///tmp/hadoop-naveen/dfs/data
[naveen@archlinux hadoop-2.9.1]$ V
-bash: V: command not found
[naveen@archlinux hadoop-2.9.1]$ cat ~/hadoop-2.9.1/etc/hadoop/mapred-site.xml
<?xml version="1.0"?>
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>
[naveen@archlinux hadoop-2.9.1]$ cd ~/hadoop-2.9.1

echo "JAVA_HOME=$JAVA_HOME"
echo "HADOOP_HOME=$HADOOP_HOME"
echo "HADOOP_CONF_DIR=$HADOOP_CONF_DIR"

java -version
bin/hdfs getconf -confKey fs.defaultFS
JAVA_HOME=/home/naveen/jdk-8u45-linux-x64/jdk1.8.0_45
HADOOP_HOME=/home/naveen/hadoop-2.9.1
HADOOP_CONF_DIR=/etc/hadoop
java version "1.8.0_45"
Java(TM) SE Runtime Environment (build 1.8.0_45-b14)
Java HotSpot(TM) 64-Bit Server VM (build 25.45-b02, mixed mode)
file:///
[naveen@archlinux hadoop-2.9.1]$ nano ~/hadoop-2.9.1/etc/hadoop/hadoop-env.sh
[naveen@archlinux hadoop-2.9.1]$ V
-bash: V: command not found
[naveen@archlinux hadoop-2.9.1]$ cat >> ~/.bashrc <<'EOF'

export JAVA_HOME=/home/naveen/jdk-8u45-linux-x64/jdk1.8.0_45
export HADOOP_HOME=/home/naveen/hadoop-2.9.1
export HADOOP_CONF_DIR=/home/naveen/hadoop-2.9.1/etc/hadoop
export PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH
EOF

source ~/.bashrc
[naveen@archlinux hadoop-2.9.1]$ echo $HADOOP_CONF_DIR
hdfs getconf -confKey fs.defaultFS
hdfs getconf -confKey dfs.replication
hdfs getconf -confKey dfs.namenode.name.dir
hdfs getconf -confKey dfs.datanode.data.dir
/home/naveen/hadoop-2.9.1/etc/hadoop
hdfs://archlinux:9000
2
file:///home/naveen/hadoop2-dir/namenode-dir
file:///home/naveen/hadoop2-dir/datanode-dir
[naveen@archlinux hadoop-2.9.1]$ cd ~/hadoop-2.9.1/etc/hadoop

echo "===== CORE SITE ====="
cat core-site.xml

echo "===== HDFS SITE ====="
cat hdfs-site.xml

echo "===== YARN SITE ====="
cat yarn-site.xml

echo "===== MAPRED SITE ====="
cat mapred-site.xml
===== CORE SITE =====
<?xml version="1.0"?>
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://archlinux:9000</value>
    </property>
</configuration>
===== HDFS SITE =====
<?xml version="1.0"?>
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>2</value>
    </property>

    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:///home/naveen/hadoop2-dir/namenode-dir</value>
    </property>

    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:///home/naveen/hadoop2-dir/datanode-dir</value>
    </property>
</configuration>
===== YARN SITE =====
<?xml version="1.0"?>
<configuration>
    <property>
        <name>yarn.resourcemanager.hostname</name>
        <value>archlinux</value>
    </property>

    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>

    <property>
        <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
        <value>org.apache.hadoop.mapred.ShuffleHandler</value>
    </property>
</configuration>
===== MAPRED SITE =====
<?xml version="1.0"?>
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>
[naveen@archlinux hadoop]$ sudo ufw allow from 10.87.234.88 to any port 9000 proto tcp
sudo ufw allow from 10.87.234.88 to any port 50070 proto tcp
sudo ufw allow from 10.87.234.88 to any port 50010 proto tcp
sudo ufw allow from 10.87.234.88 to any port 50020 proto tcp
sudo ufw allow from 10.87.234.88 to any port 50075 proto tcp

sudo ufw allow from 10.87.234.88 to any port 8030:8033 proto tcp
sudo ufw allow from 10.87.234.88 to any port 8040:8042 proto tcp
sudo ufw allow from 10.87.234.88 to any port 8088 proto tcp
sudo ufw allow from 10.87.234.88 to any port 13562 proto tcp
[sudo] password for naveen: 
Rule added
Rule added
Rule added
Rule added
Rule added
Rule added
Rule added
Rule added
Rule added
[naveen@archlinux hadoop]$ ssh DHANDEPATIL 'echo "JAVA_HOME=$JAVA_HOME"; grep HADOOP_CONF_DIR ~/hadoop-2.9.1/etc/hadoop/hadoop-env.sh; cd ~/hadoop-2.9.1 && bin/hdfs getconf -confKey fs.defaultFS'
JAVA_HOME=
export HADOOP_CONF_DIR=/home/om/hadoop-2.9.1/etc/hadoop
hdfs://archlinux:9000
[naveen@archlinux hadoop]$ ssh naveen@archlinux 'hostname; whoami'
archlinux
naveen
[naveen@archlinux hadoop]$ ls -lah /home/naveen/hadoop2-dir/namenode-dir/current/
total 1.1M
drwxr-xr-x 2 naveen naveen 4.0K Nov 11 23:36 .
drwxr-xr-x 3 naveen naveen 4.0K Nov 12 00:00 ..
-rw-r--r-- 1 naveen naveen   42 Nov 11 22:36 edits_0000000000000000001-0000000000000000002
-rw-r--r-- 1 naveen naveen   42 Nov 11 23:36 edits_0000000000000000003-0000000000000000004
-rw-r--r-- 1 naveen naveen 1.0M Nov 11 23:36 edits_inprogress_0000000000000000005
-rw-r--r-- 1 naveen naveen  323 Nov 11 22:36 fsimage_0000000000000000002
-rw-r--r-- 1 naveen naveen   62 Nov 11 22:36 fsimage_0000000000000000002.md5
-rw-r--r-- 1 naveen naveen  323 Nov 11 23:36 fsimage_0000000000000000004
-rw-r--r-- 1 naveen naveen   62 Nov 11 23:36 fsimage_0000000000000000004.md5
-rw-r--r-- 1 naveen naveen    2 Nov 11 23:36 seen_txid
-rw-r--r-- 1 naveen naveen  218 Nov 11 22:34 VERSION
[naveen@archlinux hadoop]$ cd ~/hadoop-2.9.1
source ~/.bashrc

sbin/start-dfs.sh
Starting namenodes on [archlinux]
archlinux: starting namenode, logging to /home/naveen/hadoop-2.9.1/logs/hadoop-naveen-namenode-archlinux.out
archlinux: starting datanode, logging to /home/naveen/hadoop-2.9.1/logs/hadoop-naveen-datanode-archlinux.out
DHANDEPATIL: bash: line 1: cd: /home/naveen/hadoop-2.9.1: No such file or directory
DHANDEPATIL: bash: line 1: /home/naveen/hadoop-2.9.1/sbin/hadoop-daemon.sh: No such file or directory
Starting secondary namenodes [0.0.0.0]
0.0.0.0: starting secondarynamenode, logging to /home/naveen/hadoop-2.9.1/logs/hadoop-naveen-secondarynamenode-archlinux.out
[naveen@archlinux hadoop-2.9.1]$ jps
24947 DataNode
25156 SecondaryNameNode
24808 NameNode
25325 Jps
[naveen@archlinux hadoop-2.9.1]$ ssh DHANDEPATIL 'jps'
32054 Jps
[naveen@archlinux hadoop-2.9.1]$ hdfs dfsadmin -report
Configured Capacity: 62951051264 (58.63 GB)
Present Capacity: 42118230016 (39.23 GB)
DFS Remaining: 42118197248 (39.23 GB)
DFS Used: 32768 (32 KB)
DFS Used%: 0.00%
Under replicated blocks: 0
Blocks with corrupt replicas: 0
Missing blocks: 0
Missing blocks (with replication factor 1): 0
Pending deletion blocks: 0

-------------------------------------------------
Live datanodes (1):

Name: 10.87.234.198:50010 (archlinux)
Hostname: archlinux
Decommission Status : Normal
Configured Capacity: 62951051264 (58.63 GB)
DFS Used: 32768 (32 KB)
Non DFS Used: 17601896448 (16.39 GB)
DFS Remaining: 42118197248 (39.23 GB)
DFS Used%: 0.00%
DFS Remaining%: 66.91%
Configured Cache Capacity: 0 (0 B)
Cache Used: 0 (0 B)
Cache Remaining: 0 (0 B)
Cache Used%: 100.00%
Cache Remaining%: 0.00%
Xceivers: 1
Last contact: Sat Nov 14 19:39:51 IST 2026
Last Block Report: Sat Nov 14 19:38:48 IST 2026


[naveen@archlinux hadoop-2.9.1]$ cd ~/hadoop-2.9.1
source ~/.bashrc
sbin/stop-dfs.sh
Stopping namenodes on [archlinux]
archlinux: stopping namenode
jarchlinux: stopping datanode
DHANDEPATIL: bash: line 1: cd: /home/naveen/hadoop-2.9.1: No such file or directory
DHANDEPATIL: bash: line 1: /home/naveen/hadoop-2.9.1/sbin/hadoop-daemon.sh: No such file or directory
Stopping secondary namenodes [0.0.0.0]
0.0.0.0: stopping secondarynamenode
[naveen@archlinux hadoop-2.9.1]$ jsp
-bash: jsp: command not found
[naveen@archlinux hadoop-2.9.1]$ jps
25887 Jps
[naveen@archlinux hadoop-2.9.1]$ V
-bash: V: command not found
[naveen@archlinux hadoop-2.9.1]$ sudo mkdir -p /opt
sudo ln -s /home/naveen/hadoop-2.9.1 /opt/hadoop-2.9.1
[naveen@archlinux hadoop-2.9.1]$ cat >> ~/.bashrc <<'EOF'

export HADOOP_HOME=/opt/hadoop-2.9.1
export HADOOP_CONF_DIR=/opt/hadoop-2.9.1/etc/hadoop
export PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH
EOF

source ~/.bashrc
[naveen@archlinux hadoop-2.9.1]$ V
-bash: V: command not found
[naveen@archlinux hadoop-2.9.1]$ nano /opt/hadoop-2.9.1/etc/hadoop/hadoop-env.sh
[naveen@archlinux hadoop-2.9.1]$ echo $HADOOP_HOME
echo $HADOOP_CONF_DIR
hdfs getconf -confKey fs.defaultFS
/opt/hadoop-2.9.1
/opt/hadoop-2.9.1/etc/hadoop
hdfs://archlinux:9000
[naveen@archlinux hadoop-2.9.1]$ ssh DHANDEPATIL 'ls -ld /opt/hadoop-2.9.1'
ssh DHANDEPATIL 'ls /opt/hadoop-2.9.1/sbin/hadoop-daemon.sh'
ssh DHANDEPATIL 'cd /opt/hadoop-2.9.1 && bin/hdfs getconf -confKey fs.defaultFS'
lrwxrwxrwx 1 root root 21 Nov 14 19:48 /opt/hadoop-2.9.1 -> /home/om/hadoop-2.9.1
/opt/hadoop-2.9.1/sbin/hadoop-daemon.sh
hdfs://archlinux:9000
[naveen@archlinux hadoop-2.9.1]$ cd /opt/hadoop-2.9.1
sbin/start-dfs.sh
Starting namenodes on [archlinux]
archlinux: starting namenode, logging to /home/naveen/hadoop-2.9.1/logs/hadoop-naveen-namenode-archlinux.out
archlinux: starting datanode, logging to /home/naveen/hadoop-2.9.1/logs/hadoop-naveen-datanode-archlinux.out
DHANDEPATIL: bash: line 1: cd: /home/naveen/hadoop-2.9.1: No such file or directory
DHANDEPATIL: bash: line 1: /home/naveen/hadoop-2.9.1/sbin/hadoop-daemon.sh: No such file or directory
Starting secondary namenodes [0.0.0.0]
0.0.0.0: starting secondarynamenode, logging to /home/naveen/hadoop-2.9.1/logs/hadoop-naveen-secondarynamenode-archlinux.out
[naveen@archlinux hadoop-2.9.1]$ jps
ssh DHANDEPATIL 'jps'
hdfs dfsadmin -report
27044 Jps
26679 DataNode
26872 SecondaryNameNode
26540 NameNode
32755 Jps
Configured Capacity: 62951051264 (58.63 GB)
Present Capacity: 42115432448 (39.22 GB)
DFS Remaining: 42115399680 (39.22 GB)
DFS Used: 32768 (32 KB)
DFS Used%: 0.00%
Under replicated blocks: 0
Blocks with corrupt replicas: 0
Missing blocks: 0
Missing blocks (with replication factor 1): 0
Pending deletion blocks: 0

-------------------------------------------------
Live datanodes (1):

Name: 10.87.234.198:50010 (archlinux)
Hostname: archlinux
Decommission Status : Normal
Configured Capacity: 62951051264 (58.63 GB)
DFS Used: 32768 (32 KB)
Non DFS Used: 17604694016 (16.40 GB)
DFS Remaining: 42115399680 (39.22 GB)
DFS Used%: 0.00%
DFS Remaining%: 66.90%
Configured Cache Capacity: 0 (0 B)
Cache Used: 0 (0 B)
Cache Remaining: 0 (0 B)
Cache Used%: 100.00%
Cache Remaining%: 0.00%
Xceivers: 1
Last contact: Sat Nov 14 19:49:18 IST 2026
Last Block Report: Sat Nov 14 19:49:09 IST 2026


[naveen@archlinux hadoop-2.9.1]$ ^C
[naveen@archlinux hadoop-2.9.1]$ hdfs dfsadmin -report
Configured Capacity: 564814163968 (526.02 GB)
Present Capacity: 449844981760 (418.95 GB)
DFS Remaining: 449844924416 (418.95 GB)
DFS Used: 57344 (56 KB)
DFS Used%: 0.00%
Under replicated blocks: 0
Blocks with corrupt replicas: 0
Missing blocks: 0
Missing blocks (with replication factor 1): 0
Pending deletion blocks: 0

-------------------------------------------------
Live datanodes (2):

Name: 10.87.234.198:50010 (archlinux)
Hostname: archlinux
Decommission Status : Normal
Configured Capacity: 62951051264 (58.63 GB)
DFS Used: 32768 (32 KB)
Non DFS Used: 17605255168 (16.40 GB)
DFS Remaining: 42114838528 (39.22 GB)
DFS Used%: 0.00%
DFS Remaining%: 66.90%
Configured Cache Capacity: 0 (0 B)
Cache Used: 0 (0 B)
Cache Remaining: 0 (0 B)
Cache Used%: 100.00%
Cache Remaining%: 0.00%
Xceivers: 1
Last contact: Sat Nov 14 19:51:06 IST 2026
Last Block Report: Sat Nov 14 19:49:09 IST 2026


Name: 10.87.234.88:50010 (DHANDEPATIL)
Hostname: DHANDEPATIL
Decommission Status : Normal
Configured Capacity: 501863112704 (467.40 GB)
DFS Used: 24576 (24 KB)
Non DFS Used: 68564525056 (63.86 GB)
DFS Remaining: 407730085888 (379.73 GB)
DFS Used%: 0.00%
DFS Remaining%: 81.24%
Configured Cache Capacity: 0 (0 B)
Cache Used: 0 (0 B)
Cache Remaining: 0 (0 B)
Cache Used%: 100.00%
Cache Remaining%: 0.00%
Xceivers: 1
Last contact: Sat Nov 14 19:51:04 IST 2026
Last Block Report: Sat Nov 14 19:50:49 IST 2026


[naveen@archlinux hadoop-2.9.1]$ cd /home/naveen/hadoop-2.9.1

export JAVA_HOME=/home/naveen/jdk-8u45-linux-x64/jdk1.8.0_45
export HADOOP_HOME=/home/naveen/hadoop-2.9.1
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop

sbin/start-yarn.sh
starting yarn daemons
starting resourcemanager, logging to /home/naveen/hadoop-2.9.1/logs/yarn-naveen-resourcemanager-archlinux.out
archlinux: starting nodemanager, logging to /home/naveen/hadoop-2.9.1/logs/yarn-naveen-nodemanager-archlinux.out
DHANDEPATIL: bash: line 1: cd: /home/naveen/hadoop-2.9.1: No such file or directory
DHANDEPATIL: bash: line 1: /home/naveen/hadoop-2.9.1/sbin/yarn-daemon.sh: No such file or directory
[naveen@archlinux hadoop-2.9.1]$ jps
yarn node -list
27536 NodeManager
27894 Jps
27431 ResourceManager
26679 DataNode
26872 SecondaryNameNode
26540 NameNode
26/11/14 19:51:27 INFO client.RMProxy: Connecting to ResourceManager at archlinux/10.87.234.198:8032
Total Nodes:1
         Node-Id	     Node-State	Node-Http-Address	Number-of-Running-Containers
 archlinux:40585	        RUNNING	   archlinux:8042	                           0
[naveen@archlinux hadoop-2.9.1]$ yarn node -list
26/11/14 19:52:38 INFO client.RMProxy: Connecting to ResourceManager at archlinux/10.87.234.198:8032
Total Nodes:2
         Node-Id	     Node-State	Node-Http-Address	Number-of-Running-Containers
 archlinux:40585	        RUNNING	   archlinux:8042	                           0
DHANDEPATIL:39501	        RUNNING	 DHANDEPATIL:8042	                           0
[naveen@archlinux hadoop-2.9.1]$ mkdir -p ~/hadoop-test

echo "network intrusion detection using hadoop spark" > ~/hadoop-test/input.txt
echo "hadoop stores data and spark processes data" >> ~/hadoop-test/input.txt
[naveen@archlinux hadoop-2.9.1]$ hdfs dfs -mkdir -p /test/input
hdfs dfs -put -f ~/hadoop-test/input.txt /test/input/
[naveen@archlinux hadoop-2.9.1]$ hdfs dfs -mkdir -p /test/input
hdfs dfs -put -f ~/hadoop-test/input.txt /test/input/
[naveen@archlinux hadoop-2.9.1]$ hdfs dfs -ls /test/input
Found 1 items
-rw-r--r--   2 naveen supergroup         91 2026-11-14 19:53 /test/input/input.txt
[naveen@archlinux hadoop-2.9.1]$ hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.9.1.jar \
wordcount /test/input /test/output
26/11/14 19:53:41 INFO client.RMProxy: Connecting to ResourceManager at archlinux/10.87.234.198:8032
26/11/14 19:53:42 INFO input.FileInputFormat: Total input files to process : 1
26/11/14 19:53:43 INFO mapreduce.JobSubmitter: number of splits:1
26/11/14 19:53:43 INFO Configuration.deprecation: yarn.resourcemanager.system-metrics-publisher.enabled is deprecated. Instead, use yarn.system-metrics-publisher.enabled
26/11/14 19:53:43 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1794666080258_0001
26/11/14 19:53:44 INFO impl.YarnClientImpl: Submitted application application_1794666080258_0001
26/11/14 19:53:44 INFO mapreduce.Job: The url to track the job: http://archlinux:8088/proxy/application_1794666080258_0001/
26/11/14 19:53:44 INFO mapreduce.Job: Running job: job_1794666080258_0001

Broadcast message from root@archlinux (Sat 2026-11-14 19:58:02 IST):

The system will sleep now!

26/11/14 20:12:29 INFO mapreduce.Job: Job job_1794666080258_0001 running in uber mode : false
26/11/14 20:12:29 INFO mapreduce.Job:  map 0% reduce 0%
26/11/14 20:12:29 INFO mapreduce.Job: Job job_1794666080258_0001 failed with state FAILED due to: Application application_1794666080258_0001 failed 2 times due to Error launching appattempt_1794666080258_0001_000002. Got exception: org.apache.hadoop.net.ConnectTimeoutException: Call From archlinux/10.87.234.198 to DHANDEPATIL:39501 failed on socket timeout exception: org.apache.hadoop.net.ConnectTimeoutException: 20000 millis timeout while waiting for channel to be ready for connect. ch : java.nio.channels.SocketChannel[connection-pending remote=DHANDEPATIL/10.87.234.88:39501]; For more details see:  http://wiki.apache.org/hadoop/SocketTimeout
	at sun.reflect.GeneratedConstructorAccessor37.newInstance(Unknown Source)
	at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)
	at java.lang.reflect.Constructor.newInstance(Constructor.java:422)
	at org.apache.hadoop.net.NetUtils.wrapWithMessage(NetUtils.java:824)
	at org.apache.hadoop.net.NetUtils.wrapException(NetUtils.java:774)
	at org.apache.hadoop.ipc.Client.getRpcResponse(Client.java:1497)
	at org.apache.hadoop.ipc.Client.call(Client.java:1439)
	at org.apache.hadoop.ipc.Client.call(Client.java:1349)
	at org.apache.hadoop.ipc.ProtobufRpcEngine$Invoker.invoke(ProtobufRpcEngine.java:227)
	at org.apache.hadoop.ipc.ProtobufRpcEngine$Invoker.invoke(ProtobufRpcEngine.java:116)
	at com.sun.proxy.$Proxy82.startContainers(Unknown Source)
	at org.apache.hadoop.yarn.api.impl.pb.client.ContainerManagementProtocolPBClientImpl.startContainers(ContainerManagementProtocolPBClientImpl.java:128)
	at sun.reflect.GeneratedMethodAccessor14.invoke(Unknown Source)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:497)
	at org.apache.hadoop.io.retry.RetryInvocationHandler.invokeMethod(RetryInvocationHandler.java:422)
	at org.apache.hadoop.io.retry.RetryInvocationHandler$Call.invokeMethod(RetryInvocationHandler.java:165)
	at org.apache.hadoop.io.retry.RetryInvocationHandler$Call.invoke(RetryInvocationHandler.java:157)
	at org.apache.hadoop.io.retry.RetryInvocationHandler$Call.invokeOnce(RetryInvocationHandler.java:95)
	at org.apache.hadoop.io.retry.RetryInvocationHandler.invoke(RetryInvocationHandler.java:359)
	at com.sun.proxy.$Proxy83.startContainers(Unknown Source)
	at org.apache.hadoop.yarn.server.resourcemanager.amlauncher.AMLauncher.launch(AMLauncher.java:122)
	at org.apache.hadoop.yarn.server.resourcemanager.amlauncher.AMLauncher.run(AMLauncher.java:307)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
	at java.lang.Thread.run(Thread.java:745)
Caused by: org.apache.hadoop.net.ConnectTimeoutException: 20000 millis timeout while waiting for channel to be ready for connect. ch : java.nio.channels.SocketChannel[connection-pending remote=DHANDEPATIL/10.87.234.88:39501]
	at org.apache.hadoop.net.NetUtils.connect(NetUtils.java:534)
	at org.apache.hadoop.ipc.Client$Connection.setupConnection(Client.java:687)
	at org.apache.hadoop.ipc.Client$Connection.setupIOstreams(Client.java:790)
	at org.apache.hadoop.ipc.Client$Connection.access$3500(Client.java:411)
	at org.apache.hadoop.ipc.Client.getConnection(Client.java:1554)
	at org.apache.hadoop.ipc.Client.call(Client.java:1385)
	... 19 more
. Failing the application.
26/11/14 20:12:29 INFO mapreduce.Job: Counters: 0
[naveen@archlinux hadoop-2.9.1]$
```

---

## Part 2 — Cluster execution, YARN diagnostics, and subsequent project work

The following is the second supplied file, retained in its original order.

```text
[naveen@archlinux ~]$ yarn application -list -appStates ALL
26/11/14 20:04:31 INFO client.RMProxy: Connecting to ResourceManager at archlinux/10.87.234.198:8032
Total number of applications (application-types: [], states: [NEW, NEW_SAVING, SUBMITTED, ACCEPTED, RUNNING, FINISHED, FAILED, KILLED] and tags: []):1
                Application-Id	    Application-Name	    Application-Type	      User	     Queue	             State	       Final-State	       Progress	                       Tracking-URL
application_1794666080258_0001	          word count	           MAPREDUCE	    naveen	   default	          ACCEPTED	         UNDEFINED	             0%	                                N/A
[naveen@archlinux ~]$ yarn node -list
26/11/14 20:04:48 INFO client.RMProxy: Connecting to ResourceManager at archlinux/10.87.234.198:8032
Total Nodes:2
         Node-Id	     Node-State	Node-Http-Address	Number-of-Running-Containers
 archlinux:40585	        RUNNING	   archlinux:8042	                           0
DHANDEPATIL:39501	        RUNNING	 DHANDEPATIL:8042	                           1
[naveen@archlinux ~]$ yarn logs -applicationId application_1794666080258_0001
26/11/14 20:04:55 INFO client.RMProxy: Connecting to ResourceManager at archlinux/10.87.234.198:8032
Can not find any log file matching the pattern: [ALL] for the container: container_1794666080258_0001_02_000001 within the application: application_1794666080258_0001
Can not find the logs for the application: application_1794666080258_0001 with the appOwner: naveen
[naveen@archlinux ~]$ yarn application -status application_1794666080258_0001
26/11/14 20:05:29 INFO client.RMProxy: Connecting to ResourceManager at archlinux/10.87.234.198:8032
Application Report : 
	Application-Id : application_1794666080258_0001
	Application-Name : word count
	Application-Type : MAPREDUCE
	User : naveen
	Queue : default
	Application Priority : 0
	Start-Time : 1794666224279
	Finish-Time : 0
	Progress : 0%
	State : ACCEPTED
	Final-State : UNDEFINED
	Tracking-URL : N/A
	RPC Port : -1
	AM Host : N/A
	Aggregate Resource Allocation : 1438388 MB-seconds, 701 vcore-seconds
	Aggregate Resource Preempted : 0 MB-seconds, 0 vcore-seconds
	Log Aggregation Status : DISABLED
	Diagnostics : [Sat Nov 14 20:03:08 +0530 2026] Scheduler has assigned a container for AM, waiting for AM container to be launched
	Unmanaged Application : false
	Application Node Label Expression : <Not set>
	AM container Node Label Expression : <DEFAULT_PARTITION>
	TimeoutType : LIFETIME	ExpiryTime : UNLIMITED	RemainingTime : -1seconds

[naveen@archlinux ~]$ yarn applicationattempt -list application_1794666080258_0001
26/11/14 20:05:36 INFO client.RMProxy: Connecting to ResourceManager at archlinux/10.87.234.198:8032
Total number of application attempts :2
         ApplicationAttempt-Id	               State	                    AM-Container-Id	                       Tracking-URL
appattempt_1794666080258_0001_000001	              FAILED	container_1794666080258_0001_01_000001	http://archlinux:8088/cluster/app/application_1794666080258_0001
appattempt_1794666080258_0001_000002	           ALLOCATED	container_1794666080258_0001_02_000001	http://archlinux:8088/proxy/application_1794666080258_0001/
[naveen@archlinux ~]$ yarn applicationattempt -status 1794666080258_0001_000002
26/11/14 20:06:14 INFO client.RMProxy: Connecting to ResourceManager at archlinux/10.87.234.198:8032
Exception in thread "main" java.lang.IllegalArgumentException: Invalid AppAttemptId prefix: 1794666080258_0001_000002
	at org.apache.hadoop.yarn.api.records.ApplicationAttemptId.fromString(ApplicationAttemptId.java:144)
	at org.apache.hadoop.yarn.client.cli.ApplicationCLI.printApplicationAttemptReport(ApplicationCLI.java:415)
	at org.apache.hadoop.yarn.client.cli.ApplicationCLI.run(ApplicationCLI.java:215)
	at org.apache.hadoop.util.ToolRunner.run(ToolRunner.java:76)
	at org.apache.hadoop.util.ToolRunner.run(ToolRunner.java:90)
	at org.apache.hadoop.yarn.client.cli.ApplicationCLI.main(ApplicationCLI.java:100)
[naveen@archlinux ~]$ ssh DHANDEPATIL 'ls -lt /home/om/hadoop-2.9.1/logs/ | head -20'
total 1520
drwxr-xr-x 2 om om   4096 Nov 14 20:06 userlogs
-rw-r--r-- 1 om om 399835 Nov 14 20:04 yarn-om-nodemanager-DHANDEPATIL.log
-rw-r--r-- 1 om om 269072 Nov 14 19:53 hadoop-om-datanode-DHANDEPATIL.log
-rw-r--r-- 1 om om   1508 Nov 14 19:52 yarn-om-nodemanager-DHANDEPATIL.out
-rw-r--r-- 1 om om    846 Nov 14 19:50 hadoop-om-datanode-DHANDEPATIL.out
-rw-r--r-- 1 om om 278044 Nov  8 22:42 hadoop-om-namenode-DHANDEPATIL.log
-rw-r--r-- 1 om om 207836 Nov  8 22:42 hadoop-om-secondarynamenode-DHANDEPATIL.log
-rw-r--r-- 1 om om   5281 Nov  6 17:26 hadoop-om-namenode-DHANDEPATIL.out
-rw-r--r-- 1 om om    846 Nov  6 17:24 hadoop-om-secondarynamenode-DHANDEPATIL.out
-rw-r--r-- 1 om om    846 Nov  6 17:24 hadoop-om-datanode-DHANDEPATIL.out.1
-rw-r--r-- 1 om om 246877 Nov  6 17:23 yarn-om-resourcemanager-DHANDEPATIL.log
-rw-r--r-- 1 om om    846 Nov  6 17:20 hadoop-om-datanode-DHANDEPATIL.out.2
-rw-r--r-- 1 om om    846 Nov  6 17:19 hadoop-om-datanode-DHANDEPATIL.out.3
-rw-r--r-- 1 om om   5281 Nov  6 17:08 hadoop-om-namenode-DHANDEPATIL.out.1
-rw-r--r-- 1 om om   1508 Nov  6 17:05 yarn-om-nodemanager-DHANDEPATIL.out.1
-rw-r--r-- 1 om om   1524 Nov  6 17:05 yarn-om-resourcemanager-DHANDEPATIL.out
-rw-r--r-- 1 om om    846 Nov  6 17:05 hadoop-om-secondarynamenode-DHANDEPATIL.out.1
-rw-r--r-- 1 om om    846 Nov  6 17:05 hadoop-om-datanode-DHANDEPATIL.out.4
-rw-r--r-- 1 om om   1515 Oct 27 11:05 yarn-om-nodemanager-DHANDEPATIL.out.2
[naveen@archlinux ~]$ ssh DHANDEPATIL 'grep -iE "error|exception|failed|denied|launch|container" /home/om/hadoop-2.9.1/logs/yarn-*-nodemanager-*.log | tail -50'
2026-11-14 19:52:32,752 INFO org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.yarn.server.nodemanager.containermanager.container.ContainerEventType for class org.apache.hadoop.yarn.server.nodemanager.containermanager.ContainerManagerImpl$ContainerEventDispatcher
2026-11-14 19:52:32,753 INFO org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.yarn.server.nodemanager.containermanager.application.ApplicationEventType for class org.apache.hadoop.yarn.server.nodemanager.containermanager.ContainerManagerImpl$ApplicationEventDispatcher
2026-11-14 19:52:32,754 INFO org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.event.LocalizationEventType for class org.apache.hadoop.yarn.server.nodemanager.containermanager.ContainerManagerImpl$LocalizationEventHandlerWrapper
2026-11-14 19:52:32,755 INFO org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.yarn.server.nodemanager.containermanager.AuxServicesEventType for class org.apache.hadoop.yarn.server.nodemanager.containermanager.AuxServices
2026-11-14 19:52:32,755 INFO org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.yarn.server.nodemanager.containermanager.monitor.ContainersMonitorEventType for class org.apache.hadoop.yarn.server.nodemanager.containermanager.monitor.ContainersMonitorImpl
2026-11-14 19:52:32,756 INFO org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.yarn.server.nodemanager.containermanager.launcher.ContainersLauncherEventType for class org.apache.hadoop.yarn.server.nodemanager.containermanager.launcher.ContainersLauncher
2026-11-14 19:52:32,757 INFO org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.yarn.server.nodemanager.containermanager.scheduler.ContainerSchedulerEventType for class org.apache.hadoop.yarn.server.nodemanager.containermanager.scheduler.ContainerScheduler
2026-11-14 19:52:32,782 INFO org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.yarn.server.nodemanager.ContainerManagerEventType for class org.apache.hadoop.yarn.server.nodemanager.containermanager.ContainerManagerImpl
2026-11-14 19:52:32,988 INFO org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.yarn.server.nodemanager.containermanager.loghandler.event.LogHandlerEventType for class org.apache.hadoop.yarn.server.nodemanager.containermanager.loghandler.NonAggregatingLogHandler
2026-11-14 19:52:32,990 INFO org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.sharedcache.SharedCacheUploadEventType for class org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.sharedcache.SharedCacheUploadService
2026-11-14 19:52:32,990 INFO org.apache.hadoop.yarn.server.nodemanager.containermanager.ContainerManagerImpl: AMRMProxyService is disabled
2026-11-14 19:52:32,990 INFO org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.ResourceLocalizationService: per directory file limit = 8192
2026-11-14 19:52:33,024 INFO org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.ResourceLocalizationService: Disk Validator: yarn.nodemanager.disk-validator is loaded.
2026-11-14 19:52:33,031 INFO org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.event.LocalizerEventType for class org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.ResourceLocalizationService$LocalizerTracker
2026-11-14 19:52:33,064 INFO org.apache.hadoop.yarn.server.nodemanager.containermanager.AuxServices: Adding auxiliary service mapreduce_shuffle, "mapreduce_shuffle"
2026-11-14 19:52:33,115 INFO org.apache.hadoop.yarn.server.nodemanager.containermanager.monitor.ContainersMonitorImpl:  Using ResourceCalculatorPlugin : org.apache.hadoop.yarn.util.ResourceCalculatorPlugin@1a5b6f42
2026-11-14 19:52:33,115 INFO org.apache.hadoop.yarn.server.nodemanager.containermanager.monitor.ContainersMonitorImpl:  Using ResourceCalculatorProcessTree : null
2026-11-14 19:52:33,117 INFO org.apache.hadoop.yarn.server.nodemanager.containermanager.monitor.ContainersMonitorImpl: Physical memory check enabled: true
2026-11-14 19:52:33,117 INFO org.apache.hadoop.yarn.server.nodemanager.containermanager.monitor.ContainersMonitorImpl: Virtual memory check enabled: true
2026-11-14 19:52:33,117 INFO org.apache.hadoop.yarn.server.nodemanager.containermanager.monitor.ContainersMonitorImpl: ContainersMonitor enabled: true
2026-11-14 19:52:33,122 WARN org.apache.hadoop.yarn.server.nodemanager.containermanager.monitor.ContainersMonitorImpl: NodeManager configured with 8 G physical memory allocated to containers, which is more than 80% of the total physical memory available (5.6 G). Thrashing might happen.
2026-11-14 19:52:33,122 INFO org.apache.hadoop.yarn.server.nodemanager.containermanager.ContainerManagerImpl: Not a recoverable state store. Nothing to recover.
2026-11-14 19:52:33,379 INFO org.apache.hadoop.yarn.factories.impl.pb.RpcServerFactoryPBImpl: Adding protocol org.apache.hadoop.yarn.api.ContainerManagementProtocolPB to the server
2026-11-14 19:52:33,406 INFO org.apache.hadoop.yarn.server.nodemanager.security.NMContainerTokenSecretManager: Updating node address : DHANDEPATIL:39501
2026-11-14 19:52:33,421 INFO org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.ResourceLocalizationService: Localizer started on port 8040
2026-11-14 19:52:33,478 INFO org.apache.hadoop.yarn.server.nodemanager.containermanager.ContainerManagerImpl: ContainerManager started at DHANDEPATIL/10.87.234.88:39501
2026-11-14 19:52:33,478 INFO org.apache.hadoop.yarn.server.nodemanager.containermanager.ContainerManagerImpl: ContainerManager bound to 0.0.0.0/0.0.0.0:0
2026-11-14 19:52:35,077 INFO org.apache.hadoop.yarn.server.nodemanager.NodeStatusUpdaterImpl: Sending out 0 NM container statuses: []
2026-11-14 19:52:35,086 INFO org.apache.hadoop.yarn.server.nodemanager.NodeStatusUpdaterImpl: Registering with RM using containers :[]
2026-11-14 19:52:35,408 INFO org.apache.hadoop.yarn.server.nodemanager.security.NMContainerTokenSecretManager: Rolling master-key for container-tokens, got key with id -786992573
2026-11-14 19:52:35,410 INFO org.apache.hadoop.yarn.server.nodemanager.security.NMTokenSecretManagerInNM: Rolling master-key for container-tokens, got key with id -155214739
2026-11-14 20:02:33,420 INFO org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.ResourceLocalizationService: Cache Size Before Clean: 0, Total Deleted: 0, Public Deleted: 0, Private Deleted: 0
2026-11-14 20:03:08,636 WARN org.apache.hadoop.yarn.server.nodemanager.containermanager.ContainerManagerImpl: couldn't find app application_1794666080258_0001 while processing FINISH_CONTAINERS event
2026-11-14 20:04:55,928 WARN org.apache.hadoop.yarn.webapp.GenericExceptionHandler: INTERNAL_SERVER_ERROR
javax.ws.rs.WebApplicationException: org.apache.hadoop.yarn.webapp.NotFoundException: java.lang.Exception: Unknown container. Container either has not started or has already completed or doesn't belong to this node at all.
	at org.apache.hadoop.yarn.server.nodemanager.webapp.NMWebServices.getContainerLogsInfo(NMWebServices.java:294)
	at com.sun.jersey.spi.container.JavaMethodInvokerFactory$1.invoke(JavaMethodInvokerFactory.java:60)
	at com.sun.jersey.spi.container.servlet.WebComponent.service(WebComponent.java:416)
	at com.sun.jersey.spi.container.servlet.ServletContainer.service(ServletContainer.java:537)
	at com.sun.jersey.spi.container.servlet.ServletContainer.doFilter(ServletContainer.java:886)
	at com.sun.jersey.spi.container.servlet.ServletContainer.doFilter(ServletContainer.java:834)
	at com.sun.jersey.spi.container.servlet.ServletContainer.doFilter(ServletContainer.java:795)
Caused by: org.apache.hadoop.yarn.webapp.NotFoundException: java.lang.Exception: Unknown container. Container either has not started or has already completed or doesn't belong to this node at all.
	at org.apache.hadoop.yarn.server.nodemanager.webapp.ContainerLogsUtils.getApplicationForContainer(ContainerLogsUtils.java:124)
	at org.apache.hadoop.yarn.server.nodemanager.webapp.ContainerLogsUtils.getContainerLogDirs(ContainerLogsUtils.java:59)
	at org.apache.hadoop.yarn.server.nodemanager.webapp.dao.NMContainerLogsInfo.getContainerLogsInfo(NMContainerLogsInfo.java:62)
	at org.apache.hadoop.yarn.server.nodemanager.webapp.dao.NMContainerLogsInfo.<init>(NMContainerLogsInfo.java:54)
	at org.apache.hadoop.yarn.server.nodemanager.webapp.NMWebServices.getContainerLogsInfo(NMWebServices.java:253)
Caused by: java.lang.Exception: Unknown container. Container either has not started or has already completed or doesn't belong to this node at all.
	at org.apache.hadoop.yarn.webapp.NotFoundException.<init>(NotFoundException.java:45)
[naveen@archlinux ~]$ ls -lt /home/naveen/hadoop-2.9.1/logs/ | head -20
total 636
drwxr-xr-x 2 naveen naveen   4096 Nov 14 20:05 userlogs
-rw-r--r-- 1 naveen naveen  92925 Nov 14 20:04 yarn-naveen-resourcemanager-archlinux.log
-rw-r--r-- 1 naveen naveen 168227 Nov 14 20:01 yarn-naveen-nodemanager-archlinux.log
-rw-r--r-- 1 naveen naveen 120244 Nov 14 19:58 hadoop-naveen-namenode-archlinux.log
-rw-r--r-- 1 naveen naveen  94713 Nov 14 19:58 hadoop-naveen-datanode-archlinux.log
-rw-r--r-- 1 naveen naveen   1508 Nov 14 19:51 yarn-naveen-nodemanager-archlinux.out
-rw-r--r-- 1 naveen naveen   1524 Nov 14 19:51 yarn-naveen-resourcemanager-archlinux.out
-rw-r--r-- 1 naveen naveen  96804 Nov 14 19:50 hadoop-naveen-secondarynamenode-archlinux.log
-rw-r--r-- 1 naveen naveen    850 Nov 14 19:49 hadoop-naveen-secondarynamenode-archlinux.out
-rw-r--r-- 1 naveen naveen    850 Nov 14 19:49 hadoop-naveen-datanode-archlinux.out
-rw-r--r-- 1 naveen naveen    850 Nov 14 19:49 hadoop-naveen-namenode-archlinux.out
-rw-r--r-- 1 naveen naveen    850 Nov 14 19:38 hadoop-naveen-secondarynamenode-archlinux.out.1
-rw-r--r-- 1 naveen naveen    850 Nov 14 19:38 hadoop-naveen-datanode-archlinux.out.1
-rw-r--r-- 1 naveen naveen    850 Nov 14 19:38 hadoop-naveen-namenode-archlinux.out.1
-rw-r--r-- 1 naveen naveen   1515 Nov 11 22:35 yarn-naveen-nodemanager-archlinux.out.1
-rw-r--r-- 1 naveen naveen    834 Nov 11 22:35 yarn-naveen-resourcemanager-archlinux.out.1
-rw-r--r-- 1 naveen naveen    850 Nov 11 22:35 hadoop-naveen-secondarynamenode-archlinux.out.2
-rw-r--r-- 1 naveen naveen    850 Nov 11 22:35 hadoop-naveen-datanode-archlinux.out.2
-rw-r--r-- 1 naveen naveen    850 Nov 11 22:35 hadoop-naveen-namenode-archlinux.out.2
[naveen@archlinux ~]$ grep -iE "error|exception|failed|launch|container" /home/naveen/hadoop-2.9.1/logs/yarn-*-resourcemanager-*.log | tail -40
2026-11-14 19:51:20,237 INFO org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CapacitySchedulerQueueManager: Initialized queue: root: numChildQueue= 1, capacity=1.0, absoluteCapacity=1.0, usedResources=<memory:0, vCores:0>usedCapacity=0.0, numApps=0, numContainers=0
2026-11-14 19:51:20,238 INFO org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CapacitySchedulerQueueManager: Initialized root queue root: numChildQueue= 1, capacity=1.0, absoluteCapacity=1.0, usedResources=<memory:0, vCores:0>usedCapacity=0.0, numApps=0, numContainers=0
2026-11-14 19:51:20,280 INFO org.apache.hadoop.yarn.server.resourcemanager.security.RMContainerTokenSecretManager: Rolling master-key for container-tokens
2026-11-14 19:53:44,901 INFO org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.allocator.AbstractContainerAllocator: assignedContainer application attempt=appattempt_1794666080258_0001_000001 container=null queue=org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.allocator.RegularContainerAllocator@3a2c4e7d clusterResource=<memory:16384, vCores:16> type=OFF_SWITCH requestedPartition=
2026-11-14 19:53:44,903 INFO org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.ParentQueue: assignedContainer queue=root usedCapacity=0.0 absoluteUsedCapacity=0.0 used=<memory:0, vCores:0> cluster=<memory:16384, vCores:16>
2026-11-14 19:53:44,905 INFO org.apache.hadoop.yarn.server.resourcemanager.rmcontainer.RMContainerImpl: container_1794666080258_0001_01_000001 Container Transitioned from NEW to ALLOCATED
2026-11-14 19:53:44,906 INFO org.apache.hadoop.yarn.server.resourcemanager.RMAuditLogger: USER=naveen	OPERATION=AM Allocated Container	TARGET=SchedulerApp	RESULT=SUCCESS	APPID=application_1794666080258_0001	CONTAINERID=container_1794666080258_0001_01_000001	RESOURCE=<memory:2048, vCores:1>
2026-11-14 19:53:44,928 INFO org.apache.hadoop.yarn.server.resourcemanager.security.NMTokenSecretManagerInRM: Sending NMToken for nodeId : DHANDEPATIL:39501 for container : container_1794666080258_0001_01_000001
2026-11-14 19:53:44,939 INFO org.apache.hadoop.yarn.server.resourcemanager.rmcontainer.RMContainerImpl: container_1794666080258_0001_01_000001 Container Transitioned from ALLOCATED to ACQUIRED
2026-11-14 19:53:44,940 INFO org.apache.hadoop.yarn.server.resourcemanager.rmapp.attempt.RMAppAttemptImpl: Storing attempt: AppId: application_1794666080258_0001 AttemptId: appattempt_1794666080258_0001_000001 MasterContainer: Container: [ContainerId: container_1794666080258_0001_01_000001, AllocationRequestId: 0, Version: 0, NodeId: DHANDEPATIL:39501, NodeHttpAddress: DHANDEPATIL:8042, Resource: <memory:2048, vCores:1>, Priority: 0, Token: Token { kind: ContainerToken, service: 10.87.234.88:39501 }, ExecutionType: GUARANTEED, ]
2026-11-14 19:53:44,940 INFO org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.ParentQueue: assignedContainer queue=root usedCapacity=0.125 absoluteUsedCapacity=0.125 used=<memory:2048, vCores:1> cluster=<memory:16384, vCores:16>
2026-11-14 19:53:44,955 INFO org.apache.hadoop.yarn.server.resourcemanager.rmapp.attempt.RMAppAttemptImpl: appattempt_1794666080258_0001_000001 State change from SCHEDULED to ALLOCATED_SAVING on event = CONTAINER_ALLOCATED
2026-11-14 19:53:44,964 INFO org.apache.hadoop.yarn.server.resourcemanager.amlauncher.AMLauncher: Launching masterappattempt_1794666080258_0001_000001
2026-11-14 19:53:45,026 INFO org.apache.hadoop.yarn.server.resourcemanager.amlauncher.AMLauncher: Setting up container Container: [ContainerId: container_1794666080258_0001_01_000001, AllocationRequestId: 0, Version: 0, NodeId: DHANDEPATIL:39501, NodeHttpAddress: DHANDEPATIL:8042, Resource: <memory:2048, vCores:1>, Priority: 0, Token: Token { kind: ContainerToken, service: 10.87.234.88:39501 }, ExecutionType: GUARANTEED, ] for AM appattempt_1794666080258_0001_000001
2026-11-14 20:03:08,406 INFO org.apache.hadoop.yarn.server.resourcemanager.amlauncher.AMLauncher: Error launching appattempt_1794666080258_0001_000001. Got exception: org.apache.hadoop.net.ConnectTimeoutException: Call From archlinux/10.87.234.198 to DHANDEPATIL:39501 failed on socket timeout exception: org.apache.hadoop.net.ConnectTimeoutException: 20000 millis timeout while waiting for channel to be ready for connect. ch : java.nio.channels.SocketChannel[connection-pending remote=DHANDEPATIL/10.87.234.88:39501]; For more details see:  http://wiki.apache.org/hadoop/SocketTimeout
	at org.apache.hadoop.net.NetUtils.wrapException(NetUtils.java:774)
	at com.sun.proxy.$Proxy82.startContainers(Unknown Source)
	at org.apache.hadoop.yarn.api.impl.pb.client.ContainerManagementProtocolPBClientImpl.startContainers(ContainerManagementProtocolPBClientImpl.java:128)
	at com.sun.proxy.$Proxy83.startContainers(Unknown Source)
	at org.apache.hadoop.yarn.server.resourcemanager.amlauncher.AMLauncher.launch(AMLauncher.java:122)
	at org.apache.hadoop.yarn.server.resourcemanager.amlauncher.AMLauncher.run(AMLauncher.java:307)
Caused by: org.apache.hadoop.net.ConnectTimeoutException: 20000 millis timeout while waiting for channel to be ready for connect. ch : java.nio.channels.SocketChannel[connection-pending remote=DHANDEPATIL/10.87.234.88:39501]
2026-11-14 20:03:08,409 INFO org.apache.hadoop.yarn.server.resourcemanager.rmapp.attempt.RMAppAttemptImpl: Updating application attempt appattempt_1794666080258_0001_000001 with final state: FAILED, and exit status: -1000
2026-11-14 20:03:08,410 INFO org.apache.hadoop.yarn.server.resourcemanager.rmapp.attempt.RMAppAttemptImpl: appattempt_1794666080258_0001_000001 State change from ALLOCATED to FINAL_SAVING on event = LAUNCH_FAILED
2026-11-14 20:03:08,411 INFO org.apache.hadoop.yarn.server.resourcemanager.rmapp.attempt.RMAppAttemptImpl: appattempt_1794666080258_0001_000001 State change from FINAL_SAVING to FAILED on event = ATTEMPT_UPDATE_SAVED
2026-11-14 20:03:08,411 INFO org.apache.hadoop.yarn.server.resourcemanager.rmapp.RMAppImpl: The number of failed attempts is 1. The max attempts is 2
2026-11-14 20:03:08,412 INFO org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CapacityScheduler: Application Attempt appattempt_1794666080258_0001_000001 is done. finalState=FAILED
2026-11-14 20:03:08,421 INFO org.apache.hadoop.yarn.server.resourcemanager.rmcontainer.RMContainerImpl: container_1794666080258_0001_01_000001 Container Transitioned from ACQUIRED to KILLED
2026-11-14 20:03:08,421 INFO org.apache.hadoop.yarn.server.resourcemanager.RMAuditLogger: USER=naveen	OPERATION=AM Released Container	TARGET=SchedulerApp	RESULT=SUCCESS	APPID=application_1794666080258_0001CONTAINERID=container_1794666080258_0001_01_000001	RESOURCE=<memory:2048, vCores:1>
2026-11-14 20:03:08,432 INFO org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.allocator.AbstractContainerAllocator: assignedContainer application attempt=appattempt_1794666080258_0001_000002 container=null queue=org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.allocator.RegularContainerAllocator@1ed8123b clusterResource=<memory:16384, vCores:16> type=OFF_SWITCH requestedPartition=
2026-11-14 20:03:08,433 INFO org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.ParentQueue: assignedContainer queue=root usedCapacity=0.0 absoluteUsedCapacity=0.0 used=<memory:0, vCores:0> cluster=<memory:16384, vCores:16>
2026-11-14 20:03:08,433 INFO org.apache.hadoop.yarn.server.resourcemanager.rmcontainer.RMContainerImpl: container_1794666080258_0001_02_000001 Container Transitioned from NEW to ALLOCATED
2026-11-14 20:03:08,433 INFO org.apache.hadoop.yarn.server.resourcemanager.RMAuditLogger: USER=naveen	OPERATION=AM Allocated Container	TARGET=SchedulerApp	RESULT=SUCCESS	APPID=application_1794666080258_0001	CONTAINERID=container_1794666080258_0001_02_000001	RESOURCE=<memory:2048, vCores:1>
2026-11-14 20:03:08,434 INFO org.apache.hadoop.yarn.server.resourcemanager.security.NMTokenSecretManagerInRM: Sending NMToken for nodeId : DHANDEPATIL:39501 for container : container_1794666080258_0001_02_000001
2026-11-14 20:03:08,435 INFO org.apache.hadoop.yarn.server.resourcemanager.rmcontainer.RMContainerImpl: container_1794666080258_0001_02_000001 Container Transitioned from ALLOCATED to ACQUIRED
2026-11-14 20:03:08,435 INFO org.apache.hadoop.yarn.server.resourcemanager.rmapp.attempt.RMAppAttemptImpl: Storing attempt: AppId: application_1794666080258_0001 AttemptId: appattempt_1794666080258_0001_000002 MasterContainer: Container: [ContainerId: container_1794666080258_0001_02_000001, AllocationRequestId: 0, Version: 0, NodeId: DHANDEPATIL:39501, NodeHttpAddress: DHANDEPATIL:8042, Resource: <memory:2048, vCores:1>, Priority: 0, Token: Token { kind: ContainerToken, service: 10.87.234.88:39501 }, ExecutionType: GUARANTEED, ]
2026-11-14 20:03:08,435 INFO org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.ParentQueue: assignedContainer queue=root usedCapacity=0.125 absoluteUsedCapacity=0.125 used=<memory:2048, vCores:1> cluster=<memory:16384, vCores:16>
2026-11-14 20:03:08,435 INFO org.apache.hadoop.yarn.server.resourcemanager.rmapp.attempt.RMAppAttemptImpl: appattempt_1794666080258_0001_000002 State change from SCHEDULED to ALLOCATED_SAVING on event = CONTAINER_ALLOCATED
2026-11-14 20:03:08,436 INFO org.apache.hadoop.yarn.server.resourcemanager.amlauncher.AMLauncher: Launching masterappattempt_1794666080258_0001_000002
2026-11-14 20:03:08,437 INFO org.apache.hadoop.yarn.server.resourcemanager.amlauncher.AMLauncher: Setting up container Container: [ContainerId: container_1794666080258_0001_02_000001, AllocationRequestId: 0, Version: 0, NodeId: DHANDEPATIL:39501, NodeHttpAddress: DHANDEPATIL:8042, Resource: <memory:2048, vCores:1>, Priority: 0, Token: Token { kind: ContainerToken, service: 10.87.234.88:39501 }, ExecutionType: GUARANTEED, ] for AM appattempt_1794666080258_0001_000002
[naveen@archlinux ~]$ yarn applicationattempt -status appattempt_1794666080258_0001_000002
26/11/14 20:07:25 INFO client.RMProxy: Connecting to ResourceManager at archlinux/10.87.234.198:8032
Application Attempt Report : 
	ApplicationAttempt-Id : appattempt_1794666080258_0001_000002
	State : ALLOCATED
	AMContainer : container_1794666080258_0001_02_000001
	Tracking-URL : http://archlinux:8088/proxy/application_1794666080258_0001/
	RPC Port : -1
	AM Host : N/A
	Diagnostics : [Sat Nov 14 20:03:08 +0530 2026] Scheduler has assigned a container for AM, waiting for AM container to be launched
[naveen@archlinux ~]$ ssh DHANDEPATIL 'sudo ss -lntp | grep 39501'
sudo: a terminal is required to read the password; either use ssh's -t option or configure an askpass helper
sudo: a password is required
[naveen@archlinux ~]$ ssh DHANDEPATIL 'sudo ufw status numbered'
sudo: a terminal is required to read the password; either use ssh's -t option or configure an askpass helper
sudo: a password is required
[naveen@archlinux ~]$ nc -vz -w 5 10.87.234.88 39501
nc: connect to 10.87.234.88 port 39501 (tcp) timed out: Operation now in progress
[naveen@archlinux ~]$ sudo ufw status numbered
[sudo] password for naveen: 
Status: active

     To                         Action      From
     --                         ------      ----
[ 1] 22/tcp                     ALLOW IN    172.31.76.25              
[ 2] 22/tcp                     ALLOW IN    172.31.111.173            
[ 3] 22/tcp                     ALLOW IN    10.87.234.88              
[ 4] 9000/tcp                   ALLOW IN    10.87.234.88              
[ 5] 50070/tcp                  ALLOW IN    10.87.234.88              
[ 6] 50010/tcp                  ALLOW IN    10.87.234.88              
[ 7] 50020/tcp                  ALLOW IN    10.87.234.88              
[ 8] 50075/tcp                  ALLOW IN    10.87.234.88              
[ 9] 8030:8033/tcp              ALLOW IN    10.87.234.88              
[10] 8040:8042/tcp              ALLOW IN    10.87.234.88              
[11] 8088/tcp                   ALLOW IN    10.87.234.88              
[12] 13562/tcp                  ALLOW IN    10.87.234.88              

[naveen@archlinux ~]$ sudo ss -lntp | grep 39501
[naveen@archlinux ~]$ sudo ufw status numbered
Status: active

     To                         Action      From
     --                         ------      ----
[ 1] 22/tcp                     ALLOW IN    172.31.76.25              
[ 2] 22/tcp                     ALLOW IN    172.31.111.173            
[ 3] 22/tcp                     ALLOW IN    10.87.234.88              
[ 4] 9000/tcp                   ALLOW IN    10.87.234.88              
[ 5] 50070/tcp                  ALLOW IN    10.87.234.88              
[ 6] 50010/tcp                  ALLOW IN    10.87.234.88              
[ 7] 50020/tcp                  ALLOW IN    10.87.234.88              
[ 8] 50075/tcp                  ALLOW IN    10.87.234.88              
[ 9] 8030:8033/tcp              ALLOW IN    10.87.234.88              
[10] 8040:8042/tcp              ALLOW IN    10.87.234.88              
[11] 8088/tcp                   ALLOW IN    10.87.234.88              
[12] 13562/tcp                  ALLOW IN    10.87.234.88              

[naveen@archlinux ~]$ nc -vz -w 5 10.87.234.88 39501
Connection to 10.87.234.88 39501 port [tcp/*] succeeded!
[naveen@archlinux ~]$ nc -vz -w 5 10.87.234.88 39501
Connection to 10.87.234.88 39501 port [tcp/*] succeeded!
[naveen@archlinux ~]$ yarn application -list -appStates ALL
26/11/14 20:16:55 INFO client.RMProxy: Connecting to ResourceManager at archlinux/10.87.234.198:8032
Total number of applications (application-types: [], states: [NEW, NEW_SAVING, SUBMITTED, ACCEPTED, RUNNING, FINISHED, FAILED, KILLED] and tags: []):1
                Application-Id	    Application-Name	    Application-Type	      User	     Queue	             State	       Final-State	       Progress	                       Tracking-URL
application_1794666080258_0001	          word count	           MAPREDUCE	    naveen	   default	            FAILED	            FAILED	             0%	http://archlinux:8088/cluster/app/application_1794666080258_0001
[naveen@archlinux ~]$ yarn application -kill application_1794666080258_0001
26/11/14 20:17:00 INFO client.RMProxy: Connecting to ResourceManager at archlinux/10.87.234.198:8032
Application application_1794666080258_0001 has already finished 
[naveen@archlinux ~]$ yarn node -list
26/11/14 20:17:06 INFO client.RMProxy: Connecting to ResourceManager at archlinux/10.87.234.198:8032
Total Nodes:2
         Node-Id	     Node-State	Node-Http-Address	Number-of-Running-Containers
 archlinux:40585	        RUNNING	   archlinux:8042	                           0
DHANDEPATIL:39501	        RUNNING	 DHANDEPATIL:8042	                           0
[naveen@archlinux ~]$ hdfs dfs -rm -r -f /test/output
[naveen@archlinux ~]$ hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.9.1.jar \
wordcount /test/input /test/output
26/11/14 20:17:21 INFO client.RMProxy: Connecting to ResourceManager at archlinux/10.87.234.198:8032
26/11/14 20:17:23 INFO input.FileInputFormat: Total input files to process : 1
26/11/14 20:17:23 INFO mapreduce.JobSubmitter: number of splits:1
26/11/14 20:17:23 INFO Configuration.deprecation: yarn.resourcemanager.system-metrics-publisher.enabled is deprecated. Instead, use yarn.system-metrics-publisher.enabled
26/11/14 20:17:24 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1794666080258_0002
26/11/14 20:17:24 INFO impl.YarnClientImpl: Submitted application application_1794666080258_0002
26/11/14 20:17:24 INFO mapreduce.Job: The url to track the job: http://archlinux:8088/proxy/application_1794666080258_0002/
26/11/14 20:17:24 INFO mapreduce.Job: Running job: job_1794666080258_0002
26/11/14 20:17:29 INFO mapreduce.Job: Job job_1794666080258_0002 running in uber mode : false
26/11/14 20:17:29 INFO mapreduce.Job:  map 0% reduce 0%
26/11/14 20:17:33 INFO mapreduce.Job:  map 100% reduce 0%
26/11/14 20:17:38 INFO mapreduce.Job:  map 100% reduce 100%
26/11/14 20:17:39 INFO mapreduce.Job: Job job_1794666080258_0002 completed successfully
26/11/14 20:17:39 INFO mapreduce.Job: Counters: 49
	File System Counters
		FILE: Number of bytes read=139
		FILE: Number of bytes written=395669
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=198
		HDFS: Number of bytes written=93
		HDFS: Number of read operations=6
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
	Job Counters 
		Launched map tasks=1
		Launched reduce tasks=1
		Data-local map tasks=1
		Total time spent by all maps in occupied slots (ms)=1685
		Total time spent by all reduces in occupied slots (ms)=2410
		Total time spent by all map tasks (ms)=1685
		Total time spent by all reduce tasks (ms)=2410
		Total vcore-milliseconds taken by all map tasks=1685
		Total vcore-milliseconds taken by all reduce tasks=2410
		Total megabyte-milliseconds taken by all map tasks=1725440
		Total megabyte-milliseconds taken by all reduce tasks=2467840
	Map-Reduce Framework
		Map input records=2
		Map output records=13
		Map output bytes=143
		Map output materialized bytes=139
		Input split bytes=107
		Combine input records=13
		Combine output records=10
		Reduce input groups=10
		Reduce shuffle bytes=139
		Reduce input records=10
		Reduce output records=10
		Spilled Records=20
		Shuffled Maps =1
		Failed Shuffles=0
		Merged Map outputs=1
		GC time elapsed (ms)=87
		CPU time spent (ms)=870
		Physical memory (bytes) snapshot=536797184
		Virtual memory (bytes) snapshot=3933184000
		Total committed heap usage (bytes)=346030080
	Shuffle Errors
		BAD_ID=0
		CONNECTION=0
		IO_ERROR=0
		WRONG_LENGTH=0
		WRONG_MAP=0
		WRONG_REDUCE=0
	File Input Format Counters 
		Bytes Read=91
	File Output Format Counters 
		Bytes Written=93
[naveen@archlinux ~]$ hdfs dfs -cat /test/output/part-r-00000
and	1
data	2
detection	1
hadoop	2
intrusion	1
network	1
processes	1
spark	2
stores	1
using	1
[naveen@archlinux ~]$ hdfs fsck /test/output -files -blocks -locations
Connecting to namenode via http://archlinux:50070/fsck?ugi=naveen&files=1&blocks=1&locations=1&path=%2Ftest%2Foutput
FSCK started by naveen (auth:SIMPLE) from /10.87.234.198 for path /test/output at Sat Nov 14 20:18:07 IST 2026
/test/output <dir>
/test/output/_SUCCESS 0 bytes, 0 block(s):  OK

/test/output/part-r-00000 93 bytes, 1 block(s):  OK
0. BP-1383357140-10.87.234.198-1794416650190:blk_1073741837_1013 len=93 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]

Status: HEALTHY
 Total size:	93 B
 Total dirs:	1
 Total files:	2
 Total symlinks:		0
 Total blocks (validated):	1 (avg. block size 93 B)
 Minimally replicated blocks:	1 (100.0 %)
 Over-replicated blocks:	0 (0.0 %)
 Under-replicated blocks:	0 (0.0 %)
 Mis-replicated blocks:		0 (0.0 %)
 Default replication factor:	2
 Average block replication:	2.0
 Corrupt blocks:		0
 Missing replicas:		0 (0.0 %)
 Number of data-nodes:		2
 Number of racks:		1
FSCK ended at Sat Nov 14 20:18:07 IST 2026 in 3 milliseconds


The filesystem under path '/test/output' is HEALTHY
[naveen@archlinux ~]$ ls -lh ~/Downloads/
total 368M
-rw-r--r-- 1 naveen naveen 141M Nov 11 01:15 google-chrome-stable_current_amd64.deb
-rw-r--r-- 1 naveen naveen 225M Nov 14 19:05 MachineLearningCSV.zip
-rw-r--r-- 1 naveen naveen 2.7M Nov 14 20:12 s10922-024-09874-0.pdf
[naveen@archlinux ~]$ ls -lh ~/Downloads/MachineLearningCSV.zip
-rw-r--r-- 1 naveen naveen 225M Nov 14 19:05 /home/naveen/Downloads/MachineLearningCSV.zip
[naveen@archlinux ~]$ mkdir -p ~/NIDS/dataset
mkdir -p ~/NIDS/src
mkdir -p ~/NIDS/models
mkdir -p ~/NIDS/results
[naveen@archlinux ~]$ unzip -o ~/Downloads/MachineLearningCSV.zip -d ~/NIDS/dataset/
Archive:  /home/naveen/Downloads/MachineLearningCSV.zip
   creating: /home/naveen/NIDS/dataset/MachineLearningCVE/
  inflating: /home/naveen/NIDS/dataset/MachineLearningCVE/Wednesday-workingHours.pcap_ISCX.csv  
  inflating: /home/naveen/NIDS/dataset/MachineLearningCVE/Tuesday-WorkingHours.pcap_ISCX.csv  
  inflating: /home/naveen/NIDS/dataset/MachineLearningCVE/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv  
  inflating: /home/naveen/NIDS/dataset/MachineLearningCVE/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv  
  inflating: /home/naveen/NIDS/dataset/MachineLearningCVE/Monday-WorkingHours.pcap_ISCX.csv  
  inflating: /home/naveen/NIDS/dataset/MachineLearningCVE/Friday-WorkingHours-Morning.pcap_ISCX.csv  
  inflating: /home/naveen/NIDS/dataset/MachineLearningCVE/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv  
  inflating: /home/naveen/NIDS/dataset/MachineLearningCVE/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv  
[naveen@archlinux ~]$ sudo pacman -S unzip
warning: unzip-6.0-23 is up to date -- reinstalling
resolving dependencies...
looking for conflicting packages...

Packages (1) unzip-6.0-23

Total Installed Size:  0.30 MiB
Net Upgrade Size:      0.00 MiB

:: Proceed with installation? [Y/n] y
(1/1) checking keys in keyring                                                                                                  [#############################################################################] 100%
(1/1) checking package integrity                                                                                                [#############################################################################] 100%
(1/1) loading package files                                                                                                     [#############################################################################] 100%
(1/1) checking for file conflicts                                                                                               [#############################################################################] 100%
(1/1) checking available disk space                                                                                             [#############################################################################] 100%
:: Processing package changes...
(1/1) reinstalling unzip                                                                                                        [#############################################################################] 100%
:: Running post-transaction hooks...
(1/1) Arming ConditionNeedsUpdate...
[naveen@archlinux ~]$ find ~/NIDS/dataset -type f -iname "*.csv"
/home/naveen/NIDS/dataset/MachineLearningCVE/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
/home/naveen/NIDS/dataset/MachineLearningCVE/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
/home/naveen/NIDS/dataset/MachineLearningCVE/Wednesday-workingHours.pcap_ISCX.csv
/home/naveen/NIDS/dataset/MachineLearningCVE/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
/home/naveen/NIDS/dataset/MachineLearningCVE/Monday-WorkingHours.pcap_ISCX.csv
/home/naveen/NIDS/dataset/MachineLearningCVE/Tuesday-WorkingHours.pcap_ISCX.csv
/home/naveen/NIDS/dataset/MachineLearningCVE/Friday-WorkingHours-Morning.pcap_ISCX.csv
/home/naveen/NIDS/dataset/MachineLearningCVE/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
[naveen@archlinux ~]$ du -sh ~/NIDS/dataset/
844M	/home/naveen/NIDS/dataset/
[naveen@archlinux ~]$ find ~/NIDS/dataset -type f -iname "*.csv" | wc -l
8
[naveen@archlinux ~]$ hdfs dfs -mkdir -p /nids/raw/cicids2017
hdfs dfs -mkdir -p /nids/processed
hdfs dfs -mkdir -p /nids/models
hdfs dfs -mkdir -p /nids/results
[naveen@archlinux ~]$ hdfs dfs -ls -R /nids
drwxr-xr-x   - naveen supergroup          0 2026-11-14 20:20 /nids/models
drwxr-xr-x   - naveen supergroup          0 2026-11-14 20:20 /nids/processed
drwxr-xr-x   - naveen supergroup          0 2026-11-14 20:20 /nids/raw
drwxr-xr-x   - naveen supergroup          0 2026-11-14 20:20 /nids/raw/cicids2017
drwxr-xr-x   - naveen supergroup          0 2026-11-14 20:20 /nids/results
[naveen@archlinux ~]$ find ~/NIDS/dataset -type f -iname "*.csv" -print0 |
while IFS= read -r -d '' file; do
    echo "Uploading: $file"
    hdfs dfs -put -f "$file" /nids/raw/cicids2017/
done
Uploading: /home/naveen/NIDS/dataset/MachineLearningCVE/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
Uploading: /home/naveen/NIDS/dataset/MachineLearningCVE/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
Uploading: /home/naveen/NIDS/dataset/MachineLearningCVE/Wednesday-workingHours.pcap_ISCX.csv
Uploading: /home/naveen/NIDS/dataset/MachineLearningCVE/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
Uploading: /home/naveen/NIDS/dataset/MachineLearningCVE/Monday-WorkingHours.pcap_ISCX.csv
Uploading: /home/naveen/NIDS/dataset/MachineLearningCVE/Tuesday-WorkingHours.pcap_ISCX.csv
Uploading: /home/naveen/NIDS/dataset/MachineLearningCVE/Friday-WorkingHours-Morning.pcap_ISCX.csv
Uploading: /home/naveen/NIDS/dataset/MachineLearningCVE/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
[naveen@archlinux ~]$ hdfs dfs -ls -h /nids/raw/cicids2017/
Found 8 items
-rw-r--r--   2 naveen supergroup     73.6 M 2026-11-14 20:21 /nids/raw/cicids2017/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
-rw-r--r--   2 naveen supergroup     73.3 M 2026-11-14 20:23 /nids/raw/cicids2017/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
-rw-r--r--   2 naveen supergroup     55.6 M 2026-11-14 20:25 /nids/raw/cicids2017/Friday-WorkingHours-Morning.pcap_ISCX.csv
-rw-r--r--   2 naveen supergroup    168.7 M 2026-11-14 20:24 /nids/raw/cicids2017/Monday-WorkingHours.pcap_ISCX.csv
-rw-r--r--   2 naveen supergroup     79.3 M 2026-11-14 20:26 /nids/raw/cicids2017/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
-rw-r--r--   2 naveen supergroup     49.6 M 2026-11-14 20:21 /nids/raw/cicids2017/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
-rw-r--r--   2 naveen supergroup    128.8 M 2026-11-14 20:25 /nids/raw/cicids2017/Tuesday-WorkingHours.pcap_ISCX.csv
-rw-r--r--   2 naveen supergroup    214.7 M 2026-11-14 20:22 /nids/raw/cicids2017/Wednesday-workingHours.pcap_ISCX.csv
[naveen@archlinux ~]$ hdfs dfs -du -h /nids/raw/cicids2017/
73.6 M   /nids/raw/cicids2017/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
73.3 M   /nids/raw/cicids2017/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
55.6 M   /nids/raw/cicids2017/Friday-WorkingHours-Morning.pcap_ISCX.csv
168.7 M  /nids/raw/cicids2017/Monday-WorkingHours.pcap_ISCX.csv
79.3 M   /nids/raw/cicids2017/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
49.6 M   /nids/raw/cicids2017/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
128.8 M  /nids/raw/cicids2017/Tuesday-WorkingHours.pcap_ISCX.csv
214.7 M  /nids/raw/cicids2017/Wednesday-workingHours.pcap_ISCX.csv
[naveen@archlinux ~]$ hdfs dfs -ls /nids/raw/cicids2017/ | grep -c '\.csv$'
8
[naveen@archlinux ~]$ hdfs fsck /nids/raw/cicids2017 -files -blocks -locations
Connecting to namenode via http://archlinux:50070/fsck?ugi=naveen&files=1&blocks=1&locations=1&path=%2Fnids%2Fraw%2Fcicids2017
FSCK started by naveen (auth:SIMPLE) from /10.87.234.198 for path /nids/raw/cicids2017 at Sat Nov 14 20:26:31 IST 2026
/nids/raw/cicids2017 <dir>
/nids/raw/cicids2017/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv 77123859 bytes, 1 block(s):  OK
0. BP-1383357140-10.87.234.198-1794416650190:blk_1073741841_1017 len=77123859 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]

/nids/raw/cicids2017/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv 76906168 bytes, 1 block(s):  OK
0. BP-1383357140-10.87.234.198-1794416650190:blk_1073741845_1021 len=76906168 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]

/nids/raw/cicids2017/Friday-WorkingHours-Morning.pcap_ISCX.csv 58316725 bytes, 1 block(s):  OK
0. BP-1383357140-10.87.234.198-1794416650190:blk_1073741850_1026 len=58316725 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]

/nids/raw/cicids2017/Monday-WorkingHours.pcap_ISCX.csv 176927918 bytes, 2 block(s):  OK
0. BP-1383357140-10.87.234.198-1794416650190:blk_1073741846_1022 len=134217728 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]
1. BP-1383357140-10.87.234.198-1794416650190:blk_1073741847_1023 len=42710190 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]

/nids/raw/cicids2017/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv 83102436 bytes, 1 block(s):  OK
0. BP-1383357140-10.87.234.198-1794416650190:blk_1073741851_1027 len=83102436 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]

/nids/raw/cicids2017/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv 52023263 bytes, 1 block(s):  OK
0. BP-1383357140-10.87.234.198-1794416650190:blk_1073741842_1018 len=52023263 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]

/nids/raw/cicids2017/Tuesday-WorkingHours.pcap_ISCX.csv 135078995 bytes, 2 block(s):  OK
0. BP-1383357140-10.87.234.198-1794416650190:blk_1073741848_1024 len=134217728 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]
1. BP-1383357140-10.87.234.198-1794416650190:blk_1073741849_1025 len=861267 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]

/nids/raw/cicids2017/Wednesday-workingHours.pcap_ISCX.csv 225166395 bytes, 2 block(s):  OK
0. BP-1383357140-10.87.234.198-1794416650190:blk_1073741843_1019 len=134217728 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]
1. BP-1383357140-10.87.234.198-1794416650190:blk_1073741844_1020 len=90948667 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]

Status: HEALTHY
 Total size:	884645759 B
 Total dirs:	1
 Total files:	8
 Total symlinks:		0
 Total blocks (validated):	11 (avg. block size 80422341 B)
 Minimally replicated blocks:	11 (100.0 %)
 Over-replicated blocks:	0 (0.0 %)
 Under-replicated blocks:	0 (0.0 %)
 Mis-replicated blocks:		0 (0.0 %)
 Default replication factor:	2
 Average block replication:	2.0
 Corrupt blocks:		0
 Missing replicas:		0 (0.0 %)
 Number of data-nodes:		2
 Number of racks:		1
FSCK ended at Sat Nov 14 20:26:31 IST 2026 in 3 milliseconds


The filesystem under path '/nids/raw/cicids2017' is HEALTHY
[naveen@archlinux ~]$ hdfs dfs -ls /nids/raw/cicids2017/ | grep -c '\.csv$'
8
[naveen@archlinux ~]$ hdfs fsck /nids/raw/cicids2017 -files -blocks -locations
Connecting to namenode via http://archlinux:50070/fsck?ugi=naveen&files=1&blocks=1&locations=1&path=%2Fnids%2Fraw%2Fcicids2017
FSCK started by naveen (auth:SIMPLE) from /10.87.234.198 for path /nids/raw/cicids2017 at Sat Nov 14 20:32:20 IST 2026
/nids/raw/cicids2017 <dir>
/nids/raw/cicids2017/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv 77123859 bytes, 1 block(s):  OK
0. BP-1383357140-10.87.234.198-1794416650190:blk_1073741841_1017 len=77123859 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]

/nids/raw/cicids2017/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv 76906168 bytes, 1 block(s):  OK
0. BP-1383357140-10.87.234.198-1794416650190:blk_1073741845_1021 len=76906168 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]

/nids/raw/cicids2017/Friday-WorkingHours-Morning.pcap_ISCX.csv 58316725 bytes, 1 block(s):  OK
0. BP-1383357140-10.87.234.198-1794416650190:blk_1073741850_1026 len=58316725 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]

/nids/raw/cicids2017/Monday-WorkingHours.pcap_ISCX.csv 176927918 bytes, 2 block(s):  OK
0. BP-1383357140-10.87.234.198-1794416650190:blk_1073741846_1022 len=134217728 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]
1. BP-1383357140-10.87.234.198-1794416650190:blk_1073741847_1023 len=42710190 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]

/nids/raw/cicids2017/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv 83102436 bytes, 1 block(s):  OK
0. BP-1383357140-10.87.234.198-1794416650190:blk_1073741851_1027 len=83102436 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]

/nids/raw/cicids2017/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv 52023263 bytes, 1 block(s):  OK
0. BP-1383357140-10.87.234.198-1794416650190:blk_1073741842_1018 len=52023263 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]

/nids/raw/cicids2017/Tuesday-WorkingHours.pcap_ISCX.csv 135078995 bytes, 2 block(s):  OK
0. BP-1383357140-10.87.234.198-1794416650190:blk_1073741848_1024 len=134217728 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]
1. BP-1383357140-10.87.234.198-1794416650190:blk_1073741849_1025 len=861267 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]

/nids/raw/cicids2017/Wednesday-workingHours.pcap_ISCX.csv 225166395 bytes, 2 block(s):  OK
0. BP-1383357140-10.87.234.198-1794416650190:blk_1073741843_1019 len=134217728 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]
1. BP-1383357140-10.87.234.198-1794416650190:blk_1073741844_1020 len=90948667 Live_repl=2 [DatanodeInfoWithStorage[10.87.234.88:50010,DS-7cfb5b72-16de-4645-a464-775d2721e3a9,DISK], DatanodeInfoWithStorage[10.87.234.198:50010,DS-bbdbb2ad-d18e-4fd0-800b-4f1ab667bebf,DISK]]

Status: HEALTHY
 Total size:	884645759 B
 Total dirs:	1
 Total files:	8
 Total symlinks:		0
 Total blocks (validated):	11 (avg. block size 80422341 B)
 Minimally replicated blocks:	11 (100.0 %)
 Over-replicated blocks:	0 (0.0 %)
 Under-replicated blocks:	0 (0.0 %)
 Mis-replicated blocks:		0 (0.0 %)
 Default replication factor:	2
 Average block replication:	2.0
 Corrupt blocks:		0
 Missing replicas:		0 (0.0 %)
 Number of data-nodes:		2
 Number of racks:		1
FSCK ended at Sat Nov 14 20:32:20 IST 2026 in 2 milliseconds


The filesystem under path '/nids/raw/cicids2017' is HEALTHY
[naveen@archlinux ~]$ java -version
python --version
java version "1.8.0_45"
Java(TM) SE Runtime Environment (build 1.8.0_45-b14)
Java HotSpot(TM) 64-Bit Server VM (build 25.45-b02, mixed mode)
Python 3.14.10
[naveen@archlinux ~]$ which conda
conda --version
pacman -Ss jdk17-openjdk
which: no conda in (/opt/hadoop-2.9.1/bin:/opt/hadoop-2.9.1/sbin:/home/naveen/hadoop-2.9.1/bin:/home/naveen/hadoop-2.9.1/sbin:/home/naveen/jdk-8u45-linux-x64/jdk1.8.0_45/bin:/home/naveen/hadoop-2.9.1/bin:/home/naveen/hadoop-2.9.1/sbin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/lib/jvm/default/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl)
bash: conda: command not found
extra/jdk17-openjdk 17.0.21.0.3.u1-1
    OpenJDK Java 17 development kit
[naveen@archlinux ~]$ ^C
[naveen@archlinux ~]$ sudo pacman -S jdk17-openjdk
[sudo] password for naveen: 
resolving dependencies...
looking for conflicting packages...

Packages (1) jdk17-openjdk-17.0.21.0.3.u1-1

Total Download Size:   275.84 MiB
Total Installed Size:  424.30 MiB

:: Proceed with installation? [Y/n] y
:: Retrieving packages...
 jdk17-openjdk-17.0.21.0.3.u1-1-x86_64                                                              275.8 MiB  6.81 MiB/s 00:40 [#############################################################################] 100%
(1/1) checking keys in keyring                                                                                                  [#############################################################################] 100%
(1/1) checking package integrity                                                                                                [#############################################################################] 100%
(1/1) loading package files                                                                                                     [#############################################################################] 100%
(1/1) checking for file conflicts                                                                                               [#############################################################################] 100%
(1/1) checking available disk space                                                                                             [#############################################################################] 100%
:: Processing package changes...
(1/1) installing jdk17-openjdk                                                                                                  [#############################################################################] 100%
Default Java environment is already set to 'java-8-openjdk'
See 'archlinux-java help' to change it
Optional dependencies for jdk17-openjdk
    java-rhino: for some JavaScript support
    alsa-lib: for basic sound support [installed]
    gtk3: for the Gtk+ 3 look and feel - desktop usage [installed]
:: Running post-transaction hooks...
(1/3) Arming ConditionNeedsUpdate...
(2/3) Updating icon theme caches...
(3/3) Updating the desktop file MIME type cache...
[naveen@archlinux ~]$ which conda
conda info --base
conda env list
which: no conda in (/opt/hadoop-2.9.1/bin:/opt/hadoop-2.9.1/sbin:/home/naveen/hadoop-2.9.1/bin:/home/naveen/hadoop-2.9.1/sbin:/home/naveen/jdk-8u45-linux-x64/jdk1.8.0_45/bin:/home/naveen/hadoop-2.9.1/bin:/home/naveen/hadoop-2.9.1/sbin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/lib/jvm/default/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl)
bash: conda: command not found
bash: conda: command not found
[naveen@archlinux ~]$ sudo pacman -S jdk17-openjdk
warning: jdk17-openjdk-17.0.21.0.3.u1-1 is up to date -- reinstalling
resolving dependencies...
looking for conflicting packages...

Packages (1) jdk17-openjdk-17.0.21.0.3.u1-1

Total Installed Size:  424.30 MiB
Net Upgrade Size:        0.00 MiB

:: Proceed with installation? [Y/n] y
(1/1) checking keys in keyring                                                                                                  [#############################################################################] 100%
(1/1) checking package integrity                                                                                                [#############################################################################] 100%
(1/1) loading package files                                                                                                     [#############################################################################] 100%
(1/1) checking for file conflicts                                                                                               [#############################################################################] 100%
(1/1) checking available disk space                                                                                             [#############################################################################] 100%
:: Processing package changes...
(1/1) reinstalling jdk17-openjdk                                                                                                [#############################################################################] 100%
:: Running post-transaction hooks...
(1/3) Arming ConditionNeedsUpdate...
(2/3) Updating icon theme caches...
(3/3) Updating the desktop file MIME type cache...
[naveen@archlinux ~]$ /usr/lib/jvm/java-17-openjdk/bin/java -version
openjdk version "17.0.21.0.3" 2026-10-24
OpenJDK Runtime Environment (build 17.0.21.0.3+1)
OpenJDK 64-Bit Server VM (build 17.0.21.0.3+1, mixed mode, sharing)
[naveen@archlinux ~]$ which conda
which: no conda in (/opt/hadoop-2.9.1/bin:/opt/hadoop-2.9.1/sbin:/home/naveen/hadoop-2.9.1/bin:/home/naveen/hadoop-2.9.1/sbin:/home/naveen/jdk-8u45-linux-x64/jdk1.8.0_45/bin:/home/naveen/hadoop-2.9.1/bin:/home/naveen/hadoop-2.9.1/sbin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/lib/jvm/default/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl)
[naveen@archlinux ~]$ sudo pacman -S uv
resolving dependencies...
looking for conflicting packages...

Packages (2) jemalloc-1:5.4.0-1  uv-0.13.7-1

Total Download Size:   12.63 MiB
Total Installed Size:  47.13 MiB

:: Proceed with installation? [Y/n] y
:: Retrieving packages...
 jemalloc-1:5.4.0-1-x86_64                                                                          305.5 KiB   649 KiB/s 00:00 [#############################################################################] 100%
 uv-0.13.7-1-x86_64                                                                                  12.3 MiB  3.18 MiB/s 00:04 [#############################################################################] 100%
 Total (2/2)                                                                                         12.6 MiB  3.17 MiB/s 00:04 [#############################################################################] 100%
(2/2) checking keys in keyring                                                                                                  [#############################################################################] 100%
(2/2) checking package integrity                                                                                                [#############################################################################] 100%
(2/2) loading package files                                                                                                     [#############################################################################] 100%
(2/2) checking for file conflicts                                                                                               [#############################################################################] 100%
(2/2) checking available disk space                                                                                             [#############################################################################] 100%
:: Processing package changes...
(1/2) installing jemalloc                                                                                                       [#############################################################################] 100%
Optional dependencies for jemalloc
    perl: for jeprof [installed]
(2/2) installing uv                                                                                                             [#############################################################################] 100%
:: Running post-transaction hooks...
(1/1) Arming ConditionNeedsUpdate...
[naveen@archlinux ~]$ uv python install 3.11
Installed Python 3.11.18 in 23.04s
 + cpython-3.11.18-linux-x86_64-gnu (python3.11)
warning: `/home/naveen/.local/bin` is not on your PATH. To use installed Python executables, run `export PATH="/home/naveen/.local/bin:$PATH"` or `uv python update-shell`.
[naveen@archlinux ~]$ mkdir -p ~/NIDS
uv venv --python 3.11 ~/NIDS/venv
Using CPython 3.11.18
Creating virtual environment at: NIDS/venv
Activate with: source NIDS/venv/bin/activate
[naveen@archlinux ~]$ source ~/NIDS/venv/bin/activate
(venv) [naveen@archlinux ~]$ python --version
which python
Python 3.11.18
/home/naveen/NIDS/venv/bin/python
(venv) [naveen@archlinux ~]$ source ~/NIDS/venv/bin/activate
(venv) [naveen@archlinux ~]$ export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export PATH="$JAVA_HOME/bin:$PATH"
(venv) [naveen@archlinux ~]$ cd ~/Downloads

wget https://archive.apache.org/dist/spark/spark-3.5.9/spark-3.5.9-bin-hadoop3.tgz
--2026-11-14 20:40:16--  https://archive.apache.org/dist/spark/spark-3.5.9/spark-3.5.9-bin-hadoop3.tgz
Loaded CA certificate '/etc/ssl/certs/ca-certificates.crt'
Resolving archive.apache.org (archive.apache.org)... 2a01:4f9:1a:a084::2, 65.108.204.189
Connecting to archive.apache.org (archive.apache.org)|2a01:4f9:1a:a084::2|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 401379923 (383M) [application/x-gzip]
Saving to: ‘spark-3.5.9-bin-hadoop3.tgz’

spark-3.5.9-bin-hadoop3.tgz                          100%[======================================================================================================================>] 382.79M  2.86MB/s    in 85s     

2026-11-14 20:41:42 (4.48 MB/s) - ‘spark-3.5.9-bin-hadoop3.tgz’ saved [401379923/401379923]

(venv) [naveen@archlinux Downloads]$ tar -xzf spark-3.5.9-bin-hadoop3.tgz -C ~/NIDS/
(venv) [naveen@archlinux Downloads]$ export SPARK_HOME=$HOME/NIDS/spark-3.5.9-bin-hadoop3
export PATH=$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH
(venv) [naveen@archlinux Downloads]$ spark-submit --version
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.5.9
      /_/
                        
Using Scala version 2.12.18, OpenJDK 64-Bit Server VM, 17.0.21.0.3
Branch HEAD
Compiled by user holden on 2026-07-12T18:40:50Z
Revision 7c14a3c28b141cc97a330c4d0f5d2a6da7267f85
Url https://github.com/apache/spark
Type --help for more information.
(venv) [naveen@archlinux Downloads]$ echo "$HADOOP_HOME"
echo "$HADOOP_CONF_DIR"

ls $HADOOP_CONF_DIR/core-site.xml
ls $HADOOP_CONF_DIR/hdfs-site.xml
/opt/hadoop-2.9.1
/opt/hadoop-2.9.1/etc/hadoop
/opt/hadoop-2.9.1/etc/hadoop/core-site.xml
/opt/hadoop-2.9.1/etc/hadoop/hdfs-site.xml
(venv) [naveen@archlinux Downloads]$ source ~/NIDS/venv/bin/activate

export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export SPARK_HOME=$HOME/NIDS/spark-3.5.9-bin-hadoop3
export HADOOP_HOME=/opt/hadoop-2.9.1
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export SPARK_MASTER_HOST=10.87.234.198
export SPARK_MASTER_PORT=7077
export SPARK_MASTER_WEBUI_PORT=8080

export PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH
(venv) [naveen@archlinux Downloads]$ mkdir -p $SPARK_HOME/conf

cp $SPARK_HOME/conf/spark-env.sh.template \
   $SPARK_HOME/conf/spark-env.sh
(venv) [naveen@archlinux Downloads]$ cat >> $SPARK_HOME/conf/spark-env.sh <<'EOF'

export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export SPARK_MASTER_HOST=10.87.234.198
export SPARK_MASTER_PORT=7077
export SPARK_MASTER_WEBUI_PORT=8080
export SPARK_WORKER_PORT=7078
export SPARK_WORKER_WEBUI_PORT=8081
EOF
(venv) [naveen@archlinux Downloads]$ hdfs dfs -ls /nids/raw/cicids2017/
Found 8 items
-rw-r--r--   2 naveen supergroup   77123859 2026-11-14 20:21 /nids/raw/cicids2017/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
-rw-r--r--   2 naveen supergroup   76906168 2026-11-14 20:23 /nids/raw/cicids2017/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
-rw-r--r--   2 naveen supergroup   58316725 2026-11-14 20:25 /nids/raw/cicids2017/Friday-WorkingHours-Morning.pcap_ISCX.csv
-rw-r--r--   2 naveen supergroup  176927918 2026-11-14 20:24 /nids/raw/cicids2017/Monday-WorkingHours.pcap_ISCX.csv
-rw-r--r--   2 naveen supergroup   83102436 2026-11-14 20:26 /nids/raw/cicids2017/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
-rw-r--r--   2 naveen supergroup   52023263 2026-11-14 20:21 /nids/raw/cicids2017/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
-rw-r--r--   2 naveen supergroup  135078995 2026-11-14 20:25 /nids/raw/cicids2017/Tuesday-WorkingHours.pcap_ISCX.csv
-rw-r--r--   2 naveen supergroup  225166395 2026-11-14 20:22 /nids/raw/cicids2017/Wednesday-workingHours.pcap_ISCX.csv
(venv) [naveen@archlinux Downloads]$ source ~/NIDS/venv/bin/activate

export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export SPARK_HOME=$HOME/NIDS/spark-3.5.9-bin-hadoop3
export HADOOP_HOME=/opt/hadoop-2.9.1
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop

export PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH

hdfs dfs -ls /nids/raw/cicids2017/\
> \^C
(venv) [naveen@archlinux Downloads]$ ^C
(venv) [naveen@archlinux Downloads]$ source ~/NIDS/venv/bin/activate

export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export SPARK_HOME=$HOME/NIDS/spark-3.5.9-bin-hadoop3
export HADOOP_HOME=/opt/hadoop-2.9.1
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop

export PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH

hdfs dfs -ls /nids/raw/cicids2017/
Found 8 items
-rw-r--r--   2 naveen supergroup   77123859 2026-11-14 20:21 /nids/raw/cicids2017/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
-rw-r--r--   2 naveen supergroup   76906168 2026-11-14 20:23 /nids/raw/cicids2017/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
-rw-r--r--   2 naveen supergroup   58316725 2026-11-14 20:25 /nids/raw/cicids2017/Friday-WorkingHours-Morning.pcap_ISCX.csv
-rw-r--r--   2 naveen supergroup  176927918 2026-11-14 20:24 /nids/raw/cicids2017/Monday-WorkingHours.pcap_ISCX.csv
-rw-r--r--   2 naveen supergroup   83102436 2026-11-14 20:26 /nids/raw/cicids2017/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
-rw-r--r--   2 naveen supergroup   52023263 2026-11-14 20:21 /nids/raw/cicids2017/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
-rw-r--r--   2 naveen supergroup  135078995 2026-11-14 20:25 /nids/raw/cicids2017/Tuesday-WorkingHours.pcap_ISCX.csv
-rw-r--r--   2 naveen supergroup  225166395 2026-11-14 20:22 /nids/raw/cicids2017/Wednesday-workingHours.pcap_ISCX.csv
(venv) [naveen@archlinux Downloads]$ sudo ufw allow from 10.87.234.88 to any port 7077 proto tcp
sudo ufw allow from 10.87.234.88 to any port 8080 proto tcp
sudo ufw allow from 10.87.234.88 to any port 7078 proto tcp
sudo ufw allow from 10.87.234.88 to any port 8081 proto tcp
[sudo] password for naveen: 
Rule added
Rule added
Rule added
Rule added
(venv) [naveen@archlinux Downloads]$ start-master.sh
starting org.apache.spark.deploy.master.Master, logging to /home/naveen/NIDS/spark-3.5.9-bin-hadoop3/logs/spark-naveen-org.apache.spark.deploy.master.Master-1-archlinux.out
(venv) [naveen@archlinux Downloads]$ jps
37856 Master
27536 NodeManager
37954 Jps
27431 ResourceManager
26679 DataNode
26872 SecondaryNameNode
26540 NameNode
(venv) [naveen@archlinux Downloads]$ start-worker.sh spark://10.87.234.198:7077
starting org.apache.spark.deploy.worker.Worker, logging to /home/naveen/NIDS/spark-3.5.9-bin-hadoop3/logs/spark-naveen-org.apache.spark.deploy.worker.Worker-1-archlinux.out
(venv) [naveen@archlinux Downloads]$ source ~/NIDS/venv/bin/activate

export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export SPARK_HOME=$HOME/NIDS/spark-3.5.9-bin-hadoop3
export HADOOP_HOME=/opt/hadoop-2.9.1
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop

export PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH
(venv) [naveen@archlinux Downloads]$ cat >> $SPARK_HOME/conf/spark-env.sh <<'EOF'
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export SPARK_MASTER_HOST=10.87.234.198
export SPARK_MASTER_PORT=7077
export SPARK_MASTER_WEBUI_PORT=8080
export SPARK_LOCAL_IP=10.87.234.198
export SPARK_WORKER_PORT=7078
export SPARK_WORKER_WEBUI_PORT=8081
EOF
(venv) [naveen@archlinux Downloads]$ export SPARK_LOCAL_IP=10.87.234.198
export SPARK_MASTER_HOST=10.87.234.198
(venv) [naveen@archlinux Downloads]$ sudo ufw allow from 10.87.234.88 to any port 7077 proto tcp
sudo ufw allow from 10.87.234.88 to any port 8080 proto tcp
sudo ufw allow from 10.87.234.88 to any port 7078 proto tcp
sudo ufw allow from 10.87.234.88 to any port 8081 proto tcp
Skipping adding existing rule
Skipping adding existing rule
Skipping adding existing rule
Skipping adding existing rule
(venv) [naveen@archlinux Downloads]$ start-master.sh
org.apache.spark.deploy.master.Master running as process 37856.  Stop it first.
(venv) [naveen@archlinux Downloads]$ jps
37856 Master
27536 NodeManager
27431 ResourceManager
26679 DataNode
26872 SecondaryNameNode
39033 Jps
38059 Worker
26540 NameNode
(venv) [naveen@archlinux Downloads]$ ss -lntp | grep 7077
LISTEN 0      4096   [::ffff:10.87.234.198]:7077             *:*    users:(("java",pid=37856,fd=291))
(venv) [naveen@archlinux Downloads]$ spark://10.87.234.198:7077
bash: spark://10.87.234.198:7077: No such file or directory
(venv) [naveen@archlinux Downloads]$ source ~/NIDS/venv/bin/activate

export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export SPARK_HOME=$HOME/NIDS/spark-3.5.9-bin-hadoop3
export HADOOP_HOME=/opt/hadoop-2.9.1
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH

export SPARK_LOCAL_IP=10.87.234.198
(venv) [naveen@archlinux Downloads]$ start-worker.sh spark://10.87.234.198:7077
org.apache.spark.deploy.worker.Worker running as process 38059.  Stop it first.
(venv) [naveen@archlinux Downloads]$ jps
39104 Jps
37856 Master
27536 NodeManager
27431 ResourceManager
26679 DataNode
26872 SecondaryNameNode
38059 Worker
26540 NameNode
(venv) [naveen@archlinux Downloads]$ jps
curl -s http://localhost:8080 | head
37856 Master
27536 NodeManager
27431 ResourceManager
26679 DataNode
26872 SecondaryNameNode
38059 Worker
26540 NameNode
39294 Jps
<!DOCTYPE html><html>
      <head>
        <meta http-equiv="Content-type" content="text/html; charset=utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/><link rel="stylesheet" href="/static/bootstrap.min.css" type="text/css"/><link rel="stylesheet" href="/static/vis-timeline-graph2d.min.css" type="text/css"/><link rel="stylesheet" href="/static/webui.css" type="text/css"/><link rel="stylesheet" href="/static/timeline-view.css" type="text/css"/><script src="/static/sorttable.js"></script><script src="/static/jquery-3.5.1.min.js"></script><script src="/static/vis-timeline-graph2d.min.js"></script><script src="/static/bootstrap.bundle.min.js"></script><script src="/static/initialize-tooltips.js"></script><script src="/static/table.js"></script><script src="/static/timeline-view.js"></script><script src="/static/log-view.js"></script><script src="/static/webui.js"></script><script>setUIRoot('')</script>
        
        <link rel="shortcut icon" href="/static/spark-logo-77x50px-hd.png"></link>
        <title>Spark Master at spark://10.87.234.198:7077</title>
      </head>
      <body>
        <div class="container-fluid">
          <div class="row">
(venv) [naveen@archlinux Downloads]$ export PYSPARK_PYTHON=/home/naveen/NIDS/venv/bin/python
export PYSPARK_DRIVER_PYTHON=/home/naveen/NIDS/venv/bin/python
(venv) [naveen@archlinux Downloads]$ echo 'export PYSPARK_PYTHON=/home/naveen/NIDS/venv/bin/python' \
>> ~/NIDS/spark-3.5.9-bin-hadoop3/conf/spark-env.sh
(venv) [naveen@archlinux Downloads]$ mkdir -p ~/NIDS/src
mkdir -p ~/NIDS/models
mkdir -p ~/NIDS/results
mkdir -p ~/NIDS/logs
(venv) [naveen@archlinux Downloads]$ nano ~/NIDS/src/train_nids.py
(venv) [naveen@archlinux Downloads]$ nano ~/NIDS/src/train_nids.py
(venv) [naveen@archlinux Downloads]$ sudo ufw allow from 10.87.234.88 to any port 39000 proto tcp
sudo ufw allow from 10.87.234.88 to any port 39001 proto tcp
Rule added
Rule added
(venv) [naveen@archlinux Downloads]$ source ~/NIDS/venv/bin/activate

export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export SPARK_HOME=$HOME/NIDS/spark-3.5.9-bin-hadoop3
export HADOOP_HOME=/opt/hadoop-2.9.1
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export PYSPARK_PYTHON=/home/naveen/NIDS/venv/bin/python
export PYSPARK_DRIVER_PYTHON=/home/naveen/NIDS/venv/bin/python
export PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH
(venv) [naveen@archlinux Downloads]$ spark-submit \
  --master spark://10.87.234.198:7077 \
  --deploy-mode client \
  --name NIDS-RandomForest \
  --driver-memory 2g \
  --executor-memory 1g \
  --executor-cores 1 \
  --total-executor-cores 2 \
  --conf spark.driver.host=10.87.234.198 \
  --conf spark.driver.bindAddress=0.0.0.0 \
  --conf spark.driver.port=39000 \
  --conf spark.blockManager.port=39001 \
  --conf spark.sql.shuffle.partitions=8 \
  --conf spark.pyspark.python=/home/naveen/NIDS/venv/bin/python \
  --conf spark.executorEnv.PYSPARK_PYTHON=/home/om/anaconda3/envs/nids/bin/python \
  ~/NIDS/src/train_nids.py
Traceback (most recent call last):
  File "/home/naveen/NIDS/src/train_nids.py", line 5, in <module>
    from pyspark.ml import Pipeline
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/pyspark.zip/pyspark/ml/__init__.py", line 22, in <module>
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/pyspark.zip/pyspark/ml/base.py", line 40, in <module>
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/pyspark.zip/pyspark/ml/param/__init__.py", line 32, in <module>
ModuleNotFoundError: No module named 'numpy'
26/11/14 20:54:00 INFO ShutdownHookManager: Shutdown hook called
26/11/14 20:54:00 INFO ShutdownHookManager: Deleting directory /tmp/spark-ffb96045-6f61-4cca-8109-675b04a715c0
(venv) [naveen@archlinux Downloads]$ export PYSPARK_PYTHON=/home/$(whoami)/NIDS/venv/bin/python
(venv) [naveen@archlinux Downloads]$ --conf spark.pyspark.python=./NIDS/venv/bin/python
bash: --conf: command not found
(venv) [naveen@archlinux Downloads]$ spark-submit \
  --master spark://10.87.234.198:7077 \
  --deploy-mode client \
  --name NIDS-RandomForest \
  --driver-memory 2g \
  --executor-memory 1g \
  --executor-cores 1 \
  --total-executor-cores 2 \
  --conf spark.driver.host=10.87.234.198 \
  --conf spark.driver.bindAddress=0.0.0.0 \
  --conf spark.driver.port=39000 \
  --conf spark.blockManager.port=39001 \
  --conf spark.sql.shuffle.partitions=8 \
  --conf spark.pyspark.python=python3 \
  ~/NIDS/src/train_nids.py
Traceback (most recent call last):
  File "/home/naveen/NIDS/src/train_nids.py", line 5, in <module>
    from pyspark.ml import Pipeline
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/pyspark.zip/pyspark/ml/__init__.py", line 22, in <module>
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/pyspark.zip/pyspark/ml/base.py", line 40, in <module>
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/pyspark.zip/pyspark/ml/param/__init__.py", line 32, in <module>
ModuleNotFoundError: No module named 'numpy'
26/11/14 20:55:35 INFO ShutdownHookManager: Shutdown hook called
26/11/14 20:55:35 INFO ShutdownHookManager: Deleting directory /tmp/spark-a70f0616-4c55-4c45-93ae-c43c76ef51b1
(venv) [naveen@archlinux Downloads]$ source ~/NIDS/venv/bin/activate

python -m pip install "numpy==1.26.4"
/home/naveen/NIDS/venv/bin/python: No module named pip
(venv) [naveen@archlinux Downloads]$ python -c "import numpy; print(numpy.__version__)"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
(venv) [naveen@archlinux Downloads]$ source ~/NIDS/venv/bin/activate

python -m pip install "numpy==1.26.4"
/home/naveen/NIDS/venv/bin/python: No module named pip
(venv) [naveen@archlinux Downloads]$ source ~/NIDS/venv/bin/activate

python --version
which python

python -m ensurepip --upgrade
Python 3.11.18
/home/naveen/NIDS/venv/bin/python
Looking in links: /tmp/tmpulupirwb
Processing /tmp/tmpulupirwb/setuptools-79.0.1-py3-none-any.whl
Processing /tmp/tmpulupirwb/pip-26.2.2-py3-none-any.whl
Installing collected packages: setuptools, pip
Successfully installed pip-26.2.2 setuptools-79.0.1
(venv) [naveen@archlinux Downloads]$ python -m pip --version
pip 26.2.2 from /home/naveen/NIDS/venv/lib/python3.11/site-packages/pip (python 3.11)
(venv) [naveen@archlinux Downloads]$ python -m pip install --upgrade pip
python -m pip install "numpy==1.26.4"
Requirement already satisfied: pip in /home/naveen/NIDS/venv/lib/python3.11/site-packages (26.2.2)
Collecting pip
  Downloading pip-26.3-py3-none-any.whl.metadata (4.6 kB)
Downloading pip-26.3-py3-none-any.whl (2.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 1.6 MB/s  0:00:01
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 26.2.2
    Uninstalling pip-26.2.2:
      Successfully uninstalled pip-26.2.2
Successfully installed pip-26.3
Collecting numpy==1.26.4
  Downloading numpy-1.26.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (61 kB)
Downloading numpy-1.26.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (18.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 18.3/18.3 MB 5.1 MB/s  0:00:03
Installing collected packages: numpy
Successfully installed numpy-1.26.4
(venv) [naveen@archlinux Downloads]$ python -c "import numpy; print('NumPy:', numpy.__version__)"
NumPy: 1.26.4
(venv) [naveen@archlinux Downloads]$ python -c "import numpy; from pyspark.ml import Pipeline; print('NumPy and PySpark ML imports successful')"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'pyspark'
(venv) [naveen@archlinux Downloads]$ source ~/NIDS/venv/bin/activate

export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export SPARK_HOME=$HOME/NIDS/spark-3.5.9-bin-hadoop3
export HADOOP_HOME=/opt/hadoop-2.9.1
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop

export PYSPARK_PYTHON=/home/naveen/NIDS/venv/bin/python
export PYSPARK_DRIVER_PYTHON=/home/naveen/NIDS/venv/bin/python

export PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH
(venv) [naveen@archlinux Downloads]$ spark-submit \
  --master spark://10.87.234.198:7077 \
  --deploy-mode client \
  --conf spark.pyspark.python=/home/naveen/NIDS/venv/bin/python \
  --version
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.5.9
      /_/
                        
Using Scala version 2.12.18, OpenJDK 64-Bit Server VM, 17.0.21.0.3
Branch HEAD
Compiled by user holden on 2026-07-12T18:40:50Z
Revision 7c14a3c28b141cc97a330c4d0f5d2a6da7267f85
Url https://github.com/apache/spark
Type --help for more information.
(venv) [naveen@archlinux Downloads]$ tail -n 15 ~/NIDS/spark-3.5.9-bin-hadoop3/conf/spark-env.sh

export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export SPARK_MASTER_HOST=10.87.234.198
export SPARK_MASTER_PORT=7077
export SPARK_MASTER_WEBUI_PORT=8080
export SPARK_WORKER_PORT=7078
export SPARK_WORKER_WEBUI_PORT=8081
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export SPARK_MASTER_HOST=10.87.234.198
export SPARK_MASTER_PORT=7077
export SPARK_MASTER_WEBUI_PORT=8080
export SPARK_LOCAL_IP=10.87.234.198
export SPARK_WORKER_PORT=7078
export SPARK_WORKER_WEBUI_PORT=8081
export PYSPARK_PYTHON=/home/naveen/NIDS/venv/bin/python
(venv) [naveen@archlinux Downloads]$ export PYSPARK_PYTHON=/home/naveen/NIDS/venv/bin/python
(venv) [naveen@archlinux Downloads]$ source ~/NIDS/venv/bin/activate

export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export SPARK_HOME=$HOME/NIDS/spark-3.5.9-bin-hadoop3
export PYSPARK_PYTHON=/home/naveen/NIDS/venv/bin/python
export SPARK_LOCAL_IP=10.87.234.198

export PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH

stop-worker.sh
start-worker.sh spark://10.87.234.198:7077

jps
stopping org.apache.spark.deploy.worker.Worker
starting org.apache.spark.deploy.worker.Worker, logging to /home/naveen/NIDS/spark-3.5.9-bin-hadoop3/logs/spark-naveen-org.apache.spark.deploy.worker.Worker-1-archlinux.out
37856 Master
27536 NodeManager
41714 Worker
41798 Jps
27431 ResourceManager
26679 DataNode
26872 SecondaryNameNode
26540 NameNode
(venv) [naveen@archlinux Downloads]$ jps
37856 Master
27536 NodeManager
41714 Worker
27431 ResourceManager
26679 DataNode
26872 SecondaryNameNode
41900 Jps
26540 NameNode
(venv) [naveen@archlinux Downloads]$ curl -s http://localhost:8080/json/
{
  "url" : "spark://10.87.234.198:7077",
  "workers" : [ {
    "id" : "worker-20261114210324-10.87.234.88-7078",
    "host" : "10.87.234.88",
    "port" : 7078,
    "webuiaddress" : "http://10.87.234.88:8081",
    "cores" : 12,
    "coresused" : 0,
    "coresfree" : 12,
    "memory" : 4735,
    "memoryused" : 0,
    "memoryfree" : 4735,
    "resources" : { },
    "resourcesused" : { },
    "resourcesfree" : { },
    "state" : "ALIVE",
    "lastheartbeat" : 1794670464886
  }, {
    "id" : "worker-20261114210309-10.87.234.198-7078",
    "host" : "10.87.234.198",
    "port" : 7078,
    "webuiaddress" : "http://10.87.234.198:8081",
    "cores" : 16,
    "coresused" : 0,
    "coresfree" : 16,
    "memory" : 14373,
    "memoryused" : 0,
    "memoryfree" : 14373,
    "resources" : { },
    "resourcesused" : { },
    "resourcesfree" : { },
    "state" : "ALIVE",
    "lastheartbeat" : 1794670464745
  } ],
  "aliveworkers" : 2,
  "cores" : 28,
  "coresused" : 0,
  "memory" : 19108,
  "memoryused" : 0,
  "resources" : [ { }, { } ],
  "resourcesused" : [ { }, { } ],
  "activeapps" : [ ],
  "completedapps" : [ ],
  "activedrivers" : [ ],
  "completeddrivers" : [ ],
  "status" : "ALIVE"
}(venv) [naveen@archlinux Downloads]$source ~/NIDS/venv/bin/activatee

export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export SPARK_HOME=$HOME/NIDS/spark-3.5.9-bin-hadoop3
export HADOOP_HOME=/opt/hadoop-2.9.1
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop

export PYSPARK_PYTHON=/home/naveen/NIDS/venv/bin/python
export PYSPARK_DRIVER_PYTHON=/home/naveen/NIDS/venv/bin/python

export PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH
(venv) [naveen@archlinux Downloads]$ spark-submit \
  --master spark://10.87.234.198:7077 \
  --deploy-mode client \
  --name NIDS-RandomForest \
  --driver-memory 2g \
  --executor-memory 1g \
  --executor-cores 1 \
  --total-executor-cores 2 \
  --conf spark.driver.host=10.87.234.198 \
  --conf spark.driver.bindAddress=0.0.0.0 \
  --conf spark.driver.port=39000 \
  --conf spark.blockManager.port=39001 \
  --conf spark.sql.shuffle.partitions=8 \
  --conf spark.pyspark.python=/home/naveen/NIDS/venv/bin/python \
  ~/NIDS/src/train_nids.py
26/11/14 21:04:47 INFO SparkContext: Running Spark version 3.5.9
26/11/14 21:04:47 INFO SparkContext: OS info Linux, 7.2.15-arch1-1, amd64
26/11/14 21:04:47 INFO SparkContext: Java version 17.0.21.0.3
26/11/14 21:04:47 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
26/11/14 21:04:47 INFO ResourceUtils: ==============================================================
26/11/14 21:04:47 INFO ResourceUtils: No custom resources configured for spark.driver.
26/11/14 21:04:47 INFO ResourceUtils: ==============================================================
26/11/14 21:04:47 INFO SparkContext: Submitted application: Distributed-NIDS-RandomForest
26/11/14 21:04:47 INFO ResourceProfile: Default ResourceProfile created, executor resources: Map(cores -> name: cores, amount: 1, script: , vendor: , memory -> name: memory, amount: 1024, script: , vendor: , offHeap -> name: offHeap, amount: 0, script: , vendor: ), task resources: Map(cpus -> name: cpus, amount: 1.0)
26/11/14 21:04:47 INFO ResourceProfile: Limiting resource is cpus at 1 tasks per executor
26/11/14 21:04:47 INFO ResourceProfileManager: Added ResourceProfile id: 0
26/11/14 21:04:48 INFO SecurityManager: Changing view acls to: naveen
26/11/14 21:04:48 INFO SecurityManager: Changing modify acls to: naveen
26/11/14 21:04:48 INFO SecurityManager: Changing view acls groups to: 
26/11/14 21:04:48 INFO SecurityManager: Changing modify acls groups to: 
26/11/14 21:04:48 INFO SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users with view permissions: naveen; groups with view permissions: EMPTY; users with modify permissions: naveen; groups with modify permissions: EMPTY
26/11/14 21:04:48 INFO Utils: Successfully started service 'sparkDriver' on port 39000.
26/11/14 21:04:48 INFO SparkEnv: Registering MapOutputTracker
26/11/14 21:04:48 INFO SparkEnv: Registering BlockManagerMaster
26/11/14 21:04:48 INFO BlockManagerMasterEndpoint: Using org.apache.spark.storage.DefaultTopologyMapper for getting topology information
26/11/14 21:04:48 INFO BlockManagerMasterEndpoint: BlockManagerMasterEndpoint up
26/11/14 21:04:48 INFO SparkEnv: Registering BlockManagerMasterHeartbeat
26/11/14 21:04:48 INFO DiskBlockManager: Created local directory at /tmp/blockmgr-49ee6960-daeb-46dd-a7eb-dc0ec3e97225
26/11/14 21:04:48 INFO MemoryStore: MemoryStore started with capacity 1048.8 MiB
26/11/14 21:04:48 INFO SparkEnv: Registering OutputCommitCoordinator
26/11/14 21:04:48 INFO JettyUtils: Start Jetty 10.87.234.198:4040 for SparkUI
26/11/14 21:04:48 INFO Utils: Successfully started service 'SparkUI' on port 4040.
26/11/14 21:04:48 INFO StandaloneAppClient$ClientEndpoint: Connecting to master spark://10.87.234.198:7077...
26/11/14 21:04:48 INFO TransportClientFactory: Successfully created connection to /10.87.234.198:7077 after 28 ms (0 ms spent in bootstraps)
26/11/14 21:04:48 INFO StandaloneSchedulerBackend: Connected to Spark cluster with app ID app-20261114210448-0000
26/11/14 21:04:48 INFO Utils: Successfully started service 'org.apache.spark.network.netty.NettyBlockTransferService' on port 39001.
26/11/14 21:04:48 INFO NettyBlockTransferService: Server created on 10.87.234.198 0.0.0.0:39001
26/11/14 21:04:48 INFO BlockManager: Using org.apache.spark.storage.RandomBlockReplicationPolicy for block replication policy
26/11/14 21:04:48 INFO StandaloneAppClient$ClientEndpoint: Executor added: app-20261114210448-0000/0 on worker-20261114210309-10.87.234.198-7078 (10.87.234.198:7078) with 1 core(s)
26/11/14 21:04:48 INFO BlockManagerMaster: Registering BlockManager BlockManagerId(driver, 10.87.234.198, 39001, None)
26/11/14 21:04:48 INFO StandaloneSchedulerBackend: Granted executor ID app-20261114210448-0000/0 on hostPort 10.87.234.198:7078 with 1 core(s), 1024.0 MiB RAM
26/11/14 21:04:48 INFO StandaloneAppClient$ClientEndpoint: Executor added: app-20261114210448-0000/1 on worker-20261114210324-10.87.234.88-7078 (10.87.234.88:7078) with 1 core(s)
26/11/14 21:04:48 INFO StandaloneSchedulerBackend: Granted executor ID app-20261114210448-0000/1 on hostPort 10.87.234.88:7078 with 1 core(s), 1024.0 MiB RAM
26/11/14 21:04:48 INFO BlockManagerMasterEndpoint: Registering block manager 10.87.234.198:39001 with 1048.8 MiB RAM, BlockManagerId(driver, 10.87.234.198, 39001, None)
26/11/14 21:04:48 INFO BlockManagerMaster: Registered BlockManager BlockManagerId(driver, 10.87.234.198, 39001, None)
26/11/14 21:04:48 INFO BlockManager: Initialized BlockManager: BlockManagerId(driver, 10.87.234.198, 39001, None)
26/11/14 21:04:49 INFO StandaloneAppClient$ClientEndpoint: Executor updated: app-20261114210448-0000/0 is now RUNNING
26/11/14 21:04:49 INFO StandaloneSchedulerBackend: SchedulerBackend is ready for scheduling beginning after reached minRegisteredResourcesRatio: 0.0
26/11/14 21:04:49 INFO StandaloneAppClient$ClientEndpoint: Executor updated: app-20261114210448-0000/1 is now RUNNING

========== NIDS TRAINING STARTED ==========

Spark application: app-20261114210448-0000
Spark master: spark://10.87.234.198:7077
Dataset columns: 79
^CERROR:root:Exception while sending command.
Traceback (most recent call last):
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/py4j-0.10.9.7-src.zip/py4j/clientserver.py", line 511, in send_command
    answer = smart_decode(self.stream.readline()[:-1])
                          ^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: reentrant call inside <_io.BufferedReader name=6>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/py4j-0.10.9.7-src.zip/py4j/java_gateway.py", line 1038, in send_command
    response = connection.send_command(command)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/py4j-0.10.9.7-src.zip/py4j/clientserver.py", line 539, in send_command
    raise Py4JNetworkError(
py4j.protocol.Py4JNetworkError: Error while sending or receiving
ERROR:root:Exception while sending command.
Traceback (most recent call last):
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/py4j-0.10.9.7-src.zip/py4j/clientserver.py", line 511, in send_command
    answer = smart_decode(self.stream.readline()[:-1])
                          ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/naveen/.local/share/uv/python/cpython-3.11.18-linux-x86_64-gnu/lib/python3.11/socket.py", line 718, in readinto
    return self._sock.recv_into(b)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/pyspark.zip/pyspark/context.py", line 381, in signal_handler
    self.cancelAllJobs()
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/pyspark.zip/pyspark/context.py", line 2446, in cancelAllJobs
    self._jsc.sc().cancelAllJobs()
    ^^^^^^^^^^^^^^
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/py4j-0.10.9.7-src.zip/py4j/java_gateway.py", line 1322, in __call__
    return_value = get_return_value(
                   ^^^^^^^^^^^^^^^^^
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/pyspark.zip/pyspark/errors/exceptions/captured.py", line 179, in deco
    return f(*a, **kw)
           ^^^^^^^^^^^
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/py4j-0.10.9.7-src.zip/py4j/protocol.py", line 334, in get_return_value
    raise Py4JError(
py4j.protocol.Py4JError: An error occurred while calling o22.sc

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/py4j-0.10.9.7-src.zip/py4j/java_gateway.py", line 1038, in send_command
    response = connection.send_command(command)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/py4j-0.10.9.7-src.zip/py4j/clientserver.py", line 539, in send_command
    raise Py4JNetworkError(
py4j.protocol.Py4JNetworkError: Error while sending or receiving
Traceback (most recent call last):
  File "/home/naveen/NIDS/src/train_nids.py", line 49, in <module>
    print("Original records:", df.count())
                               ^^^^^^^^^^
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/pyspark.zip/pyspark/sql/dataframe.py", line 1239, in count
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/py4j-0.10.9.7-src.zip/py4j/java_gateway.py", line 1322, in __call__
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/pyspark.zip/pyspark/errors/exceptions/captured.py", line 179, in deco
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/py4j-0.10.9.7-src.zip/py4j/protocol.py", line 334, in get_return_value
py4j.protocol.Py4JError: An error occurred while calling o45.count
(venv) [naveen@archlinux Downloads]$ jps
37856 Master
27536 NodeManager
41714 Worker
27431 ResourceManager
26679 DataNode
26872 SecondaryNameNode
26540 NameNode
52237 Jps
(venv) [naveen@archlinux Downloads]$ source ~/NIDS/venv/bin/activate

export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export SPARK_HOME=$HOME/NIDS/spark-3.5.9-bin-hadoop3
export HADOOP_HOME=/opt/hadoop-2.9.1
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop

export PYSPARK_PYTHON=/home/naveen/NIDS/venv/bin/python
export PYSPARK_DRIVER_PYTHON=/home/naveen/NIDS/venv/bin/python

export PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH
(venv) [naveen@archlinux Downloads]$ source ~/NIDS/venv/bin/activate

export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export SPARK_HOME=$HOME/NIDS/spark-3.5.9-bin-hadoop3
export HADOOP_HOME=/opt/hadoop-2.9.1
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop

export PYSPARK_PYTHON=/home/naveen/NIDS/venv/bin/python
export PYSPARK_DRIVER_PYTHON=/home/naveen/NIDS/venv/bin/python

export PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH
(venv) [naveen@archlinux Downloads]$ spark-submit \
  --master spark://10.87.234.198:7077 \
  --deploy-mode client \
  --name NIDS-RandomForest \
  --driver-memory 2g \
  --executor-memory 1g \
  --executor-cores 1 \
  --total-executor-cores 2 \
  --conf spark.driver.host=10.87.234.198 \
  --conf spark.driver.bindAddress=0.0.0.0 \
  --conf spark.driver.port=39000 \
  --conf spark.blockManager.port=39001 \
  --conf spark.sql.shuffle.partitions=8 \
  --conf spark.pyspark.python=/home/naveen/NIDS/venv/bin/python \
  ~/NIDS/src/train_nids.py
26/11/14 22:29:18 INFO SparkContext: Running Spark version 3.5.9
26/11/14 22:29:18 INFO SparkContext: OS info Linux, 7.2.15-arch1-1, amd64
26/11/14 22:29:18 INFO SparkContext: Java version 17.0.21.0.3
26/11/14 22:29:18 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
26/11/14 22:29:18 INFO ResourceUtils: ==============================================================
26/11/14 22:29:18 INFO ResourceUtils: No custom resources configured for spark.driver.
26/11/14 22:29:18 INFO ResourceUtils: ==============================================================
26/11/14 22:29:18 INFO SparkContext: Submitted application: Distributed-NIDS-RandomForest
26/11/14 22:29:18 INFO ResourceProfile: Default ResourceProfile created, executor resources: Map(cores -> name: cores, amount: 1, script: , vendor: , memory -> name: memory, amount: 1024, script: , vendor: , offHeap -> name: offHeap, amount: 0, script: , vendor: ), task resources: Map(cpus -> name: cpus, amount: 1.0)
26/11/14 22:29:18 INFO ResourceProfile: Limiting resource is cpus at 1 tasks per executor
26/11/14 22:29:18 INFO ResourceProfileManager: Added ResourceProfile id: 0
26/11/14 22:29:18 INFO SecurityManager: Changing view acls to: naveen
26/11/14 22:29:18 INFO SecurityManager: Changing modify acls to: naveen
26/11/14 22:29:18 INFO SecurityManager: Changing view acls groups to: 
26/11/14 22:29:18 INFO SecurityManager: Changing modify acls groups to: 
26/11/14 22:29:18 INFO SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users with view permissions: naveen; groups with view permissions: EMPTY; users with modify permissions: naveen; groups with modify permissions: EMPTY
26/11/14 22:29:18 INFO Utils: Successfully started service 'sparkDriver' on port 39000.
26/11/14 22:29:18 INFO SparkEnv: Registering MapOutputTracker
26/11/14 22:29:18 INFO SparkEnv: Registering BlockManagerMaster
26/11/14 22:29:18 INFO BlockManagerMasterEndpoint: Using org.apache.spark.storage.DefaultTopologyMapper for getting topology information
26/11/14 22:29:18 INFO BlockManagerMasterEndpoint: BlockManagerMasterEndpoint up
26/11/14 22:29:18 INFO SparkEnv: Registering BlockManagerMasterHeartbeat
26/11/14 22:29:18 INFO DiskBlockManager: Created local directory at /tmp/blockmgr-02b37ec3-5f33-4ef3-8ecc-7175175b144b
26/11/14 22:29:18 INFO MemoryStore: MemoryStore started with capacity 1048.8 MiB
26/11/14 22:29:18 INFO SparkEnv: Registering OutputCommitCoordinator
26/11/14 22:29:19 INFO JettyUtils: Start Jetty 10.87.234.198:4040 for SparkUI
26/11/14 22:29:19 INFO Utils: Successfully started service 'SparkUI' on port 4040.
26/11/14 22:29:19 INFO StandaloneAppClient$ClientEndpoint: Connecting to master spark://10.87.234.198:7077...
26/11/14 22:29:19 INFO TransportClientFactory: Successfully created connection to /10.87.234.198:7077 after 26 ms (0 ms spent in bootstraps)
26/11/14 22:29:19 INFO StandaloneSchedulerBackend: Connected to Spark cluster with app ID app-20261114222919-0001
26/11/14 22:29:19 INFO StandaloneAppClient$ClientEndpoint: Executor added: app-20261114222919-0001/0 on worker-20261114210309-10.87.234.198-7078 (10.87.234.198:7078) with 1 core(s)
26/11/14 22:29:19 INFO StandaloneSchedulerBackend: Granted executor ID app-20261114222919-0001/0 on hostPort 10.87.234.198:7078 with 1 core(s), 1024.0 MiB RAM
26/11/14 22:29:19 INFO StandaloneAppClient$ClientEndpoint: Executor added: app-20261114222919-0001/1 on worker-20261114210309-10.87.234.198-7078 (10.87.234.198:7078) with 1 core(s)
26/11/14 22:29:19 INFO StandaloneSchedulerBackend: Granted executor ID app-20261114222919-0001/1 on hostPort 10.87.234.198:7078 with 1 core(s), 1024.0 MiB RAM
26/11/14 22:29:19 INFO Utils: Successfully started service 'org.apache.spark.network.netty.NettyBlockTransferService' on port 39001.
26/11/14 22:29:19 INFO NettyBlockTransferService: Server created on 10.87.234.198 0.0.0.0:39001
26/11/14 22:29:19 INFO BlockManager: Using org.apache.spark.storage.RandomBlockReplicationPolicy for block replication policy
26/11/14 22:29:19 INFO BlockManagerMaster: Registering BlockManager BlockManagerId(driver, 10.87.234.198, 39001, None)
26/11/14 22:29:19 INFO BlockManagerMasterEndpoint: Registering block manager 10.87.234.198:39001 with 1048.8 MiB RAM, BlockManagerId(driver, 10.87.234.198, 39001, None)
26/11/14 22:29:19 INFO BlockManagerMaster: Registered BlockManager BlockManagerId(driver, 10.87.234.198, 39001, None)
26/11/14 22:29:19 INFO BlockManager: Initialized BlockManager: BlockManagerId(driver, 10.87.234.198, 39001, None)
26/11/14 22:29:19 INFO StandaloneAppClient$ClientEndpoint: Executor updated: app-20261114222919-0001/1 is now RUNNING
26/11/14 22:29:19 INFO StandaloneAppClient$ClientEndpoint: Executor updated: app-20261114222919-0001/0 is now RUNNING
26/11/14 22:29:19 INFO StandaloneSchedulerBackend: SchedulerBackend is ready for scheduling beginning after reached minRegisteredResourcesRatio: 0.0

========== NIDS TRAINING STARTED ==========

Spark application: app-20261114222919-0001
Spark master: spark://10.87.234.198:7077
Dataset columns: 79
Original records: 2830743
26/11/14 22:29:42 WARN SparkStringUtils: Truncated the string representation of a plan since it was too large. This behavior can be adjusted by setting 'spark.sql.debug.maxToStringFields'.

========== DATASET SUMMARY ==========
Total cleaned records: 2830743
Number of features: 78

Class distribution:
+-----+-------+
|label|  count|
+-----+-------+
|  0.0|2273097|
|  1.0| 557646|
+-----+-------+


Training records: 1981730
Validation records: 424214
Testing records: 424799

Class weights:
BENIGN: 0.622607566812192
ATTACK: 2.539025865205738

========== TRAINING RANDOM FOREST ==========
26/11/14 22:32:26 WARN DAGScheduler: Broadcasting large task binary with size 1112.4 KiB
26/11/14 22:32:45 WARN DAGScheduler: Broadcasting large task binary with size 1602.5 KiB
26/11/14 22:33:05 WARN DAGScheduler: Broadcasting large task binary with size 2.3 MiB
26/11/14 22:33:27 WARN DAGScheduler: Broadcasting large task binary with size 3.2 MiB
26/11/14 22:33:51 WARN DAGScheduler: Broadcasting large task binary with size 4.4 MiB
26/11/14 22:34:17 WARN DAGScheduler: Broadcasting large task binary with size 5.8 MiB
26/11/14 22:34:45 WARN DAGScheduler: Broadcasting large task binary with size 7.4 MiB

Model training completed!
26/11/14 22:35:14 WARN DAGScheduler: Broadcasting large task binary with size 4.6 MiB
26/11/14 22:35:21 WARN DAGScheduler: Broadcasting large task binary with size 4.6 MiB
26/11/14 22:35:27 WARN DAGScheduler: Broadcasting large task binary with size 4.6 MiB
26/11/14 22:35:33 WARN DAGScheduler: Broadcasting large task binary with size 4.6 MiB
26/11/14 22:35:39 WARN DAGScheduler: Broadcasting large task binary with size 4.6 MiB
26/11/14 22:35:45 WARN DAGScheduler: Broadcasting large task binary with size 4.6 MiB

========== TEST RESULTS ==========
Validation Accuracy: 0.9970
Test Accuracy:       0.9969
Weighted Precision:  0.9969
Weighted Recall:     0.9969
Weighted F1 Score:   0.9969
ROC-AUC:             0.9998

========== CONFUSION MATRIX ==========
26/11/14 22:35:52 WARN DAGScheduler: Broadcasting large task binary with size 4.6 MiB
26/11/14 22:35:59 WARN DAGScheduler: Broadcasting large task binary with size 4.6 MiB
+-----+----------+------+
|label|prediction| count|
+-----+----------+------+
|  0.0|       0.0|340092|
|  0.0|       1.0|  1105|
|  1.0|       0.0|   230|
|  1.0|       1.0| 83372|
+-----+----------+------+

26/11/14 22:36:01 WARN TaskSetManager: Stage 88 contains a task of very large size (2179 KiB). The maximum recommended task size is 1000 KiB.
Traceback (most recent call last):
  File "/home/naveen/NIDS/src/train_nids.py", line 306, in <module>
    metrics_df = spark.createDataFrame(
                 ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/pyspark.zip/pyspark/sql/session.py", line 1443, in createDataFrame
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/pyspark.zip/pyspark/sql/session.py", line 1485, in _create_dataframe
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/pyspark.zip/pyspark/sql/session.py", line 1093, in _createFromLocal
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/pyspark.zip/pyspark/sql/session.py", line 955, in _inferSchemaFromList
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/pyspark.zip/pyspark/sql/types.py", line 1808, in _merge_type
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/pyspark.zip/pyspark/sql/types.py", line 1810, in <listcomp>
  File "/home/naveen/NIDS/spark-3.5.9-bin-hadoop3/python/lib/pyspark.zip/pyspark/sql/types.py", line 1800, in _merge_type
pyspark.errors.exceptions.base.PySparkTypeError: [CANNOT_MERGE_TYPE] Can not merge type `DoubleType` and `LongType`.
(venv) [naveen@archlinux Downloads]$ ^C
(venv) [naveen@archlinux Downloads]$ nl -ba ~/NIDS/src/train_nids.py | sed -n '280,340p'
   280	    .orderBy("label", "prediction")
   281	)
   282	
   283	confusion.show()
   284	
   285	# --------------------------------------------------
   286	# 9. Save trained model and results to HDFS
   287	# --------------------------------------------------
   288	
   289	model.write().overwrite().save(MODEL_PATH)
   290	
   291	metrics = [
   292	    ("validation_accuracy", float(validation_accuracy)),
   293	    ("test_accuracy", float(accuracy)),
   294	    ("weighted_precision", float(precision)),
   295	    ("weighted_recall", float(recall)),
   296	    ("weighted_f1", float(f1)),
   297	    ("roc_auc", float(auc)),
   298	    ("training_records", int(train_count)),
   299	    ("validation_records", int(val_df.count())),
   300	    ("test_records", int(test_df.count())),
   301	    ("feature_count", int(len(feature_cols))),
   302	    ("random_forest_trees", 100),
   303	    ("random_forest_max_depth", 12)
   304	]
   305	
   306	metrics_df = spark.createDataFrame(
   307	    metrics,
   308	    ["metric", "value"]
   309	)
   310	
   311	metrics_df.write.mode("overwrite").csv(
   312	    RESULT_PATH + "/metrics",
   313	    header=True
   314	)
   315	
   316	confusion.write.mode("overwrite").csv(
   317	    RESULT_PATH + "/confusion_matrix",
   318	    header=True
   319	)
   320	
   321	print("\nModel saved to:", MODEL_PATH)
   322	print("Results saved to:", RESULT_PATH)
   323	
   324	# --------------------------------------------------
   325	# 10. Cleanup
   326	# --------------------------------------------------
   327	
   328	train_df.unpersist()
   329	val_df.unpersist()
   330	test_df.unpersist()
   331	df.unpersist()
   332	
   333	spark.stop()
   334	
   335	print("\n========== NIDS TRAINING FINISHED ==========\n")
(venv) [naveen@archlinux Downloads]$ hdfs dfs -ls /nids/models/
Found 1 items
drwxr-xr-x   - naveen supergroup          0 2026-11-14 22:36 /nids/models/random_forest_binary_v1
(venv) [naveen@archlinux Downloads]$ hdfs dfs -ls /nids/results/
(venv) [naveen@archlinux Downloads]$ source ~/NIDS/venv/bin/activate

python -m pip install streamlit pandas
Collecting streamlit
  Downloading streamlit-1.67.0-py3-none-any.whl.metadata (10 kB)
Collecting pandas
  Downloading pandas-3.1.1-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (16 kB)
Collecting altair!=5.4.0,!=5.4.1,<7,>=5.0.0 (from streamlit)
  Downloading altair-6.3.0-py3-none-any.whl.metadata (11 kB)
Collecting click<9,>=7.0 (from streamlit)
  Downloading click-8.5.1-py3-none-any.whl.metadata (2.6 kB)
Requirement already satisfied: numpy<3,>=1.25.0 in /home/naveen/NIDS/venv/lib/python3.11/site-packages (from streamlit) (1.26.4)
Collecting packaging>=20 (from streamlit)
  Downloading packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
Collecting pillow<14,>=9.2.0 (from streamlit)
  Downloading pillow-13.0.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (9.1 kB)
Collecting pydeck<1,>=0.8.0b4 (from streamlit)
  Downloading pydeck-0.9.3-py2.py3-none-any.whl.metadata (4.2 kB)
Collecting protobuf<8,>=5.26.1 (from streamlit)
  Downloading protobuf-7.36.2-cp310-abi3-manylinux2014_x86_64.whl.metadata (595 bytes)
Collecting pyarrow!=25.0.0,<27,>=12.0.0 (from streamlit)
  Downloading pyarrow-26.0.1-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (3.0 kB)
Collecting requests<3,>=2.27 (from streamlit)
  Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
Collecting typing-extensions<5,>=4.10.0 (from streamlit)
  Downloading typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
Collecting starlette<2,>=0.46.0 (from streamlit)
  Downloading starlette-1.10.0-py3-none-any.whl.metadata (6.6 kB)
Collecting uvicorn<1,>=0.30.0 (from streamlit)
  Downloading uvicorn-0.54.0-py3-none-any.whl.metadata (6.6 kB)
Collecting anyio<5,>=4.0.0 (from streamlit)
  Downloading anyio-4.16.0-py3-none-any.whl.metadata (4.7 kB)
Collecting python-multipart<1,>=0.0.10 (from streamlit)
  Downloading python_multipart-0.0.33-py3-none-any.whl.metadata (6.3 kB)
Collecting websockets<18,>=12.0.0 (from streamlit)
  Downloading websockets-17.4-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (6.3 kB)
Collecting itsdangerous<3,>=2.1.2 (from streamlit)
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting watchdog<8,>=2.1.5 (from streamlit)
  Downloading watchdog-7.1.0-py3-none-manylinux_2_17_x86_64.whl.metadata (62 kB)
Collecting numpy<3,>=1.25.0 (from streamlit)
  Downloading numpy-2.4.6-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (6.6 kB)
Collecting python-dateutil>=2.9.0 (from pandas)
  Downloading python_dateutil-4.0.0-py3-none-any.whl.metadata (7.3 kB)
Collecting jinja2 (from altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting jsonschema>=3.0 (from altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Downloading jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)
Collecting narwhals>=2.4.0 (from altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Downloading narwhals-2.28.0-py3-none-any.whl.metadata (15 kB)
Collecting idna>=2.8 (from anyio<5,>=4.0.0->streamlit)
  Downloading idna-3.20-py3-none-any.whl.metadata (7.2 kB)
Collecting charset_normalizer<4,>=2 (from requests<3,>=2.27->streamlit)
  Downloading charset_normalizer-3.5.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (46 kB)
Collecting urllib3<3,>=1.26 (from requests<3,>=2.27->streamlit)
  Downloading urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)
Collecting certifi>=2023.5.7 (from requests<3,>=2.27->streamlit)
  Downloading certifi-2026.10.23-py3-none-any.whl.metadata (2.5 kB)
Collecting h11>=0.8 (from uvicorn<1,>=0.30.0->streamlit)
  Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting MarkupSafe>=2.0 (from jinja2->altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Downloading markupsafe-3.0.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
Collecting attrs>=22.2.0 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Downloading attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting referencing>=0.28.4 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Downloading referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)
Collecting rpds-py>=0.25.0 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Downloading rpds_py-2026.9.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.1 kB)
Collecting tzdata (from python-dateutil>=2.9.0->pandas)
  Downloading tzdata-2026.6-py2.py3-none-any.whl.metadata (1.4 kB)
Downloading streamlit-1.67.0-py3-none-any.whl (11.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.2/11.2 MB 1.4 MB/s  0:00:08
Downloading pandas-3.1.1-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (12.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.4/12.4 MB 1.3 MB/s  0:00:09
Downloading altair-6.3.0-py3-none-any.whl (797 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 797.2/797.2 kB 836.5 kB/s  0:00:00
Downloading anyio-4.16.0-py3-none-any.whl (134 kB)
Downloading click-8.5.1-py3-none-any.whl (126 kB)
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Downloading numpy-2.4.6-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.9/16.9 MB 1.7 MB/s  0:00:10
Downloading pillow-13.0.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (7.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.1/7.1 MB 2.6 MB/s  0:00:02
Downloading protobuf-7.36.2-cp310-abi3-manylinux2014_x86_64.whl (343 kB)
Downloading pyarrow-26.0.1-cp311-cp311-manylinux_2_28_x86_64.whl (55.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 55.0/55.0 MB 3.5 MB/s  0:00:15
Downloading pydeck-0.9.3-py2.py3-none-any.whl (11.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.4/11.4 MB 3.8 MB/s  0:00:03
Downloading python_multipart-0.0.33-py3-none-any.whl (32 kB)
Downloading requests-2.34.2-py3-none-any.whl (73 kB)
Downloading charset_normalizer-3.5.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (269 kB)
Downloading idna-3.20-py3-none-any.whl (69 kB)
Downloading starlette-1.10.0-py3-none-any.whl (80 kB)
Downloading typing_extensions-4.16.0-py3-none-any.whl (45 kB)
Downloading urllib3-2.8.0-py3-none-any.whl (135 kB)
Downloading uvicorn-0.54.0-py3-none-any.whl (87 kB)
Downloading watchdog-7.1.0-py3-none-manylinux_2_17_x86_64.whl (103 kB)
Downloading websockets-17.4-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (226 kB)
Downloading certifi-2026.10.23-py3-none-any.whl (135 kB)
Downloading h11-0.16.0-py3-none-any.whl (37 kB)
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading jsonschema-4.26.0-py3-none-any.whl (90 kB)
Downloading attrs-26.1.0-py3-none-any.whl (67 kB)
Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Downloading markupsafe-3.0.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
Downloading narwhals-2.28.0-py3-none-any.whl (490 kB)
Downloading packaging-26.3-py3-none-any.whl (129 kB)
Downloading python_dateutil-4.0.0-py3-none-any.whl (92 kB)
Downloading referencing-0.37.0-py3-none-any.whl (26 kB)
Downloading rpds_py-2026.9.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (375 kB)
Downloading tzdata-2026.6-py2.py3-none-any.whl (348 kB)
Installing collected packages: websockets, watchdog, urllib3, tzdata, typing-extensions, rpds-py, python-multipart, pyarrow, protobuf, pillow, packaging, numpy, narwhals, MarkupSafe, itsdangerous, idna, h11, click, charset_normalizer, certifi, attrs, uvicorn, requests, referencing, python-dateutil, jinja2, anyio, starlette, pydeck, pandas, jsonschema-specifications, jsonschema, altair, streamlit
  Attempting uninstall: numpy
    Found existing installation: numpy 1.26.4
    Uninstalling numpy-1.26.4:
      Successfully uninstalled numpy-1.26.4
Successfully installed MarkupSafe-3.0.4 altair-6.3.0 anyio-4.16.0 attrs-26.1.0 certifi-2026.10.23 charset_normalizer-3.5.2 click-8.5.1 h11-0.16.0 idna-3.20 itsdangerous-2.2.0 jinja2-3.1.6 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 narwhals-2.28.0 numpy-2.4.6 packaging-26.3 pandas-3.1.1 pillow-13.0.0 protobuf-7.36.2 pyarrow-26.0.1 pydeck-0.9.3 python-dateutil-4.0.0 python-multipart-0.0.33 referencing-0.37.0 requests-2.34.2 rpds-py-2026.9.1 starlette-1.10.0 streamlit-1.67.0 typing-extensions-4.16.0 tzdata-2026.6 urllib3-2.8.0 uvicorn-0.54.0 watchdog-7.1.0 websockets-17.4
(venv) [naveen@archlinux Downloads]$ nano ~/NIDS/src/dashboard.py
(venv) [naveen@archlinux Downloads]$ source ~/NIDS/venv/bin/activate

streamlit run ~/NIDS/src/dashboard.py \
  --server.address 0.0.0.0 \
  --server.port 8501

      👋 Welcome to Streamlit!

      If you'd like to receive helpful onboarding emails, news, offers, promotions,
      and the occasional swag, please enter your email address below. Otherwise,
      leave this field blank.

      Email: m26cse019@iitj.ac.in

  You can find our privacy policy at https://streamlit.io/privacy-policy

  Summary:
  - This open source library collects usage statistics.
  - We cannot see and do not store information contained inside Streamlit apps,
    such as text, charts, images, etc.
  - Telemetry data is stored in servers in the United States.
  - If you'd like to opt out, add the following to ~/.streamlit/config.toml,
    creating that file if necessary:

    [browser]
    gatherUsageStats = false

2026-11-14 22:45:32.145 Uvicorn server started on 0.0.0.0:8501

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://10.87.234.198:8501

  Help agents write better Streamlit apps?
  Install the official Streamlit skills by running streamlit skills in your terminal.

2026-11-14 22:45:36.633 Please replace `use_container_width` with `width`.

`use_container_width` will be removed after 2025-12-31.

For `use_container_width=True`, use `width='stretch'`. For `use_container_width=False`, use `width='content'`.
2026-11-14 22:45:36.655 Serialization of dataframe to Arrow table was unsuccessful. Applying automatic fixes for column types to make the dataframe Arrow-compatible.
Traceback (most recent call last):
  File "/home/naveen/NIDS/venv/lib/python3.11/site-packages/streamlit/dataframe_util.py", line 967, in convert_pandas_df_to_arrow_table
    return pa.Table.from_pandas(df, preserve_index=preserve_index)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "pyarrow/table.pxi", line 4777, in pyarrow.lib.Table.from_pandas
  File "/home/naveen/NIDS/venv/lib/python3.11/site-packages/pyarrow/pandas_compat.py", line 658, in dataframe_to_arrays
    arrays = [convert_column(c, f)
             ^^^^^^^^^^^^^^^^^^^^^
  File "/home/naveen/NIDS/venv/lib/python3.11/site-packages/pyarrow/pandas_compat.py", line 658, in <listcomp>
    arrays = [convert_column(c, f)
              ^^^^^^^^^^^^^^^^^^^^
  File "/home/naveen/NIDS/venv/lib/python3.11/site-packages/pyarrow/pandas_compat.py", line 643, in convert_column
    raise e
  File "/home/naveen/NIDS/venv/lib/python3.11/site-packages/pyarrow/pandas_compat.py", line 637, in convert_column
    result = pa.array(col, type=type_, from_pandas=True, safe=safe)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "pyarrow/array.pxi", line 414, in pyarrow.lib.array
  File "pyarrow/array.pxi", line 97, in pyarrow.lib._ndarray_to_array
  File "pyarrow/error.pxi", line 92, in pyarrow.lib.check_status
pyarrow.lib.ArrowTypeError: ("Expected bytes, got a 'int' object", 'Conversion failed for column Value with type object')
^C  Stopping...
(venv) [naveen@archlinux Downloads]$ source ~/NIDS/venv/bin/activate

streamlit run ~/NIDS/src/dashboard.py \
  --server.address 0.0.0.0 \
  --server.port 8501
2026-11-14 22:47:18.125 Uvicorn server started on 0.0.0.0:8501

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://10.87.234.198:8501

  Help agents write better Streamlit apps?
  Install the official Streamlit skills by running streamlit skills in your terminal.

2026-11-14 22:47:22.108 Please replace `use_container_width` with `width`.

`use_container_width` will be removed after 2025-12-31.

For `use_container_width=True`, use `width='stretch'`. For `use_container_width=False`, use `width='content'`.
2026-11-14 22:47:22.138 Serialization of dataframe to Arrow table was unsuccessful. Applying automatic fixes for column types to make the dataframe Arrow-compatible.
Traceback (most recent call last):
  File "/home/naveen/NIDS/venv/lib/python3.11/site-packages/streamlit/dataframe_util.py", line 967, in convert_pandas_df_to_arrow_table
    return pa.Table.from_pandas(df, preserve_index=preserve_index)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "pyarrow/table.pxi", line 4777, in pyarrow.lib.Table.from_pandas
  File "/home/naveen/NIDS/venv/lib/python3.11/site-packages/pyarrow/pandas_compat.py", line 658, in dataframe_to_arrays
    arrays = [convert_column(c, f)
             ^^^^^^^^^^^^^^^^^^^^^
  File "/home/naveen/NIDS/venv/lib/python3.11/site-packages/pyarrow/pandas_compat.py", line 658, in <listcomp>
    arrays = [convert_column(c, f)
              ^^^^^^^^^^^^^^^^^^^^
  File "/home/naveen/NIDS/venv/lib/python3.11/site-packages/pyarrow/pandas_compat.py", line 643, in convert_column
    raise e
  File "/home/naveen/NIDS/venv/lib/python3.11/site-packages/pyarrow/pandas_compat.py", line 637, in convert_column
    result = pa.array(col, type=type_, from_pandas=True, safe=safe)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "pyarrow/array.pxi", line 414, in pyarrow.lib.array
  File "pyarrow/array.pxi", line 97, in pyarrow.lib._ndarray_to_array
  File "pyarrow/error.pxi", line 92, in pyarrow.lib.check_status
pyarrow.lib.ArrowTypeError: ("Expected bytes, got a 'int' object", 'Conversion failed for column Value with type object')
```
