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
        if attr == 'age':
            try:
                if not isinstance(value, int):
                    age = int(value)
                    return super().__setattr__(attr, age)
            except (ValueError, TypeError):
                raise ValueError(NOT_INT_ERROR.format(attr=attr, value=value))
        return super(User, self).__setattr__(attr, value)

    def __str__(self):
        return f"{self.cls}(name={self.name}, age={self.age})"


john = User("John", "12")

print(john.age + 10)