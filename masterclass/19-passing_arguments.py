# oop example: polymorphism, object oriented, abstract, magic methods
from abc import ABC, abstractmethod
import random


class Operation(ABC):

    OPERATOR = ""
    EQUAL = "="

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @abstractmethod
    def apply(self):
        pass


class Add(Operation):

    OPERATOR = "+"

    def apply(self):
        return self.num1 + self.num2


class Sub(Operation):
    OPERATOR = "-"

    def apply(self):
        return self.num1 - self.num2


class Multiply(Operation):
    OPERATOR = "*"

    def apply(self):
        return self.num1 * self.num2


class Divide(Operation):
    OPERATOR = "/"

    ZERO_DIVISION_ERROR = "Can not divide by zero"

    def apply(self):
        if self.num2 == 0:
            return self.ZERO_DIVISION_ERROR
        return self.num1 / self.num2


class IntDiv(Operation):
    OPERATOR = "//"

    def apply(self):
        return self.num1 // self.num2


class Reminder(Operation):

    OPERATOR = "%"

    def apply(self):
        return self.num1 % self.num2


class Number:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    # https://stackoverflow.com/questions/60952972/what-is-the-python3s-magic-method-for-division
    def __truediv__(self, other):
        return self.value / other.value

    def __floordiv__(self, other):
        return self.value // other.value

    # https://www.tutorialsteacher.com/python/magic-methods-in-python
    def __mod__(self, other):
        return self.value % other.value

    def to_int(self):
        return int(self.value)


def get_random_numbers():
    num1 = Number(random.randint(1, 50))
    num2 = Number(random.randint(1, 10))
    return num1, num2


def to_txt(text: str):
    with open("result.txt", "w") as f:
        f.write(text)


def main():
    num1, num2 = get_random_numbers()
    operations = [Add, Sub, Multiply, Divide, IntDiv, Reminder]
    result = ""

    for operation in operations:
        opt = operation(num1, num2)
        result += f"{opt.num1} {opt.OPERATOR} {opt.num2} {opt.EQUAL} {opt.apply()}\n"
        print(result)
        to_txt(result)


if __name__ == "__main__":
    main()
