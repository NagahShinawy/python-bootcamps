MALE = "M"
FEMALE = "F"


GENDERS = {MALE: 1, FEMALE: 0}


if GENDERS["M"] == 1:
    print("Male")
else:
    print("Female")


BLOOD_TYPES = (
    "A+",
    "A-",
    "B+",
    "B-",
    "AB+",
    "AB-",
    "O+",
    "O-",
)


is_pregnant = True

users = [
    {"username": "james", "age": 12, "id": 1, "gender": MALE},
    {"username": "john", "age": 20, "id": 10, "gender": MALE},
    {"username": "angela", "age": 23, "id": 90, "gender": FEMALE, "is_pregnant": True},
    {"username": "sara", "age": 25, "id": 66, "gender": FEMALE, "is_pregnant": False},
]

males = [user for user in users if user.get("gender") == MALE]

print(males)

females1 = [user for user in users if user.get("gender") == FEMALE]
print(females1)

females2 = [user for user in users if user not in males]

print(females2)

print(females1 == females2)
