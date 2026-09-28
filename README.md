# 🔄 How CloudPulse Works

### 1. Monitoring Agent

A Python agent runs on each monitored virtual machine.

It collects:

```text
CPU Usage
Memory Usage
Disk Usage
Network Statistics
Hostname
Operating System
Uptime
Timestamp
```

The agent uses the `psutil` library to access system-level information.

### 2. Metric Transmission

The monitoring agent packages the collected information into JSON and sends it to the central monitoring server through a REST API.

Example:

```json
{
  "hostname": "cloudpulse-vm-01",
  "cpu_usage": 42.5,
  "memory_usage": 61.2,
  "disk_usage": 48.7,
  "network_sent": 12450,
  "network_received": 23890,
  "timestamp": "2026-09-19T10:30:00"
}
```

### 3. Central API

The Flask backend receives and processes the incoming monitoring data.

The API is responsible for:

* Receiving metrics
* Validating data
* Identifying VMs
* Storing metrics
* Providing data to the dashboard
* Processing alert conditions

### 4. Database

Monitoring data is stored in a relational database.

The database maintains information such as:

```text
VM Information
    │
    ├── Hostname
    ├── IP Address
    ├── Operating System
    └── Last Seen

Metrics
    │
    ├── CPU
    ├── Memory
    ├── Disk
    ├── Network
    └── Timestamp

Alerts
    │
    ├── VM
    ├── Metric
    ├── Threshold
    ├── Severity
    └── Timestamp
```

### 5. Dashboard

The dashboard provides a centralized view of all monitored infrastructure.

Users can view:

* Total monitored VMs
* Healthy VMs
* Warning VMs
* Critical VMs
* Current resource utilization
* Historical performance graphs
* VM availability
* Recent alerts

### 6. Alerting

CloudPulse evaluates resource utilization against configurable thresholds.

Example:

```text
CPU > 80%   → WARNING
CPU > 90%   → CRITICAL

RAM > 80%   → WARNING
RAM > 90%   → CRITICAL

Disk > 80%  → WARNING
Disk > 90%  → CRITICAL
```
