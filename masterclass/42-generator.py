TEN_SECONDS = 10
NUMBERS = 100
# call function to get value ba value


def timer():
    count = 1
    while count <= TEN_SECONDS:
        yield count  # get count and pause func, then resume func again from this point [yield point]
        count += 1


def evens():
    for num in range(NUMBERS):
        if num % 2 == 0:
            yield num


seconds = timer()
print(seconds)  # <generator object timer at 0x000001E3E18CEC48>

for second in seconds:
    print(second, end=" | ")

print()
print("#" * 100)
evns = evens()

for even in evns:
    print(even, end=" | ")
