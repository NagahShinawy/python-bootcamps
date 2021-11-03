def to_int(value: str):
    try:
        num = int(value)

    except (ValueError, TypeError):
        return False
    else:
        return num


def values_to_int(*args):
    return (to_int(value) for value in args)


number = to_int("-7")
number2 = to_int("test")


if number is not False:
    print(number + 10)


if number2 is not False:
    print(number2)

else:
    print("Not valid number")

numbers = values_to_int("45", "40", "30", "test")
print(
    numbers
)  # <generator object values_to_int.<locals>.<genexpr> at 0x000001FB8FCE1A48>
for val in numbers:
    print(val, type(val))
