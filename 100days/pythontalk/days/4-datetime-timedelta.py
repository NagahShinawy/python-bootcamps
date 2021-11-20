from datetime import datetime, timedelta

# create timedelta obj
# convert from seconds to hours
# convert from seconds to minutes
# get diff between 2 dates objs
# convert from date obj to str using strftime ==> datetimeObj.strftime(YOUR CUSTOM FORMAT)
# get next month from today

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
