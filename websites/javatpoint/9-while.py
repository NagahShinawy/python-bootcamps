"""
while expression:
    statements
"""

# while [pre tested loop]

# The Python while loop allows a part of the code to be executed until the given condition returns false.
# It is also known as a pre-tested loop

# The expression should be any valid Python expression resulting in true or false


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
    if letter == 'p':
        break

    print(letter, end="")
