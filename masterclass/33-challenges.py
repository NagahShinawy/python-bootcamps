numbers = range(1, 101)

odd = [num for num in numbers if num % 2 != 0]

print(odd)

print("#" * 50)


evens = [num for num in numbers if num not in odd]

print(evens)
