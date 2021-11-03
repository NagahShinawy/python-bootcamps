from abc import ABC, abstractmethod


class Operation(ABC):

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @abstractmethod
    def apply(self):
        pass


class Add(Operation):

    def apply(self):
        return self.num1 + self.num2


class Sub(Operation):

    def apply(self):
        return self.num1 - self.num2


class Multiply(Operation):

    def apply(self):
        return self.num1 * self.num2


class Divide(Operation):
    ZERO_DIVISION_ERROR = "Can not divide by zero"

    def apply(self):
        if self.num2 == 0:
            return self.ZERO_DIVISION_ERROR
        return self.num1 + self.num2


def main():
    operations = [Add, Sub, Multiply, Divide]

    num1 = 15
    num2 = 3

    for operation in operations:
        opr = operation(num1, num2)
        print(f"{opr.__class__.__name__} --> {opr.apply()}")


if __name__ == '__main__':
    main()




