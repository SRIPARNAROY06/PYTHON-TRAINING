from datetime import date, datetime, timedelta

def estimated_delivery(delivery_date,timeline_days):
    d=datetime.strptime(delivery_date,'%Y-%m-%d')
    return (d+timedelta(days=timeline_days)).date()
print(estimated_delivery("2025-12-05",10))