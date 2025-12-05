from datetime import datetime,timedelta,date

def calculate_age(dob):
    dob=datetime.strptime(dob,'%Y-%m-%d').date()
    today=date.today()

    years=today.year-dob.year
    months=today.month-dob.month
    days=today.day-dob.day

    if days<0:
        months-=1
        prev_month=today.month-1 or 12
        prev_year=today.year if today.month!=1 else today.year-1
        days+=(date(prev_year,prev_month,1).replace(day=28)+timedelta(days=4)).day

    if months<0:
        years-=1
        months+=12

    return years,months,days

print(calculate_age("2003-01-06"))
