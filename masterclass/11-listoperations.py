# lists are mutable

emails = [
    "john@test.com",
    "james@test.com",
    "loen@test.com",
    "adam@test.com",
    "angela@test.com",
]

external_emails = [
    "sara@edu.com",
    "martin@edu.com",
]
print(emails)
emails[-1] = "angel-amartin@test.com"

print(emails)

allemails = emails + external_emails

print(allemails)

# duplication

shopping_cart = [
    "mobile",
    "laptop",
    "shoes",
    "jacket",
]

print(shopping_cart * 2)


fruits = ["Apple", "Orange", "Banana", "Mango"]

print("Apple" in fruits)
print("apple" in fruits)
print("orange" in fruits)
print("Orange" in fruits)
