# groups
# list of tuples
# slicing
# skip by 3
# dictionary comprehensive
# tuple unpacking
# update method dictionary
# constants
# format method
# using os to create folders
# mkdir

import os


DAY = "Day"
DURATION = "Day {start}-{end}"
DAYS = range(1, 101, 3)

END = 97  # 100 - 3

groups = [(day, day + 3) if day == END else (day, day + 2) for day in DAYS[:-1]]

print(groups)

print(list(DAYS))
map_days = {
    f"{DAY}#{group[0]}-{group[1]}": list(range(group[0], group[1] + 1))
    for group in groups
}

print(map_days)

map_days = dict()

for group in groups:
    start, end = group
    # duration = f"{DAY}#{start}-{end}"
    duration = DURATION.format(start=start, end=end)
    days = list(range(start, end + 1))
    map_days.update({duration: days})


print(map_days)


def create_day(day):
    os.mkdir(day)


for group in groups:
    start, end = group
    duration = f"days-{start}-{end}"
    create_day(duration)
