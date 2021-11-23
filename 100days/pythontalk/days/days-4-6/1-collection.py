from collections import namedtuple


# A `namedtuple` is a convenient way to define a class without methods.
# This allows you to store `dict` like objects you can access by attributes. Let's first look at a classic `tuple`:

users = [
    ("bob", "1991-01-01", "bob@test.com"),
    ("james", "1994-01-01", "james@test.com"),
    ("john", "1995-01-01", "john@test.com"),
    ("adam", "1999-01-01", "adam@test.com"),
]


# WITHOUT namedtuple
print("Username", "Date of birth", "Email")
print("#" * 50)
for user in users:
    print(user[0], user[1], user[2])


# ########################## ############################## ##########################################
# With namedtuple
print("#" * 100)


User = namedtuple("User", ["username", "dob", "email"])

for user in users:
    obj = User(*user)
    print(obj.username, obj.dob, obj.email)  # more readable
