from typing import Union

userid = 12  # int
name = "Loen"  # str
salary = 1000.4  # float
is_male = True  # boolean

# ################ ################ ################ ################ ################ ###############
print(userid, type(userid))
print(name, type(name))
print(salary, type(salary))
print(is_male, type(is_male))


# ################ ################ ################ ################ ################ ###############

# Standard data types: LOOK IMAGE

# numbers:

# int, float, complex

x = 1 + 3j
print(f"X = {x} is {type(x)} data type")

print(isinstance(x, complex))  # True


# lists

items = [4, 5.6, "test", False]

print(items * 2)  # [4, 5.6, 'test', False, 4, 5.6, 'test', False]


def clean(items: Union[list, tuple]):
    return [item for item in items if item]


print(clean(items))


# tuple:  is a read-only data structure as we can't modify the size and value of the items of a tuple


# concatenate tuples

print(("red", "green") + ("blue", "white"))  # ('red', 'green', 'blue', 'white')

STATUS = ("Pending", "Approved", "Canceled")

# Error
# STATUS[0] = "PENDING"  # TypeError: 'tuple' object does not support item assignment

# ################ ################ ################ ################ ################ ###############

# Dictionary

author = {
    "name": "John",
    "books": [
        {"title": "clean code", "price": 100},
        {"title": "python for all", "price": 60},
        {"title": "django for web apps", "price": 80},
    ],
    "work_history": ["IBM", "Amazon", "Google", "Microsoft"],
}

print("Name", author["name"])
print("clean code", author["books"][0])
print("python for all", author["books"][1])
print("django for web apps", author["books"][2])

print("Work History", author["work_history"])


# Boolean
# ################ ################ ################ ################ ################ ###############

is_active = True

print(is_active, type(is_active))

# ################ ################ ################ ################ ################ ###############

# Python Set is the unordered collection of the data type.
# It is iterable, mutable(can modify after creation), and has unique elements.

emps = {
    "john": 1200,
    "loen": 1500,
    "james": 1200,
    "adam": 1400,
    "smith": 1400,
    "angela": 1600,
}


# set comprehension
salaries = {salary for salary in emps.values()}


print(salaries)

# set Error
# print(salary[0]) TypeError: 'float' object is not subscriptable

print(salaries)

# set methods

# 1- remove

salaries.remove(1200)

print(salaries)

# 2- add

salaries.add(1800)

print(salaries)
