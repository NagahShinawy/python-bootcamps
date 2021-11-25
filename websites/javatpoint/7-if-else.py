# Python If-else statements Decision making
# constants
# if else
# if elif
# inheritance
# polymorphism
# abstract base class (ABC)
# abstract method
# class attributes
# instance attribute
# validate attributes with __setattr__

from abc import ABC, abstractmethod


"""
if expression:
    statement
"""


number = int(input("Number: "))

EVEN = "Even Number"
ODD = "Odd Number"
ELIGIBLE = "You are eligible to vote !!"
NOT_ELIGIBLE = "Sorry! you have to wait !!"

FAILED = "Failed"
PASSED = "Passed"
GOOD = "Good"
VERY_GOOD = "Very Good"
EXCELLENT = "Excellent"


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

# ############## ############## ############## ############## ############## #############

age = 30
UNDERAGE = 18

if age >= UNDERAGE:
    print(ELIGIBLE)
else:
    print(NOT_ELIGIBLE)


def get_degree(mark: int):
    if mark not in range(0, 101):
        raise ValueError("invalid mark")
    if mark in range(0, 50):  # 0 49
        return FAILED
    if mark in range(50, 66):  # 50 - 65
        return PASSED
    if mark in range(66, 76):  # 66 - 75
        return GOOD
    if mark in range(76, 86):  # 76 - 85
        return VERY_GOOD

    return EXCELLENT


class Degree(ABC):

    MIN = 0
    MAX = 100
    GPA_RANGE = range(MIN, MAX + 1)
    PERCENTAGE = "%"
    GPA = "unknown"

    def __init__(self, degree):
        self.degree = degree

    def __str__(self):
        return f"{self.__class__.__name__}({self.degree})"

    def __setattr__(self, key, value):
        if key == "degree":
            if not isinstance(value, (float, int)):
                raise ValueError(f"should be number given {value.__class__.__name__}")
            if value not in self.GPA_RANGE:
                raise ValueError(
                    f"'{self.GPA}' GPA should be from '{self.MIN}' to '{self.MAX}'"
                )

        return super().__setattr__(key, value)

    @property
    def percentage(self):
        return f"{self.degree} %"

    def gpa(self):
        return self.GPA


print(get_degree(100))


class Failed(Degree):
    MIN = 0
    MAX = 49
    GPA_RANGE = range(MIN, MAX + 1)
    GPA = "Failed"


class Passed(Degree):
    MIN = 50
    MAX = 65
    GPA_RANGE = range(MIN, MAX + 1)
    GPA = "Passed"


class Good(Degree):
    MIN = 66
    MAX = 75
    GPA_RANGE = range(MIN, MAX + 1)
    GPA = "Good"


class VeryGood(Degree):
    MIN = 76
    MAX = 85
    GPA_RANGE = range(MIN, MAX + 1)
    GPA = "Very Good"


class Excellent(Degree):
    MIN = 86
    MAX = 100
    GPA_RANGE = range(MIN, MAX + 1)
    GPA = "Excellent"


cs = Good(70)

print(cs)
print(cs.percentage)
