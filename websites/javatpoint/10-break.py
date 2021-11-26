"""
The break is a keyword in python which is used to bring the program control out of the loop.
The break statement breaks the loops one by one, i.e., in the case of nested loops,
it breaks the inner loop first and then proceeds to outer loops.
In other words, we can say that break is used to abort the current execution
of the program and the control goes to the next line after the loop
"""

names = ["john", "james", "leon", "adam", "angela", "sara"]

LEON = "leon"
for name in names:
    if name == LEON:
        break
    print(name)


PYTHON = "python"

for letter in PYTHON:
    if letter == "h":
        break

    print(letter)