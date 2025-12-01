
from datetime import datetime

def append_log(filename, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, 'a') as f:
        f.write(f"[{timestamp}] {message}\n")


append_log("log.txt", "This is a log entry")
