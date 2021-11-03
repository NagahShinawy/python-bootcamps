from prettytable import PrettyTable

COLS = ("Name", "Age", "Job", "Experience")
info: PrettyTable = PrettyTable()
info.field_names = COLS


with open("info.txt") as f:
    lines = [line.strip() for line in f.readlines() if line]


row = []

for ln in lines:
    if ln:
        _, value = ln.split(":")
        row.append(value)

info.add_row(row)

print(info)

print("#" * 50)

with open("info.txt", "r") as f:
    ln = f.readline()
    print(ln, type(ln))  # read just single line  ==> str


print("#" * 50)

with open("info.txt", "r") as f:
    content = f.read()
    print(content, type(content))  # read all content as single string  ==> str

print("#" * 50)

with open("info.txt", "r") as f:
    content = f.read(6)  # how many characters you want to return
    print(content, len(content))

print("#" * 50)

with open("info.txt", "a") as f:
    f.write("\nexp:+5")


# w mode replace all content with new content you write
with open("info.txt", "w") as f:
    f.write("test")