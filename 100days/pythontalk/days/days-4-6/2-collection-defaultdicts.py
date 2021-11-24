import random
from collections import defaultdict


# I guess you are all too familiar with KeyError when using a dict, no?


# https://www.geeksforgeeks.org/defaultdict-in-python/
"""
Defaultdict is a container like dictionaries present in the module collections.
Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object.
The functionality of both dictionaries and defualtdict are almost same except for the fact that
defualtdict never raises a KeyError. It provides a default value for the key that does not exists
"""
profile = {
    "username": "test",
    "email": "test@test.com",
    "dob": "2000-01-01",
}

# print(profile["address"])  # KeyError: 'address'

print(profile.get("address"))  # None
print(
    profile.get("address", False)
)  # False ==> value to return in case of key does not exists at dictionary

race = [
    ("james", 10),
    ("loen", 19),
    ("adam", 20),
    ("james", 13),
    ("loen", 17),
    ("adam", 30),
]

challenges = dict()

for name, mark in race:
    challenges[name] = mark


# No duplicated keys, Just take care of last updated key-value
# last updated value for key 'james' = 13
# last updated value for key 'loen' = 17
# last updated value for key 'adam' = 30

print(challenges)  # {'james': 13, 'loen': 17, 'adam': 30}


# ###################### ###################### ###################### ###################### #####################

# defaultdict

# Syntax: defaultdict(default_factory)

# default_factory: A function returning the default value for the dictionary defined.
# If this argument is absent then the dictionary raises a KeyError.


def empty():
    return ""


profile = defaultdict(empty)

profile["username"] = "Adam"
profile["dob"] = "2000-01-01"

print(
    profile
)  # defaultdict(<function empty at 0x000001EB809E24C8>, {'username': 'Adam', 'dob': '2000-01-01'})


print(profile["username"])  # Adam
print(profile["dob"])  # 2000-01-01
print(
    profile["email"]
)  # ''   ==> never raise Keyerror, it just return default value ==> ''


city = defaultdict(lambda: None)

city.update({"name": "Cairo", "location": "Africa"})

print(city["population"])  # None
print(
    city
)  # defaultdict(<function <lambda> at 0x000002C41EF52948>, {'name': 'Cairo', 'location': 'Africa'})


print(type(city))  # <class 'collections.defaultdict'>

# ###################### ###################### ###################### ###################### #####################


# how does it work ?

"""
__missing__(): This function is used to provide the default value for the dictionary.
This function takes default_factory as an argument and if this argument is None,
a KeyError is raised otherwise it provides a default value for the given key.
This method is basically called by the __getitem__() method of the dict class when the requested key is not found.
__getitem__() raises or return the value returned by the __missing__(). method
"""

item = defaultdict(lambda: "Not Found")

item["name"] = "Phone"
item["price"] = "300$"

print(item["seller"])  # Not Found


# means value in case of missing
print(item.__missing__("name"))  # Not Found  ==> name key is EXIST at item dict
# but 'Not Found' the value in case of missing keys

print(item.__missing__("price"))  # Not Found
print(item.__missing__("seller"))  # Not Found


# ###################### ###################### ###################### ###################### #####################


# default_factory=None is missing so, KeyError will raise for keys does not exist
car = defaultdict()

car["model"] = "BMW"

print(car["model"])

# print(car["price"])  # KeyError: 'price'  ==> BECAUSE YOU DOES NOT ASSIGN DEFAULT_FACTORY

# ###################### ###################### ###################### ###################### #####################

"""
Using List as default_factory
When the list class is passed as the default_factory argument
then a defaultdict is created with the values that are list.
"""


col = defaultdict(list)  # means default value (default_factory) for missing keys is []

print(col["name"])  # []
print(col["age"])

print(col)  # defaultdict(<class 'list'>, {'name': [], 'age': []})


# ################## ################## ################## ################## ################## #################


questions = (
    "Java or PHP?",
    "Laravel or Zend?",
    "Django or Flask?",
    "React or Vue",
    "Boostrap or foundation?",
)

answers = defaultdict(list)  # default value for keys is list obj


# defaultdict(<class 'list'>,
# {'Java or PHP?': ['Java ', ' PHP'], 'Laravel or Zend?': ['Laravel ', ' Zend'],
# 'Django or Flask?': ['Django ', ' Flask'], 'React or Vue?': ['React ', ' Vue'],
# 'Boostrap or foundation?': ['Boostrap ', ' foundation']})

for question in questions:
    first_answer, second_answer = question.split("or")
    if second_answer.endswith("?"):
        second_answer = second_answer[:-1]
    answers[question].extend([first_answer, second_answer])


print(answers)
print(answers[questions[0]])
print(answers[questions[3]])


# ################## ################## ################## ################## ################## #################

# Using int as default_factory
# When the int class is passed as the default_factory argument,
# then a defaultdict is created with default value as zero.

BONUS = 3

emps = ["james", "john", "adam", "loen", "angela"]
salaries = defaultdict(int)  # default values is int ==> 0

print(salaries["test"])  # 0

for emp in emps:
    salary = random.randint(1, 10)
    salaries[emp] = salary + BONUS


print(salaries)
print(salaries["james"])
print(salaries["john"])


print("#" * 100)

doubles = defaultdict(int)

numbers = range(1, 11)

for number in numbers:
    doubles[number] = number * 2

print(
    doubles
)  # defaultdict(<class 'int'>, {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20})
