import psutil # Requires psutil 'pip install psutil'
import time

def monitor_disk_performance(interval=1):
    while True:
        disk_usage = psutil.disk_io_counters()
        read_speed = disk_usage.read_bytes / (1024 * 1024)  # Convert bytes to MB
        write_speed = disk_usage.write_bytes / (1024 * 1024)  # Convert bytes to MB

        print(f"Read Speed: {read_speed:.2f} MB/s\t Write Speed: {write_speed:.2f} MB/s")

        time.sleep(interval)

if __name__ == "__main__":
    monitor_disk_performance()