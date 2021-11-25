# Python If-else statements Decision making
# constants

"""
if expression:
    statement
"""


number = int(input("Number: "))

EVEN = "Even Number"
ODD = "Odd Number"

JAN = 1

MONTHS = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "June",
    7: "July",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec",
}


def to_month(month):
    return MONTHS[month]


def is_even(num):
    return num % 2 == 0


def next_month(month: int):
    if month not in range(1, 13):
        raise ValueError

    if month == 12:
        month = 1
    else:
        month += 1
    return to_month(month)


print(next_month(12))
print(next_month(3))


if is_even(number):
    print(EVEN)

else:
    print(ODD)


# find largest number of three numbers

a = 10
b = 10
c = 10

if a > b and a > c:
    print("A")

elif b > a and b > c:
    print("B")

elif c > b and c > a:
    print("C")

elif a == b == c:
    print("All the same")