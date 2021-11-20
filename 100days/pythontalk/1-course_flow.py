# groups
# list of tuples
# slicing
# skip by 3
# dictionary comprehensive
# tuple unpacking
# update method dictionary
# constants

DAY = "Day"

DAYS = range(1, 101, 3)

LAST_END = 97  # 100 - 3

groups = [(day, day + 3) if day == LAST_END else (day, day + 2) for day in DAYS[:-1]]

print(groups)

print(list(DAYS))
map_days = {f"{DAY}#{group[0]}-{group[1]}": list(range(group[0], group[1] + 1)) for group in groups}

print(map_days)

map_days = dict()

for group in groups:
    start, end = group
    duration = f"{DAY}#{start}-{end}"
    days = list(range(start, end + 1))
    map_days.update({duration: days})


print(map_days)