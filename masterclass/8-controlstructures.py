ADULT = 18

MAX_AGE = 120


def is_under_age(age: int):
    return age < ADULT


def is_adult(age):
    return ADULT <= age <= MAX_AGE


def main():
    age = input("Please enter your age: ")

    if is_under_age(int(age)):
        print("You are not allowed to register. Only Adults")

    if is_adult(int(age)):
        print("You can register!")

    else:
        print("Max value of age is not allowed")


main()


