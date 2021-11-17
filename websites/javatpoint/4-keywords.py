"""
Python Keywords are special reserved words that convey a special meaning to the compiler/interpreter. Each keyword has a special meaning and a specific operation.
These keywords can't be used as a variable. Following is the List of Python Keywords.
"""

"""
1- True - It represents the Boolean true,
if the given condition is true, then it returns "True". Non-zero values are treated as true.

2- False - It represents the Boolean false; if the given condition is false
then it returns "False". Zero value is treated as false

3- None - It denotes(يدل) the null value or void. An empty list or Zero can't be treated as None.

4- and - It is a logical operator. It is used to check the multiple conditions.
It returns true if both conditions are true. Consider the following truth table.


5. or - It is a logical operator in Python.
It returns true if one of the conditions is true. Consider the following truth table.

6- 6. not - It is a logical operator and inverts the truth value. Consider the following truth table.

10. continue - It is used to stop the execution of the current iteration. Consider the following example.

"""


def skip_odd(numbers):
    for number in range(0, numbers + 1):
        if number % 2 != 0:
            continue
        print(number)


def find_member(member, members):
    for obj in members:
        if obj == member:
            break
        print(obj)


skip_odd(12)

print("#" * 100)

NAMES = ["John", "Loen", "James", "Adam", "Angela", "Smith"]
ADAM = "Adam"

find_member(ADAM, NAMES)