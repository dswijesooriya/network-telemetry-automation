# Network Automation & Telemetry Dashboard

A hands-on network engineering project demonstrating automated configuration backups and real-time monitoring using a virtual Nokia SR Linux router.

## 🏗️ Architecture
This lab simulates a production network environment using the following open-source stack:
*   **Virtualization:** Ubuntu Server 22.04 on VirtualBox
*   **Network Lab:** Containerlab + Docker (Nokia SR Linux)
*   **Telemetry:** SNMP -> SNMP Exporter -> Prometheus
*   **Visualization:** Grafana
*   **Automation:** Python + Netmiko

## 🚀 Features
*   **Live Monitoring:** Grafana dashboard displaying real-time router uptime, interface traffic (bits/sec), and interface UP/DOWN status.
*   **Automated Backups:** Python script using Netmiko to SSH into the router, capture the running configuration, and save it locally.
*   **Fault Tolerance:** Script includes `try/except` logic to handle unreachable devices gracefully without crashing.

## 🛠️ How to Reproduce (High Level)
1. Deploy the Containerlab topology: `sudo containerlab deploy -t simple-lab.yml`
2. Start Prometheus and SNMP Exporter services.
3. Run the Python automation script: `python3 multi_router.py`

## 📸 Dashboard Proof
*(When you upload the screenshot later, it goes here)*
