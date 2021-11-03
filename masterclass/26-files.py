from prettytable import PrettyTable

COLS = ("Name", "Age", "Job")
info: PrettyTable = PrettyTable()
info.field_names = COLS


with open("info.txt") as f:
    lines = [line.strip() for line in f.readlines()]


row = []

for ln in lines:
    _, value = ln.split(":")
    row.append(value)

info.add_row(row)

print(info)