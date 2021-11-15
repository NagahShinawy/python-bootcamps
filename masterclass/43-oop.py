class BaseError(Exception):
    _message = "error occurred"

    @classmethod
    def _raise(cls):
        raise cls(cls._message)


class LevelNotExist(BaseError):
    _message = "level {level} is not found, choose one of {levels}"


class Language:
    LEVELS = ["machine", "assembly", "high"]

    def __init__(self, name: str, users: int, level: str):
        self.name = name
        self.users = users
        self.level = level

    def __setattr__(self, key, value):
        if key == "level" and value not in self.LEVELS:
            error = LevelNotExist
            error._message = error._message.format(level=value, levels=self.LEVELS)
            error._raise()
        return super(Language, self).__setattr__(key, value)

    def __repr__(self):
        return f"{self.name} - {self.users}"


class PhoneNumberInvalid(BaseError):
    _message = "Enter a valid phone number"


python = Language(name="python", users=100, level="high")

if 1:
    raise PhoneNumberInvalid
