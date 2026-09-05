# 🔐 NetScan — Network Security & TCP Port Scanner

NetScan is a Python-based TCP network port scanner designed to identify open TCP ports and their commonly associated services on authorized systems.

The project provides both a command-line scanner and a Flask-based web interface, allowing users to specify a target IP address or hostname and scan a custom range of TCP ports.

## 🎯 Project Purpose

The purpose of NetScan is to demonstrate the fundamentals of network reconnaissance and TCP port scanning using Python sockets.

The project focuses on understanding how TCP connections can be used to determine whether network services are accessible on specific ports.

## ✨ Features

- TCP port scanning using Python sockets
- Concurrent port scanning for improved performance
- Custom port-range selection
- IP address and hostname validation
- TCP service identification
- Scan statistics
- Web-based interface using Flask
- CSV report generation
- Input validation and error handling
- Responsive cybersecurity-themed interface

## ⚠️ Ethical Use

NetScan should only be used against systems that you own or have explicit authorization to test.

Unauthorized port scanning may violate organizational policies or applicable laws.

## 🛠️ Technologies Used

- **Python** — Core programming language
- **Python Socket Library** — TCP connection and port scanning
- **ThreadPoolExecutor** — Concurrent port scanning
- **Flask** — Web application backend
- **HTML5** — Web interface structure
- **CSS3** — User interface styling
- **JavaScript** — Frontend interaction and API communication
- **CSV** — Scan report generation


### ⚠️ One important thing

Because your `reports/` folder contains generated CSV files, we should **not commit those reports to GitHub** unless you specifically want sample reports there.

Your `.gitignore` should eventually contain:

```text
venv/
__pycache__/
*.pyc
reports/*.csv

