from abc import ABC


# using protected attributes

# Mixin for crud operations

# *args real example ==> can create one or many courses

# using composition : means has-A ==> course (has a) teacher


class CRUDMixin:
    def __init__(self):
        self.objects = []

    def _create(self, obj):
        if obj not in self.objects:
            self.objects.append(obj)

    def _delete(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)

    def _create_all(self, *args):
        for obj in args:
            self._create(obj)

    def _delete_all(self, *args):
        for obj in args:
            self._delete(obj)

    @property
    def count(self):
        return len(self.objects)

    def __len__(self):
        return len(self.objects)


class Course:
    def __init__(self, title, duration, teacher):
        self.title = title
        self.duration = duration

        # composition
        self.teacher = teacher

    def __repr__(self):
        return f"<{self.title} - {self.duration} - {self.teacher}>"


class Member(ABC, CRUDMixin):
    def __init__(
        self, name: str, dob: str, phone: str, email: str, address=None, *args, **kwargs
    ):
        super().__init__()
        self.name = name
        self.dob = dob
        self.phone = phone
        self.email = email
        self.address = address
        self.courses = self.objects

    def __str__(self):
        return f"{self.__class__.__name__}<{self.name} - {self.phone}>"

    def join_course(self, course: Course):
        self._create(course)

    def join_courses(self, *args: Course):
        self._create_all(*args)

    def remove_course(self, course: Course):
        self._delete(course)


class Student(Member):
    def __init__(self, class_, name, dob, phone, email, address=None, *args, **kwargs):
        self.marks = []
        self.class_ = class_
        super().__init__(name, dob, phone, email, address=address, *args, **kwargs)


class Teacher(Member):
    pass


def main():
    prof = Teacher(
        name="Prof", dob="01-01-1980", phone="+20127999999", email="prof@test.con",
    )
    django = Course("Django", "10H", prof)
    gui = Course("PyQt GUI", "5H", prof)
    flask = Course("Flask Micro Framework", "3H", prof)
    nodejs = Course("NodeJs", "7H", prof)
    php = Course("PHP", "4H", prof)

    john = Student(
        class_="A",
        name="John",
        dob="01-01-1999",
        phone="+20127444444",
        email="jonh@test.con",
    )
    leon = Student(
        class_="B",
        name="Loen",
        dob="01-01-2000",
        phone="+20127555555",
        email="loen@test.con",
    )

    print(john)
    john.join_course(flask)
    john.join_course(django)
    print(john.courses)

    print(john.count)
    print(len(john))

    print("#" * 100)
    leon.join_courses(php, nodejs, gui)
    print(leon.courses)


if __name__ == "__main__":
    main()
