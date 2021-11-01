products = [
    "mobile",
    "laptop",
    "headphone",
]

# 1- append

print(products, len(products))
products += ["keyboard"]

print(products, len(products))
products.append("mouse")

print(products, len(products))


# 2- insert

products.insert(2, "Jacket")


print(products)


# 3- index


# test = products.index("test")  # ValueError: 'test' is not in list
jacket_index = products.index("Jacket")  # 2

print(jacket_index)


# 4- remove

# products.remove("test")  # ValueError: list.remove(x): x not in list

mouse = products.remove("mouse")

print(mouse)  # None: just remove obj NOT RETURN IT

# 5

# lap = products.pop(10)  # IndexError: pop index out of rang
lap = products.pop(1)  # remove obj AND return it

print(lap)

print(products)
