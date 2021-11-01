numbers = range(10)

print(numbers)
print(list(numbers))

evens = range(0, 11, 2)

print(evens)
print(list(evens))


QUARTER1 = "Q1"
QUARTER2 = "Q2"
QUARTER3 = "Q3"
QUARTER4 = "Q4"

QUARTERS = [QUARTER1, QUARTER2, QUARTER3, QUARTER4]


def month_quarter(month: int):
    if month in range(1, 4):
        return QUARTER1
    elif month in range(4, 7):
        return QUARTER2

    elif month in range(7, 10):
        return QUARTER3

    elif month in range(10, 13):
        return QUARTER4
    else:
        raise ValueError("invalid month")


print(month_quarter(9))

numbers = range(0, 31, 3)
by_5 = range(0, 101, 5)

print(list(numbers))  # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

print(
    list(by_5)
)  # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
