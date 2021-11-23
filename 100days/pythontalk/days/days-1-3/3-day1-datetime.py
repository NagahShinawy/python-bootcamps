from datetime import datetime
from datetime import date

# 1- using timedelta
# 2- get differences between 2 days objs
# 3- convert from days to months
# 4- create date obj
# 5- match 2 date objs
# 6- using constants
# 7- using keyword argument with format method


# get current today date

# 1- using datetime
today = datetime.today()

CELEBRATE = "let's celebrate !"
WAITING_TO_CHRISTMAS = "Sorry, there are still [{days}] days to christmas"

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

print("#" * 100)

CHRISTMAS = date(2021, 12, 25)

print(CHRISTMAS)
print(CHRISTMAS.year)
print(CHRISTMAS.month)
print(CHRISTMAS.day)

print(type(CHRISTMAS))  # <class 'datetime.date'>

remaining_to_christmas = CHRISTMAS - today

print(remaining_to_christmas.days)


# convert from days to month
# how many months and days in int(day)
def from_days_to_months(days: int):
    months = days // 30
    remaining_days = days % 30
    return months, remaining_days


remaining = remaining_to_christmas.days
print(from_days_to_months(remaining))

mnths, dys = from_days_to_months(remaining)

print(f"You have {remaining} days [{mnths} months(s) {dys} day(s)]")

# ########### ########### ########### ########### ########### ########### ########### ##########

print(type(remaining_to_christmas))  # <class 'datetime.timedelta'>

print(remaining_to_christmas.days)

print(remaining_to_christmas.total_seconds())


CHRISTMAS = date(2021, 11, 25)

print(id(CHRISTMAS))
print(id(today))


if CHRISTMAS == today:
    print(CELEBRATE)

else:
    print(WAITING_TO_CHRISTMAS.format(days=(CHRISTMAS - today).days))
