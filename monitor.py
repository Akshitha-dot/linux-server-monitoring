import time
import shutil
import os


def get_cpu_usage():
    load = os.getloadavg()[0]
    cpu_count = os.cpu_count() or 1
    return (load / cpu_count) * 100


def get_disk_usage():
    total, used, free = shutil.disk_usage("/")
    return (used / total) * 100


print("===== LINUX SERVER MONITORING =====")

while True:
    cpu = get_cpu_usage()
    disk = get_disk_usage()

    print(f"CPU Usage: {cpu:.2f}%")
    print(f"Disk Usage: {disk:.2f}%")
    print("-" * 40)

    time.sleep(5)
