# 1- Single-line String
book = "Clean Code"

# 2- Multi-line String

books = """
clean code
python for prof
django for web apps
"""

# 3- Adding black slash at the end of each line.

# John JamesLoen AdamSara Angela
names = "John James" "Loen Adam" "Sara Angela"

# #################### #################### #################### #################### ###################
print(book)
print(books)


print(names)


# 4- Boolean

# # #################### #################### #################### #################### ###################
x = 1 == True
y = 0 == False
z = 3 == True

a = True + 10
b = False + 10

print(x)  # True 1 means True
print(y)  # True 0 means False
print(a)  # True means 1  ==> 1 + 10 = 11
print(b)  # False means 0  ==> 0 + 10  = 10

# # #################### #################### #################### #################### ###################

# 5- Example - Special Literals

is_married = None

print(dir(None))

# # #################### #################### #################### #################### ###################

# List contains items of different data types. Lists are mutable i.e., modifiable.

books = ["clean code", "clean arch", "Js", "React"]

print(books)

# # #################### #################### #################### #################### ###################

# Dictionary

# nested dictionary

medical_report = {
    "created": "2012-01-01",
    "medical_center": "Alfa",
    "hear": "good",
    "eye": "good",
}


print(medical_report)

medical_report = {
    "fname": "James",
    "lname": "Loen",
    "address": "Cairo",
    "gender": "male",
    "national_id": "01234567891234",
    "passport": "X0123456789",
    "created": "2012-01-01",
    "medical_center": {
        "name": "Alfa",
        "location": {"lat": 3434.34, "log": 345.90},
        "address": "Giza-Egypt",
    },
    "hear": "good",
    "eye": "good",
    "status": "fit",
}

# # #################### #################### #################### #################### ###################


# tuple : ready only data structure
# Python tuple is collection of different data-type. It is immutable which means it cannot be modified after creation.

GENDER = ("Male", "Female")
DAYS = ("Mon", "Tue", "Wen", "Thr", "Fri", "Sat", "Sun")

BLOOD_TYPES = ("A+", "A-", ...)  # Ellipsis
print(BLOOD_TYPES)

LOCATION = (34.90, 90.32)

# # #################### #################### #################### #################### ###################

print("#" * 100)

"""
Set:

Python set is the collection of the unordered dataset with no duplicates.
It is enclosed by the {} and each element is separated by the comma(,).
"""

salaries = {500, 600, 300, 1200, 400, 600, 100, 500}

print(salaries)
print(len(salaries))
print(sorted(salaries), type(sorted(salaries)))  # list
