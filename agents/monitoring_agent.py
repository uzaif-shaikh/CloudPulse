
import time
import socket
from datetime import datetime

import psutil
import requests

API_URL = "http://127.0.0.1:5000/api/metrics"
SERVER_ID = 1
INTERVAL = 10


def collect_metrics():
    # Measure CPU usage over one second
    cpu_usage = psutil.cpu_percent(interval=1)

    memory_usage = psutil.virtual_memory().percent

    # Windows system drive; adjust if needed
    disk_usage = psutil.disk_usage("C:\\").percent

    # Cumulative network counters in bytes
    network = psutil.net_io_counters()

    return {
        "server_id": SERVER_ID,
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "disk_usage": disk_usage,
        "network_sent": network.bytes_sent,
        "network_received": network.bytes_recv,
    }


def send_metrics(metrics):
    try:
        response = requests.post(
            API_URL,
            json=metrics,
            timeout=10,
        )

        if response.status_code == 201:
            print(
                datetime.now().strftime("%H:%M:%S"),
                "Metrics saved successfully:",
                response.json(),
            )
        else:
            print("API error:", response.status_code, response.text)

    except requests.RequestException as error:
        print("Connection error:", error)


if __name__ == "__main__":
    print("CloudPulse Monitoring Agent started")
    print("Monitoring:", socket.gethostname())

    while True:
        metrics = collect_metrics()
        send_metrics(metrics)
        time.sleep(INTERVAL)
