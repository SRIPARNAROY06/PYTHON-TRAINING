from datetime import datetime,timedelta
def count_weekdays(start_date,end_date):
    start=datetime.strptime(start_date,'%Y-%m-%d')
    end=datetime.strptime(end_date,'%Y-%m-%d')

    ct=0
    current=start
    while current<=end:
        if current.weekday()<5:
            ct+=1
        current+=timedelta(days=1)

    return ct
print(count_weekdays("2025-01-01","2025-01-10"))