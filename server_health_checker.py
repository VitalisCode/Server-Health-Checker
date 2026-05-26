import psutil #process and system utilities module for monitoring system resources
from datetime import datetime


CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90


def check_cpu():

    cpu_usage = psutil.cpu_percent(interval=1)

    print(f" CPU Usage: {cpu_usage}%")

    if cpu_usage > CPU_THRESHOLD:
        print(" High CPU Usage Alert")


def check_memory():

    memory = psutil.virtual_memory()

    print(f" Memory Usage: {memory.percent}%")

    if memory.percent > MEMORY_THRESHOLD:
        print(" High Memory Usage Alert")


def check_disk():

    disk = psutil.disk_usage('/')

    print(f" Disk Usage: {disk.percent}%")

    if disk.percent > DISK_THRESHOLD:
        print(" High Disk Usage Alert")


def save_log(log_message):

    with open("server_health_logs.txt", "a") as file:
        file.write(log_message + "\n")


def main():

    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    print("=" * 45)
    print("        SERVER HEALTH CHECKER")
    print("=" * 45)

    print(f" Time: {current_time}\n")

    check_cpu()
    check_memory()
    check_disk()

    log_message = (
        f"{current_time} | "
        f"CPU Checked | "
        f"Memory Checked | "
        f"Disk Checked"
    )

    save_log(log_message)

    print("\n Health check saved to log file")


if __name__ == "__main__":
    main()