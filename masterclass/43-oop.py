from abc import ABC, abstractmethod
from typing import List


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


# abstract base class
# interface

# class mixin
class ClsMixin(ABC):
    @property
    def cls(self):
        return self.__class__.__name__


class JsonMixin(ABC):
    @abstractmethod
    def to_json(self):
        pass


class Seller(JsonMixin, ClsMixin):
    def __init__(self, name):
        self.name = name

    def to_json(self):
        return {"name": self.name}

    def __str__(self):
        return f"{self.cls}({self.name})"


class Product(JsonMixin, ClsMixin):
    def __init__(self, name: str, price: float, seller: Seller):
        self.name = name
        self.price = price
        self.seller = seller

    def __str__(self):
        return f"{self.cls}({self.name}<{self.price}>)"

    def to_json(self):
        return {"name": self.name, "price": self.price, "seller": self.seller.to_json()}


class Order(JsonMixin, ClsMixin):
    def __init__(self, products: List[Product]):
        self.products = products

    def __str__(self):
        return f"{self.cls}({len(self.products)})"

    def __len__(self):
        return self.products

    def to_json(self):
        return [product.to_json() for product in self.products]


class Color:
    pass


class Teddy:
    # class attribute
    WHITE = 'White'
    quantity = 0

    def __init__(self, name, color):
        self.__name = name
        self.__color = color
        Teddy.quantity += 1

    def change_color(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @property
    def to_white(self):
        self.__color = self.WHITE
        return self.__color


def main():
    python = Language(name="Python", users=100, level="high")
    # ############# ############# ############# ############# ############# ############
    amazon = Seller("Amazon")
    noon = Seller("noon")
    extra = Seller("Extra")

    phone = Product("iphone", 1000, noon)
    laptop = Product("macbook pro", 2000, amazon)
    screen = Product("dell", 500, extra)

    order = Order(products=[phone, laptop, screen])
    print(order)
    print(order.to_json())
    print(noon)
    print(phone)

    # ############# ############# ############# ############# ############# ############
    panda = Teddy("panda", "red")
    dolphin = Teddy("dolphin", "blue")
    rabbit = Teddy("rabbit", "white")
    print(panda.quantity, panda.color)
    print(rabbit.quantity, rabbit.color)
    print(dolphin.quantity, dolphin.color)
    dolphin.change_color('sky')
    print(dolphin.color)
    print(dolphin.to_white)


if __name__ == "__main__":
    main()
