# In Python, variables are a symbolic name that is a reference or pointer to an object.
# The variables are used to denote objects by that name


# name is reference, "John" is str obj
name = "John"


# Object Identity
price = 100
price2 = price

print(price == price2)  # True
print(price is price2)  # True

print(id(price) == id(price2))  # True
print("#" * 50)

# ############ ############ ############ ############ ############ ############ ###########


"""
Camel Case: nameOfStudent
Pascal Case: NameOfStudent
Snake Case: name_of_student
"""

# Multiple Assignment

# 1. Assigning single value to multiple variables

row = col = 3

print(row, col)  # 3

# 2. Assigning multiple values to multiple variables:

row, col = 4, 5

print("Row", row)
print("Col", col)


# ############ ############ ############ ############ ############ ############ ###########

# 3- Python Variable Types


# local vars
def calc_sum(number):
    total = 0
    for i in range(number + 1):
        total += i
    return total


print(calc_sum(10))  # 55

# print(total)  # NameError: name 'total' is not defined


# Global Variables

DEV = "develop"  # can be accessed everywhere

# using global keyword

salary = 1000
bonus = 200


def update_salary():
    salary = 5000


def raise_salary():
    global salary
    salary = salary + bonus


update_salary()
print(salary)  # 1000

print(salary)  # 1000
raise_salary()
print(salary)  # 1200
