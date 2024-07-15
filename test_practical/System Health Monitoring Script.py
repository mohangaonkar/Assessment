# 1. System Health Monitoring Script:
# Develop a script that monitors the health of a Linux system. It should check
# CPU usage, memory usage, disk space, and running processes. If any of
# these metrics exceed predefined thresholds (e.g., CPU usage > 80%), the
# script should send an alert to the console or a log file.

import psutil
import datetime

# Define thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

# Check for CPU usage
def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"Current CPU Usage: {cpu_usage}%")

    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"CPU usage exceeds threshold ({CPU_THRESHOLD}%): {cpu_usage}%")

# Check for memory usage
def check_memory():
    memory_usage = psutil.virtual_memory().percent
    print(f"Current Memory Usage: {memory_usage}%")

    if memory_usage > MEMORY_THRESHOLD:
        log_alert(f"Memory usage exceeds threshold ({MEMORY_THRESHOLD}%): {memory_usage}%")

# check for check disk usage
def check_disk():
    disk_usage = psutil.disk_usage('/').percent
    print(f"Current Disk Usage: {disk_usage}%")

    if disk_usage > DISK_THRESHOLD:
        log_alert(f"Disk usage exceeds threshold ({DISK_THRESHOLD}%): {disk_usage}%")

# Check for running processes
def check_processes():
    running_processes = len(psutil.pids())
    print(f"Total Running Processes: {running_processes}")
    # You can define thresholds for processes if needed

# Log alerts to file
def log_alert(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("system_health_alert.log", "a") as f:
        f.write(f"[{timestamp}] {message}\n")

# Main function
def main():
    print("Starting system health monitoring...")

    check_cpu()
    check_memory()
    check_disk()
    check_processes()

    print("System health check completed.")

if __name__ == "__main__":
    main()
