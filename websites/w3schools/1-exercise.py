# https://www.w3schools.com/python/exercise.asp

# Syntax  # DONE
# Comments  # DONE
# Variables  # DONE
# Data Types  # DONE
# Numbers  # DONE
# Strings  # DONE
# Booleans  # DONE
# Operators  # DONE
# Lists  # DONE
# Tuples  # DONE
# sets  # DONE
# Dictionary
# if else
# while
# for
# function
# lambda
# classes
# Inheritance
# modules


fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]

fruits.update(more_fruits)

print(fruits)


"""
discard
Remove an element from a set if it is a member.
        
If the element is not a member, do nothing.
"""

fruits.discard("banana")

print(fruits)

print("#" * 100)


car = {"model": "BMW", "year": 2020, "price": "120K"}

print(car)

car.clear()
print(car)
