from datetime import datetime

timestamps=[
    "2025-01-01 10:30:00",
    "2025-01-06 09:00:00",
    "2025-01-13 11:45:00",
]

def count_mondays(ts_list):
    count=0
    for t in ts_list:
        dt=datetime.strptime(t,"%Y-%m-%d %H:%M:%S")
        if dt.weekday()==0:
            count+=1

    return count
print(count_mondays(timestamps))