import datetime
def mark_attendance():
    while True:
        name=input("Enter student name: ")
        if name.lower()=="done":
            print("Attendance recorded")
            break

        status=input(f"Status for {name} (Present/Absent): ")

        timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open ("attendance.txt","a") as f:
            f.write(f"{timestamp}\t{name}\t{status}\n")

        print("Entry added \n")

mark_attendance()
