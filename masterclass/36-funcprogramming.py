TEN = 10


def add_ten(number):
    return number + TEN


def twice(function, num):
    return function(function(num))


print(add_ten(1))  # 1
print(twice(add_ten, 1))  # 21  ==> (1 + 10) + 10
