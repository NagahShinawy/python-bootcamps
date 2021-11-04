# key value data structure ==> key value pairs
# mapping key with value
from dataclasses import dataclass


country = {
    "name": "Egypt",
    "capital": "Cairo",
    "region": "Africa",
    "famous_cities": ["cairo", "alex", "ssh"],
}

items = [
    {"name": "mobile", "price": 20, "in_stock": True},
    {"name": "laptop", "price": 2000, "in_stock": True},
    {"name": "headphone", "price": 100, "in_stock": False},
    {"name": "jacket", "price": 50, "in_stock": False},
]

print(f"COUNTRY IS : {country['name']}")
print(f"CAPITAL IS : {country['capital']}")
print(f"REGION IS : {country['region']}")
print(f"CITIES IS : {country['famous_cities']}")
print(f"Cairo IS : {country['famous_cities'][0]}")
print(f"Alex IS : {country['famous_cities'][1]}")
print(f"Cities IS : {country['famous_cities'][2]}")


for item in items:
    print(item)


total = sum([item["price"] for item in items])
print(total)


# dataclass: class that is represent data


@dataclass
class Item:
    name: str
    price: float
    in_stock: bool


macbook = Item("macbook", 3000, True)
print(macbook.in_stock)
