fname = "John"

lname = "Loen"
SPACE = " "

fullname = fname + SPACE + lname

print(fullname)

print("5" + "5")  # strings = '55'

print(5 + 5)  # integers = 10
book = "clean code"
price = 30
# book_info = book + price  # TypeError: can only concatenate str (not "int") to str

book_info = book + str(price)

print(book_info)

book_info = f"{book} {price}"

print(book_info)

# duplicates

line = "#" * 50

print(line)

# line = "#" * "10"  # TypeError: can't multiply sequence by non-int of type 'str'
