"""
for iterating_var in sequence:
    statement(s)
"""

# tuple
# lists
# constants
# end in print()
# type hinting

from typing import Union


BONUS = 0.3

DEPENDENCY_RELATION = ("son", "daughter", "father", "mother", "husband", "wife")

GENDER = ("male", "female")

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
