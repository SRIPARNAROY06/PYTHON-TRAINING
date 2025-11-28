from datetime import datetime

def log_error(message, log_file="error.log"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] ERROR: {message}\n"


    with open(log_file, "a") as file:
        file.write(log_entry)

    print(f"Logged: {log_entry.strip()}")


for i in range(1, 6):
    log_error(f"Simulated error number {i}")
