"""
A list in Python is used to store the sequence of various types of data
Python lists are mutable type its mean we can modify its element after it created.
However, Python consists of six data-types that are capable to store the sequences
but the most common and reliable type is the list.
"""

"""
The list has the following characteristics:

1- The lists are ordered.
2- The element of the list can access by index.
3- The lists are the mutable type.
4- The lists are mutable types.
5- A list can store the number of various elements.
"""

# bad data structure
user_data = [
    "John",  # username
    "John",  # first name
    "Loen",  # last name
    23,  # age
    False,  # is_married
]

numbers1 = [3, 4, 6]
numbers2 = [3, 4, 6]

print(numbers1 == numbers2)  # True

print(numbers1 is numbers2)  # False because lists are mutable


# ############ ############ ############ ############ ############ ############ ############ ###########

# Both lists have consisted of the same elements,
# but the second list changed the index position of the 5th element that violates the order of lists.
# When compare both lists it returns the false.

# Lists maintain the order of the element for the lifetime. That's why it is the ordered collection of objects.
a = [1, 2, "Peter", 4.50, "Ricky", 5, 6]
b = [1, 2, 5, "Peter", 4.50, "Ricky", 6]

print(a == b)
