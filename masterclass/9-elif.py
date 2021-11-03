grade = int(input("Please enter your grade: "))

if grade in range(0, 50):
    print("Failed")

elif grade in range(50, 66):
    print("Passed")

elif grade in range(66, 76):
    print("Good")


elif grade in range(76, 86):
    print("Very Good")


elif grade in range(86, 101):
    print("Excellent")


else:
    print("Invalid Grade")
