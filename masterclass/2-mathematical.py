# ** means power
print(2 ** 3)  # 8
print(2 ** 4)  # 16

print(pow(2, 4))  # 16

sqr = 49 ** 0.5
print(sqr)  # 7.0


print(20 / 4)  # 5.0  float

print(20 // 4)  # 5 int


# reminder

print(36 % 30)  # 6

is_even = 40 % 2 == 0
print(is_even)  # True

print(7 % (5 // 2))  # 1.0


class Counter:

    RESET_VALUE = 0

    def __init__(self, value=0):
        self.value = value

    @property
    def is_even(self) -> bool:
        return self.value % 2 == 0

    @property
    def is_odd(self) -> bool:
        return not self.is_even

    @property
    def next(self) -> int:
        return self.value + 1

    @property
    def prev(self) -> int:
        return self.RESET_VALUE if self.value < 1 else self.value - 1

    @property
    def next_3(self) -> list:
        return [self.next, self.next + 1, self.next + 2]

    @property
    def reset(self) -> int:
        self.value = self.RESET_VALUE
        return self.value


counter = Counter(value=20)

print(counter.is_odd)
print(counter.is_even)

print(counter.prev)
print(counter.prev)

print(counter.next_3)
print(counter.reset)
