START = 0

counter = START

counter += 1  # ===> means counter = counter + 1

print(counter)

age = 30

age -= 10

last_year = age

print(age)
print(last_year)

salary = 50

salary *= 3

print(salary)  # 150

income = 500

income /= 2

print(income)  # 250.0

income = 500
income //= 2
print(income)  # 250

welcome = "Welcome "

name = input("Please enter your name: ")

if name:
    welcome += name


print(welcome)