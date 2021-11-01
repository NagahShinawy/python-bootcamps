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