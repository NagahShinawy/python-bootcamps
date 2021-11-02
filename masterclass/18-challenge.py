food = [
    "rice", "chicken", "meat", "pasta", "fish"
]


print(food[2])

food.append("egg")
print(food)


food.insert(3, "bisc")

print(food)

TIMES = 5


def sqr(number: int):
    return number ** 2


for i in range(TIMES):
    print("I am a programmer")

print("#" * 100)

for i in range(1, 10):
    print(i, sqr(i))