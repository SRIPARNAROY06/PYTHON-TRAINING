from datetime import datetime

dates=["2025-01-10","2024-12-25"]

def sort_dates(date_list):
    dt_list=[datetime.strptime(d, "%Y-%m-%d") for d in date_list]
    dt_list.sort()
    return dt_list

sorted_dates=sort_dates(dates)
for d in sorted_dates:
    print(d.date())