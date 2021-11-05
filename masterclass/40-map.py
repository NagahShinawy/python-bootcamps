# map: apply logic[expression] on iterable


BONUS = 100

salaries = [6000, 4000, 5000, 3000, 8000, 7000]

with_bonus = map(lambda sal: sal + BONUS, salaries)

print(salaries)
print(with_bonus)  # <map object at 0x0000020A4211E288>

print(list(with_bonus))
