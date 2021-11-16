from abc import ABC

NOT_INT_ERROR = "{attr} should be valid int number, given '{value}'"


# class mixin
class ClsMixin(ABC):
    @property
    def cls(self):
        return self.__class__.__name__


class User(ClsMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, attr, value):
        if attr == "age":
            try:
                if not isinstance(value, int):
                    age = int(value)
                    return super().__setattr__(attr, age)
            except (ValueError, TypeError):
                raise ValueError(NOT_INT_ERROR.format(attr=attr, value=value))
        return super(User, self).__setattr__(attr, value)

    def __str__(self):
        return f"{self.cls}(name={self.name}, age={self.age})"

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def to_json(self):
        return {"name": self.name, "age": self.age}


class Book:
    def __init__(self, title, price):
        self.__title = title
        self.__price = price

    @property
    def title(self):
        return self.__title


adam = User("adam", "12")

print(adam.age + 10)

print("#" * 100)

cleancode = Book("Clean Code", 10)
print(cleancode.title)


print("#" * 100)

print(adam.to_json())