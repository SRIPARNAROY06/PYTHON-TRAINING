from datetime import datetime

log_file = "logfile.txt"

entry = input("Enter log message: ")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(log_file, "a") as f:
    f.write(f"[{timestamp}] {entry}\n")

print("Log entry added.")
