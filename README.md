# SOC Linux Authentication Log Analyzer

## Overview

This project simulates a **Security Operations Center (SOC) analyst workflow** by analyzing real Linux authentication logs (`auth.log`) to detect suspicious SSH activity. The goal is to demonstrate how Python can be used to automate common SOC tasks such as log ingestion, event filtering, indicator extraction, correlation, and alert generation.

This project is intentionally designed to mirror **junior SOC / cybersecurity analyst responsibilities** rather than advanced data science or machine learning.

---

## What This Project Detects

The current implementation focuses on SSH-related threats, including:

* 🚩 **Brute-force SSH login attempts** (high number of failed logins from a single IP)
* 🚩 **Password spraying behavior** (multiple failed logins against different usernames from the same IP)
* 🚩 **Suspicious authentication patterns** using threshold-based alerting

These detections are based on patterns commonly monitored in enterprise SOC environments.

---

## Log Source

* **Log type:** Linux authentication logs
* **File analyzed:** `auth.log`
* **Log events include:**

  * SSH failed login attempts
  * SSH successful logins
  * Privilege escalation via `sudo`

The logs are stored separately from the detection logic to reflect SOC best practices.

---

## Project Structure

```
soc-linux-auth-analyzer/
├── analyzer.py        # Python detection logic
├── logs/
│   └── auth.log       # Linux authentication logs
├── screenshots/       # Documentation screenshots
└── README.md
```

---

## How It Works (SOC Workflow)

1. **Log Ingestion**

   * Reads Linux authentication logs from `logs/auth.log`

2. **Event Filtering**

   * Identifies SSH authentication failures (`Failed password` events)

3. **Indicator Extraction**

   * Extracts source IP addresses from failed login events

4. **Event Correlation**

   * Counts failed authentication attempts per IP address

5. **Alert Generation**

   * Triggers alerts when failed attempts exceed a defined threshold

---

## Example Alert Output

```
ALERT: Possible brute-force attack from 203.0.113.50 (7 failed attempts)
```

---

## Technologies Used

* Python 3
* Linux authentication logs (`auth.log`)
* Git & GitHub
* PyCharm

No external Python libraries are required — only the Python standard library is used.

---

📸 Screenshot Walkthrough

Screenshot 1 – Project Structure

SOC-style project layout separating raw Linux authentication logs from Python detection logic.

Screenshot 2 – Linux auth.log

Realistic Linux authentication log containing SSH successful and failed login events used for analysis.

Screenshot 3 – Log Ingestion Code

Python script reading and iterating through Linux authentication logs to enable automated analysis.

Screenshot 4 – Log Ingestion Output

Console output confirming successful ingestion and processing of Linux auth.log entries.

Screenshot 5 – Failed SSH Login Filtering

Filtering authentication logs to isolate failed SSH login attempts for security analysis.

Screenshot 6 – Source IP Extraction

Extracting source IP addresses from failed SSH authentication events.

Screenshot 7 – Failed Login Correlation

Counting failed authentication attempts per IP address to identify potential attack patterns.

Screenshot 8 – Threshold-Based Alerting

Generating SOC-style alerts when failed login attempts exceed a defined threshold.

---

## Why This Project Matters

This project demonstrates:

* SOC-style log analysis and alerting
* Security-focused thinking and detection logic
* Python automation for cybersecurity operations
* Clear documentation and reproducible workflow
---

## Future Improvements

Planned enhancements include:

* Detecting successful logins after repeated failures
* Identifying off-hours authentication activity
* Adding alert severity levels (LOW / MEDIUM / HIGH)

---

## Author

Manzi Siibo:
Cybersecurity student focused on SOC operations, defensive security, and security automation.
