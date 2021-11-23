from collections import namedtuple


# A `namedtuple` is a convenient (مريح) way to define a class without methods.
# This allows you to store `dict` like objects you can access by attributes. Let's first look at a classic `tuple`:

users = [
    ("bob", "1991-01-01", "bob@test.com"),
    ("james", "1994-01-01", "james@test.com"),
    ("john", "1995-01-01", "john@test.com"),
    ("adam", "1999-01-01", "adam@test.com"),
]

# PROBLEM: The order is not really meaningful leading to ugly code to output the data:

# WITHOUT namedtuple
print("Username", "Date of birth", "Email")
print("#" * 50)
for user in users:
    print(user[0], user[1], user[2])


# ########################## ############################## ##########################################
# With namedtuple
# SOLUTION: using attributes rather than indexing (order)

print("#" * 100)


User = namedtuple("User", ["username", "dob", "email"])

for user in users:
    obj = User(*user)
    print(obj.username, obj.dob, obj.email)  # more readable

# ########################## ############################## ##########################################

print("#" * 100)

Location = namedtuple("Location", "long,lat")

work = Location(23.54, 65.9)
print(work)  # Location(long=23.54, lat=65.9)
print(type(work))  # <class '__main__.Location'>
print(f"Long: {work.long}")
print(f"Lat: {work.lat}")


# ########################## ############################## ##########################################

print("#" * 100)

book = ("clean code", 10, "uncle bob", "2000-01-01")

# not readable code, it is ugly code

print(f"'{book[0]}' by '{book[2]}' is '{book[1]}$' was published at '{book[3]}'")


Book = namedtuple("Book", "title price author published")

clean_code = Book("Clean Code", 14, "Bob", "2000-01-01")  # <class '__main__.Book'>

print(
    clean_code
)  # Book(title='Clean Code', price=13, author='Bob', published='2000-01-01')


print(
    f"'{clean_code.title}' by '{clean_code.author}' is '{clean_code.price}$' was published at '{clean_code.published}'"
)

print(clean_code.count(14))  # count comes from tuple class

print(type(clean_code))


# namedtuple inherits from tuple

print(Book.mro())  # [<class '__main__.Book'>, <class 'tuple'>, <class 'object'>]


# ########################## ############################## ##########################################

print("#" * 100)

clean_arch = Book(title="Clean Arch", published="1999-01-01", price=16, author="James")

print(clean_arch.title, clean_arch.author)
print(
    clean_arch
)  # Book(title='Clean Arch', price=16, author='James', published='1999-01-01')
print(type(clean_arch))  # <class '__main__.Book'>
