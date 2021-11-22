from datetime import datetime, timedelta, date

# create timedelta obj
# convert from seconds to hours
# convert from seconds to minutes
# get diff between 2 dates objs
# convert from date obj to str using strftime ==> datetimeObj.strftime(YOUR CUSTOM FORMAT)
# get next month from today
# add 2 dates objs [python use magic methods to implement that]

SLEEP_TIME = 5


weeding = timedelta(days=5, hours=10)

print(type(weeding))  # <class 'datetime.timedelta'>

print(weeding.days)  # 5
print(weeding.seconds)  # 36000 = 10 hours

# ERROR
# print(
#     weeding.hours
# )  # AttributeError: 'datetime.timedelta' object has no attribute 'hours'


def seconds_to_minutes(secs: int):
    return secs / 60


def seconds_to_hours(secs: int):
    return secs / 60 / 60


seconds = weeding.seconds
hours = (seconds + 12) / 60 / 60
print(hours)  # 10.0

print(seconds_to_minutes(seconds))  # 600.0

today = datetime.today()

SLEEP = timedelta(
    hours=SLEEP_TIME
)  # datetime.timedelta(seconds=18000)  18000 is 5 hours


print(today - SLEEP)  # 5 hours before current datetime, 5 is SLEEP_TIME

BEFORE_WEEK = 7

week = timedelta(days=BEFORE_WEEK)

print(today)  # 2021-11-20 12:41:26.748156   # today
print(today - week)  # 2021-11-13 12:41:26.748156  ==> week before

week_before = today - week

print(type(week_before))  # <class 'datetime.datetime'>

print(week_before.strftime("%d-%b-%Y %H:%M:%S"))


# ################################################ ##################################################
print("#" * 50)

MONTH_DAYS = 30

next_month = today + timedelta(days=MONTH_DAYS)

print(today)
print(next_month)


# ################################################ ##################################################

print("#" * 50)
DAYS_IN_YEAR = 365
next_year = today + timedelta(days=DAYS_IN_YEAR)

print(today)  # 2021-11-20 12:52:40.003728
print(next_year)  # 2022-11-20 12:52:40.003728

# ################################################ ##################################################
print("#" * 50)

WEEK = 7  # days

HOURS_THREE_DAYS = 3 * 24

print(today)  # 2021-11-20 13:03:23.199853

# after 10 days
print(
    today + timedelta(days=WEEK, hours=HOURS_THREE_DAYS)
)  # 2021-11-30 13:03:23.199853


# validate till 25 days

VALIDATE_DAYS = 25

today = date(year=2021, month=10, day=4)
wrong_date = date(year=2021, month=12, day=3)
next_25_days = today + timedelta(days=VALIDATE_DAYS)

print(next_25_days)  # 2021-10-29

days = wrong_date - today

print(days)

print(today + timedelta(days=21) + timedelta(days=21) + timedelta(days=18))
