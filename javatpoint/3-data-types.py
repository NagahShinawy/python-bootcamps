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
