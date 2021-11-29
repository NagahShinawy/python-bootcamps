#  strings are treated as the sequence of characters

#  which means that Python doesn't support the character data-type; instead,
#  a single character written as 'p' is treated as the string of length 1.

# strings
# constants
# creating strings using single , double and triple quotes
# string indexing, splitting
# string immutable which means it can not be change
# string slicing
# negative indexing
# slicing with step
# delete del string
# duplicate string
# string operator
# in membership operator
# raw string using r
# escape chars
# escaping  (https://www.javatpoint.com/python-strings)
# format method  (using Curly braces, Positional Argument, Keyword argument, dictionary unpacking)
# string methods  https://www.javatpoint.com/python-strings


hi = "Hi"
welcome = "Hello World"

print(welcome, type(welcome))

ACCEPT = "Y"  # string of single letter with length 1

REFUSED = "N"

policy = """
To register for the medical test please follow these steps:
• Please Access to this link https://v2.gcchmc.org/
• Press book an appointment button
"""
print(ACCEPT)
print(REFUSED)


# Strings indexing and splitting

laptop = "macbook"

print(laptop[0])
print(laptop[1])
print(laptop[2])
print(laptop[3])
print(laptop[4])
print(laptop[5])
print(laptop[6])

# ERROR
# print(laptop[7])  # IndexError: string index out of range

# ERROR
# laptop[0] = "M"  # TypeError: 'str' object does not support item assignment


# slicing
#                   0 1 2 3 4 5 6
print(laptop[:])  # m a c b o o k
print(laptop[:3])  # m a c
print(laptop[3:5])  # bo

# negative indexing
print(laptop[:-3])  # macb  [ exclude last 3 chars]

print(laptop[:-1])  # macboo [ exclude last char]

print(laptop[-2:])  # ok  [ get just last 2 chars]

# reverse

print(laptop[::-1])  # koobcam

laptop = "macbook pro 2021"
print(laptop[2:8:2])  # cok

# ERROR
# del laptop[0]  # TypeError: 'str' object doesn't support item deletion

print(laptop)


del laptop

# ERROR
# print(laptop)  NameError: name 'laptop' is not defined

print("#" * 50)  # duplicate chars

email = "john@test.com"

DOMAIN = "test.com"


# in operator
print(DOMAIN in email)  # True

# raw string using r

print("this is \\ ")  # escape chars  ==> this is \

print("this is \ ")  # this is \

# ERROR
# print(r"this is \")  # SyntaxError: EOL while scanning string literal

print(r"this is \ ")  # this is \

# ################


# escape chars
context = 'They said, "Hello what\'s going on?"'
print(context)


# escape chars using triple quotes
print('''''They said, "What's there?"''')


# escaping single quotes
print('They said, "What\'s going on?"')


# escaping double quotes
print('They said, "What\'s going on?"')


# https://www.javatpoint.com/python-strings

# The list of an escape sequence is given below:

# ############# ############# ############# ############# ############# ############# ############

# The format() method
print("#" * 50)

username = "john"
dob = "1990-01-01"

# Using Curly braces
print("Username: {}\nDate of birth".format(username, dob))

# Using Positional Argument
MESSI = "Messi"
RONALDO = "Ronaldo"

print("{1} and {0} are best players ".format(RONALDO, MESSI))


# ############# ############# ############# ############# ############# ############# ############

# using keyword argument
user = {
    "username": "John",
    "dob": "1990-01-01",
    "id": "123456789",
}


print(
    "Username: {username}\nDate of birth: {dob}\nid:{id}".format(
        username=user["username"], dob=user["dob"], id=user["id"]
    )
)

# using dictionary unpacking
print("Username: {username}\nDate of birth: {dob}\nid:{id}".format(**user))
