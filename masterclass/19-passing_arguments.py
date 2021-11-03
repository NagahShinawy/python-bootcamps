# oop example: polymorphism, object oriented, abstract
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


def get_random_numbers():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 10)
    return num1, num2


def to_txt(text: str):
    with open("result.txt", "w") as f:
        f.write(text)


def main():
    operations = [Add, Sub, Multiply, Divide]
    result = ""

    for operation in operations:
        num1, num2 = get_random_numbers()
        opr = operation(num1, num2)
        result += f"{opr.num1} {opr.OPERATOR} {opr.num2} {opr.EQUAL} {opr.apply()}\n"
        print(result)
        to_txt(result)


if __name__ == '__main__':
    main()




