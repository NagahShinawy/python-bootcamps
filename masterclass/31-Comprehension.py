numbers = [6, 8, 90, 12, 100]


print(numbers)
sqrs = [num ** 2 for num in numbers]

print(sqrs)


names = ["James", "John", "Loen", "Smith", "Angela", "Anna", "Adam"]

name_len = [(name, len(name)) for name in names]

print(name_len)

PENDING = "Pending"
APPROVE = "Approve"
CANCELED = "Canceled"
REJECTED = "Rejected"


STATUS = (PENDING, APPROVE, CANCELED, REJECTED)

FINISHED = (status for status in STATUS if status not in (PENDING, CANCELED))

print(FINISHED)  # <generator object <genexpr> at 0x000002CEFC40EC48>
