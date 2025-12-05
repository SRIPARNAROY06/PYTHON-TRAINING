from datetime import datetime,timedelta,date

def leap_year(year):
    return year % 4 == 0 and(year % 100 != 0 or year % 400 == 0)

print(leap_year(2000))
print(leap_year(2024))
print(leap_year(2100))
