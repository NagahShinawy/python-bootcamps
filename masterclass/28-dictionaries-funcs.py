product = {"name": "mobile", "price": 90, "has_offer": False}

# 1- using in operator

# checking using KEYS  ==> just like using get()
print("price" in product)
print("discount" in product)


# 2- using get method
discount = product.get("discount")  # None
print(discount)


discount = product.get(
    "discount", False
)  # False   ==> value returned in case of key not found
print(discount)

price = product.get("price")
print(price)


# 3- using update method

product.update({"color": "red"})

print(product)

# update dictionary

product["seller"] = "Amazon"

print(product)

# 4- remove item from dictionary

product.pop("color")

print(product)

product.update({"colors": ["red", "green", "blue", "black", "white"]})

print(product)
