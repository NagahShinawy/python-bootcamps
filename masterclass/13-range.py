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

START_Q1 = 1
END_Q1 = 3

START_Q2 = 4
END_Q2 = 6

START_Q3 = 7
END_Q3 = 9

START_Q4 = 10
END_Q4 = 12


def month_quarter(month: int):
    if month in range(START_Q1, END_Q1 + 1):
        return QUARTER1
    elif month in range(START_Q2, END_Q2 + 1):
        return QUARTER2

    elif month in range(START_Q3, END_Q3 + 1):
        return QUARTER3

    elif month in range(START_Q4, END_Q4 + 1):
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
