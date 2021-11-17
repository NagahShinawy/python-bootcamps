from abc import ABC

NOT_INT_ERROR = "{attr} should be valid int number, given '{value}'"
NOT_NUMBER = "value '{value}' not number"


class NotNumberException(ValueError):
    pass


# class mixin
class ClsMixin(ABC):
    @property
    def cls(self):
        return self.__class__.__name__


class InputMixin:

    PROMPT = "Enter Your Value: "

    # protected method
    def _set_value(self):
        value = input(self.PROMPT)
        setattr(self, "_value", value)
        return value

    @staticmethod
    def to_int(value):
        try:
            value = int(value)
        except (ValueError, TypeError):
            raise NotNumberException(NOT_NUMBER.format(value=value))
        else:
            return value

    @staticmethod
    def to_float(value):
        try:
            value = float(value)
        except (ValueError, TypeError):
            raise NotNumberException(NOT_NUMBER.format(value=value))
        else:
            return value


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


class Book(InputMixin):
    def __init__(self, title: str, price: float):
        self.__title = title
        self.__price = price

    @property
    def title(self):
        return self.__title

    @property
    def price(self):
        return self.__price

    def update_title(self):
        self.__title = self._set_value()
        return self.__title

    def update_price(self):
        self.__price = float(self._set_value())
        return self.__price


adam = User("adam", "12")

print(adam.age + 10)

print("#" * 100)

cleancode = Book("Clean Code", 10)
django = Book("django for web apps", 23.6)
print(cleancode.title)


print("#" * 100)

print(adam.to_json())
cleancode.update_title()
print(cleancode.title)

print("#" * 100)

print(cleancode.price)
cleancode.update_price()
print(cleancode.price)

print("#" * 100)

print(django.price)

print(django.to_int(django.price))

flask = Book("Flask for micro web apps", "46.7")

print(flask.price)
print(flask.to_float(flask.price))
