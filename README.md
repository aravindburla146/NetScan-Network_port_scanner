# 🔐 NetScan — Network Security & TCP Port Scanner


**NetScan** is a Python-based network security tool designed to identify open TCP ports and their commonly associated services on authorized systems.

The project combines a **Python socket-based scanning engine** with a **Flask web interface**, providing an easy-to-use interface for performing custom TCP port scans, viewing scan statistics, identifying common services, and exporting results as CSV reports.

---

## 📸 NetScan Preview

![NetScan Interface](screenshots/Screenshot%202026-09-05%20162123.png)

*NetScan web interface for TCP port scanning and network security analysis.*

---

## 🎯 Project Purpose

The purpose of NetScan is to provide a simple and educational network scanning tool that demonstrates how TCP port scanning works at the socket-programming level.

The project was developed to understand practical concepts including:

- TCP connections
- Network ports
- Socket programming
- Concurrent scanning
- Service identification
- Input validation
- Flask web applications
- Scan result processing
- CSV report generation

NetScan is intended for **cybersecurity education, authorized security testing, and network administration**.

---

## ✨ Features

### 🔍 TCP Port Scanning

- Scan individual TCP ports or custom port ranges
- Supports ports from `1` to `65535`
- Uses Python TCP sockets
- Detects open and closed ports

### ⚡ Concurrent Scanning

- Uses Python `ThreadPoolExecutor`
- Scans multiple ports concurrently
- Significantly improves scanning speed compared with sequential scanning

### 🧩 Service Identification

- Identifies commonly associated TCP services
- Uses Python's built-in service database
- Displays `Unknown` when a service cannot be identified

### 🌐 Web Interface

- Flask-powered web application
- Simple cybersecurity-themed interface
- Target IP/hostname input
- Custom start and end port selection
- Real-time scan status

### 📊 Scan Statistics

Displays:

- Total ports scanned
- Number of open ports
- Scan duration
- Detected services

### 📥 CSV Reporting

- Automatically generates a CSV report after each scan
- Includes target, port, status, and service
- Download reports directly from the web interface

### 🛡️ Input Validation

NetScan validates:

- IP addresses
- Hostnames
- Port numbers
- Port ranges
- Maximum scan range

The web interface limits a single scan request to **5,000 ports**.

---

## 🖥️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Core scanning engine |
| Socket | TCP port scanning |
| ThreadPoolExecutor | Concurrent scanning |
| Flask | Web application backend |
| HTML5 | Web interface structure |
| CSS3 | User interface styling |
| JavaScript | Frontend interaction and API requests |
| CSV | Scan report generation |

---

## 🏗️ System Architecture

```text
                 ┌──────────────────────┐
                 │      Web Browser     │
                 │   HTML/CSS/JS UI     │
                 └──────────┬───────────┘
                            │
                            │ HTTP Request
                            ▼
                 ┌──────────────────────┐
                 │      Flask App       │
                 │       app.py         │
                 └──────────┬───────────┘
                            │
                            │ Scan Request
                            ▼
                 ┌──────────────────────┐
                 │    Scanner Engine    │
                 │     scanner.py       │
                 └──────────┬───────────┘
                            │
                 ┌──────────┴───────────┐
                 │                      │
                 ▼                      ▼
        ┌─────────────────┐    ┌─────────────────┐
        │  TCP Sockets    │    │ Concurrent Scan │
        │  Port Testing   │    │ Thread Pool     │
        └────────┬────────┘    └────────┬────────┘
                 │                      │
                 └──────────┬───────────┘
                            ▼
                 ┌──────────────────────┐
                 │    Scan Results      │
                 │ Open / Closed /      │
                 │ Service Information  │
                 └──────────┬───────────┘
                            │
                 ┌──────────┴───────────┐
                 ▼                      ▼
        ┌─────────────────┐    ┌─────────────────┐
        │  Web Interface  │    │   CSV Report    │
        │  Results Table  │    │    Download     │
        └─────────────────┘    └─────────────────┘
```
---

### 🔐 Built with ❤️ for Cybersecurity. Scan Smart. Stay Secure. Keep Learning.
