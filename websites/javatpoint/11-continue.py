# continue: means skip current iteration


# skips evens

for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(number)


# remove invalid chars

movie = "inception:/\ ?.mp4"

INVALID_CHARS = ':?/\\<>*"'


def get_valid_pathname(name: str):
    result = ""
    for char in name:
        if char in INVALID_CHARS:
            continue
        result += char

    return result


print(movie)
print(get_valid_pathname(movie))
