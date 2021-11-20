# groups
# list of tuples
# slicing
# skip by 3

DAY = "Day"

DAYS = range(1, 101, 3)

LAST_END = 97  # 100 - 3

groups = [(day, day + 3) if day == LAST_END else (day, day + 2) for day in DAYS[:-1]]

print(groups)

print(list(DAYS))
