# Lambdas is quick function or anonymous function, function with no name, no return statement
# for example ==>  input: x , expression = OUTPUT: x ** 2

DOLLAR = 15


def dollar_to_egy(value):
    return value * DOLLAR


salary = 2000

print(dollar_to_egy(salary))


result = lambda value: value * DOLLAR


print(result)  # <function <lambda> at 0x0000028C95C42708>
print(result(10))
print(result(1))


result = (lambda value: value * DOLLAR)(2)

print(result)


salaries = [200, 500, 1000, 2000, 300, 700]

print("#" * 100)

dollar = lambda value: value * DOLLAR

for salary in salaries:
    print(dollar(salary))
