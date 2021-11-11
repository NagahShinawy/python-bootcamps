# https://dev.to/jerrynsh/using-generators-in-python-the-why-the-what-and-the-when-55l
import sys

NUMBERS = range(0, 1_000_000)


# using generator
def get_evens():
    for num in NUMBERS:
        if num % 2 == 0:
            yield num


# using generator
def get_evens2():
    return (num for num in NUMBERS if num % 2 == 0)


# using
def get_evens3():
    return [num for num in NUMBERS if num % 2 == 0]


print("Size of generator", sys.getsizeof(get_evens()))
print("Size of generator", sys.getsizeof(get_evens2()))
print("Size of without generator", sys.getsizeof(get_evens3()))


nums_generator = (i for i in range(1, 100_000_000))

print(sum(nums_generator))
print(sum(nums_generator))  # 0, because it can only be iterated once.
