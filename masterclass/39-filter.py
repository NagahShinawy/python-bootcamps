# filter: filter items from iterable based on condition

numbers = [4, 6, 7, 9, 11, 20, 13, 15]


evens = [num for num in filter(lambda num: num % 2 == 0, numbers)]

odd = filter(lambda num: num not in evens, numbers)

print(evens)
print(list(evens))
print(odd)  # <filter object at 0x0000027927EBB508>
print(list(odd))
