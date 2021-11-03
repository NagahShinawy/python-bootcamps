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

    def __init__(self, val=0):
        self.val = val

    @property
    def is_even(self) -> bool:
        return self.val % 2 == 0

    @property
    def is_odd(self) -> bool:
        return not self.is_even

    @property
    def next(self) -> int:
        return self.val + 1

    @property
    def prev(self) -> int:
        return self.RESET_VALUE if self.val < 1 else self.val - 1

    @property
    def next_3(self) -> list:
        return [self.next, self.next + 1, self.next + 2]

    @property
    def reset(self) -> int:
        self.val = self.RESET_VALUE
        return self.val

    def __setattr__(self, key, value):
        if key == "val":
            if not isinstance(value, (int, float)):
                raise TypeError(
                    f"number must be valid int, float given '{value.__class__.__name__}'"
                )
            if value < 0:
                raise ValueError(f"number must be positive value give '{value}'")
        return super().__setattr__(key, value)


counter = Counter(val=20)

print(counter.is_odd)
print(counter.is_even)

print(counter.prev)
print(counter.prev)

print(counter.next_3)
print(counter.reset)


c = Counter(val=-1)
