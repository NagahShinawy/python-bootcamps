"""
while expression:
    statements
"""

# while [pre tested loop]

# The Python while loop allows a part of the code to be executed until the given condition returns false.
# It is also known as a pre-tested loop

# The expression should be any valid Python expression resulting in true or false
# else with while


# # prints all letters except 'a' and 't'

website = "javatpoint"
EXCLUDED_LETTERS = "at"

print(website)

for letter in website:
    if letter in EXCLUDED_LETTERS:
        continue
    print(letter, end="")


print()
# stop when find letter 'p'

for letter in website:
    if letter == "p":
        break

    print(letter, end="")


# pass statement: do nothing, skip implementation


def welcome():
    pass


print()
# Example-1: Program to print 1 to 10 using while loop

start = 1
END = 10

while start <= END:
    print(start)
    start += 1


# ############ ############ ############ ############ ############ ############ ###########

# Example -2: Program to print table of given numbers.

user_number = 5

start = 1
END = 10
MULTI = "*"


while start <= END:
    result = start * user_number
    print(f"{start} {MULTI} {user_number} = {result}")
    start += 1


"""
Python allows us to use the else statement with the while loop also.
The else block is executed when the condition given in the while statement becomes false. Like for loop,
if the while loop is broken using break statement, then the else block will not be executed,
and the statement present after else block will be executed. The else statement is optional to use with the while loop.
Consider the following example.
"""
counter = 1

while counter <= END:
    print(counter, end="")
    counter += 1
    if counter > END:
        print()

else:
    print("Done")
