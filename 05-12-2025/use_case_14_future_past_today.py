from datetime import datetime,date

def check_date(date_str):
    given=datetime.strptime(date_str,"%Y-%m-%d").date()
    today=date.today()

    if given > today:
        return "Future"
    elif given < today:
        return "Past"
    else:
        return "Today"
print(check_date("2025-12-05"))

