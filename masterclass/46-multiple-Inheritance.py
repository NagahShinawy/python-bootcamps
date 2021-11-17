# Multiple Inheritance
# MRO


class BasicProfile:
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def show_profile(self):
        print(f"First Name: {self.fname}")
        print(f"Last Name: {self.lname}")
        print(f"Email: {self.fname}")


class VitalSignProfile:
    def __init__(self, fname, lname, email, high, weight):
        super().__init__(fname, lname, email)
        self.high = high
        self.weight = weight

    def show_profile(self):
        print(f"High: {self.high}")
        print(f"Weight: {self.weight}")


# MRO : means go first to 'VitalSignProfile' because you used it first
class HealthProfile(VitalSignProfile, BasicProfile):

    pass


class MedicalProfile(BasicProfile, VitalSignProfile):

    pass


# required 5 args because you are using VitalSignProfile that use 5 [ 3 from BasicProfile, 2 from VitalSignProfile]
# TypeError: __init__() missing 5 required positional arguments: 'fname', 'lname', 'email', 'high', and 'weight'
# print(HealthProfile())


# means go and init for first class you inherit from
print(MedicalProfile("", "", ""))


class BasicInfo:
    def show(self):
        print("From Basic Info")


class PersonalInfo:
    def show(self):
        print("From PersonalInfo")


class PersonalDetails(BasicInfo, PersonalInfo):
    pass


details = PersonalDetails()
details.show()  # From Basic Info ==> because 'BasicInfo' comes first [MRO]
