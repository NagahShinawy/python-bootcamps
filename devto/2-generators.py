import sys


# https://dev.to/jerrynsh/using-generators-in-python-the-why-the-what-and-the-when-55l

# todo 1 : what is Generators?
# using generators when dealing with large datasets with memory constraints

"""
using generators when dealing with large datasets with memory constraints
Consider using Generator when dealing with a huge dataset
Consider using Generator in scenarios where we do not need to reiterate it more than once
Generators give us lazy evaluation
They are a great way to generate sequences in a memory-efficient manner
"""

# todo 2: What Is a Generator Function ?
"""
1- a Generator function is a special kind of function that returns many items.
2- The point here is that the items are returned ONE BY ONE RATHER THAN ALL AT ONCE
3- The main difference between a regular function and a Generator function lies
in the use of return and yield statements in Python.
"""

# todo 3: Generators give you lazy evaluation
"""
1- Behind the scene, Generators don’t compute the value of each item when being instantiated.
Rather, they compute it when we ask for it. This is what people mean by Generators give you lazy evaluation.

2- As a result,
Generators allow us to PROCESS AND DEAL WITH ONE VALUE AT A TIME WITHOUT HAVING TO LOAD EVERYTHING IN MEMORY FIRST.
"""

# todo 4: When and Where Should I Use Generators?
"""
1- Generators are great when you encounter problems that require you to READ FROM A LARGE DATASET.
2- Reading from a large dataset means our computer or server would have to allocate memory for it.
3- The only condition to remember is that a Generator can only be iterated ONCE.
4- as long as we do not need the previous value from our dataset, we can always use Generator
"""


"""
regular func 'read_csv_from_regular_fn' open our CSV file and loads everything in memory in an INSTANCE
Generator opens our large CSV file, loops through every row, and YIELDS EACH ROW AT A TIME RATHER THAN ALL AT ONCE
"""

# todo 4: When NOT To Use Generators ?
"""
1- We need the previous values

A Generator can only be iterated once.
The example below shows that the Generator expression from nums_generator can only be iterated once.
Using sum on it for the second time resulted in zero as the Generator was exhausted.


2- Dealing with relatively small files
"""
NUMBERS = range(0, 100_000_000)


# using generator
def get_evens():
    for num in NUMBERS:
        if num % 2 == 0:
            yield num


# using generator
def get_evens2():
    return (num for num in NUMBERS if num % 2 == 0)


# using
def get_evens3():
    return [num for num in NUMBERS if num % 2 == 0]


print("Size of generator", sys.getsizeof(get_evens()))
print("Size of generator", sys.getsizeof(get_evens2()))
print("Size of without generator", sys.getsizeof(get_evens3()))


"""
Like list comprehensions
the Generator expression allows us to quickly create a Generator object without having to use the yield statement.
"""

"""
1- using list comprehensions
In Example 1, i ** i for the entire range of 100_000_000 is being evaluated and stored in memory beforehand.
It returns a full list.

2- using generator
In Example 2, i ** i is only evaluated when being iterated, one at a time. It returns a Generator expression
"""
nums_generator = (i for i in range(1, 100_000_000))

print(sum(nums_generator))  # 4999999950000000
print(sum(nums_generator))  # 0, because it can only be iterated ONCE.
