from abc import ABC, abstractmethod


class Base(ABC):

    def __init__(self, number: int):
        self.number = number

    @abstractmethod
    def apply(self):
        pass


class Fizz(Base):

    def apply(self):
        return self.number % 3 == 0


class Buzz(Base):

    def apply(self):
        return self.number % 5 == 0


class FizzBuzz(Fizz, Buzz):

    def apply(self):
        return Fizz.apply(self) & Buzz.apply(self)


ACTIONS = [Fizz, Buzz, FizzBuzz]

for i in range(1, 46):
    for action in ACTIONS:
        if action(i).apply():
            print(f"{i} is {action.__name__}")
        else:
            print(f"{i} NO FIZZ, BUZZ, FIZZBUZZ")
            break



