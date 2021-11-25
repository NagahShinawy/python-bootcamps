"""
for iterating_var in sequence:
    statement(s)
"""

# tuple
# lists
# constants
# end in print()
# type hinting
# range func
# range
# pyramid
# else with loop
# else with for
# else with break of loop


from typing import Union


BONUS = 0.3

DEPENDENCY_RELATION = ("son", "daughter", "father", "mother", "husband", "wife")

GENDER = ("male", "female")
ADULTHOOD_AGE = 18
PRIMARY_SCHOOL_AGES = [7, 10]  # surveys needed only for these ages
SECONDARY_SCHOOL_AGES = [13, 16]  # surveys needed only for these ages
SCHOOL_AGES = range(6, 18)  # list all school ages, used for testing


ALLOWED_BLOOD_TYPES = ("A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-")

PROFILE_EMPLOYMENT = ("employee", "unemployed", "part time employee", "retired")
# ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ######

username = "John"

for char in username:
    print(char)


# ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ######
print("#" * 50)


username = "James"

for char in username:
    print(char, end=" ")


print("")


def calc_bonus(sal):
    return sal * BONUS


salaries = [4000, 6000, 3000, 1000, 1200]

print("Before \t After")
for salary in salaries:
    total = salary + calc_bonus(salary)
    print(f"{salary} \t {calc_bonus(salary)}")


def calc_sum(items: Union[list, tuple]):
    totl = 0
    for item in items:
        totl += item

    return totl


print(calc_sum([6, 3, 1]))  #
print(calc_sum((5, 4)))

# ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ######
print("#" * 50)


# range(start,stop,step size)

# EVENS FROM 0 TO 10

for number in range(0, 11, 2):
    print(number)


for number in range(0, 11):
    print(number, end=" ")


# Example - 2: Program to print table of given number.
#

print("")
n = int(input("Enter the number "))
for i in range(1, 11):
    c = n * i
    print(f"{i} * {n} = {c}")


# pyramids problem

# Example- 1: Nested for loop

for i in range(1, 6):
    for _ in range(i):
        print("*", end="")
    print()


# Example-2: Program to number pyramid.

for i in range(1, 6):
    for _ in range(i):
        print(i, end="")

    print()


"""
Using else statement with for loop
Unlike other languages like C, C++, or Java,
Python allows us to use the else statement with the for loop which can be executed only
when all the iterations are exhausted.
Here, we must notice that if the loop contains any of the break statement then the else statement will not be executed.
"""

for i in range(5):
    print(i, end=" ")
    if i == 4:
        print()
        # break  # if you type break else block will NOT executed
else:
    print("completed!")
