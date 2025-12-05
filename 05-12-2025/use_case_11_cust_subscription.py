from datetime import datetime, timedelta, date

start_date=date(2025,12,4)
duration_days=30


expiry_date=start_date+timedelta(days=duration_days)
print(start_date)
print(expiry_date)
