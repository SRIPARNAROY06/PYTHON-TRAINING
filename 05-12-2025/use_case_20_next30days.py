from datetime import datetime, timedelta,date
def next_30_days():
    today=datetime.today()
    return[(today + timedelta(days=i)).date() for i in range(30)]

print(next_30_days())