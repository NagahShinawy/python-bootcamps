emails = [
    "john@test.com",  # 0
    "james@test.com",  # 1
    "loen@test.com",  # 2
    "adam@test.com",  # 3
    "angela@test.com",  # 4
]


print(emails[2:-1])
print(emails[1:3])

print(emails[::-1])

print(emails[::2])  # ['angela@test.com', 'loen@test.com', 'john@test.com']
print(emails[::-2])  # ['angela@test.com', 'loen@test.com', 'john@test.com']


print((emails[:3]))  # ['john@test.com', 'james@test.com', 'loen@test.com']

print(emails[2:])  # ['loen@test.com', 'adam@test.com', 'angela@test.com']

print(emails[1:4])  # ['james@test.com', 'loen@test.com', 'adam@test.com']

print(emails[1:5] == emails[1:5])  # True


numbers = [50, 34, 66, 77, 10, 23, 65, 98, 90, 100, 300, 200, 250]

print(numbers[::2])  # [50, 66, 10, 65, 90, 300, 250]

print(numbers[::3])  # [50, 77, 65, 100, 250]