from datetime import datetime
from datetime import date

# get current today date

# 1- using datetime
today = datetime.today()

print(today)  # 2021-11-20 11:04:41.458327
print(
    type(today)  # <class 'datetime.datetime'>
)  # TypeError: descriptor 'date' of 'datetime.datetime' object needs an argument
# print(datetime.date())


print(today.date())  # 2021-11-20


# 2- using date
print(date.today())  # 2021-11-20

today = date.today()

month = today.month
print(month)  # 11

day = today.day
print(day)

year = today.year

print(year)
