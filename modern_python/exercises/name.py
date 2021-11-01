class Name:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def to_fullname(self):
        return f"{self.fname} {self.lname}".title()

    def __str__(self):
        return self.to_fullname()

    def __len__(self):
        return len(self.to_fullname())


john = Name(fname="john", lname="james")

print(john)
print(len(john))
