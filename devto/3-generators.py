"""
As Generators give us lazy evaluation, they are a great way to generate sequences in a memory-efficient manner.
We should definitely consider using Generator when dealing with huge datasets to optimize our program
"""

import cProfile
numbers = (num for num in range(100))

# print(numbers[0])  # TypeError: 'generator' object is not subscriptable


# test performance using list com
cProfile.run(statement="sum([num for num in range(10_000_000)])")

print("#" * 100)

# test performance using generator
cProfile.run(statement="sum((num for num in range(10_000_000)))")
