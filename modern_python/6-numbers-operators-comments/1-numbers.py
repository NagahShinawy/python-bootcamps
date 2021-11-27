import random
import inflect

# private
# constants
# floating point
# decimal places
# N decimal places
# using property decorator
# using private access modifier
# using class method (classmethod)
# encapsulation: hide attributes, just dealing with it using methods
# from number to word using inflect
# using type() function
# floor division
# float / float = float
# float / int = float
# int / float = float
# int / int = float

# #####

# int + float = float
# float + float = float
# int + int = int

# ########### ########### ########### ########### ########### ########### ########### ##########
print(12 + 1.0)  # 13.0 float
print(12.0 + 1.0)  # 13.0 float
print(12 + 1)  # 13 int

revenue = 130
YEARLY_BONUS = 150

print(10.5 / 2.6)  # 4.038461538461538   ===> float / float  ==> float
print(10.5 / 2)  # 5.25   ===> float / int ==> float
print(10 / 2.0)  # 5.0   ===> int / float == float

print(10 / 2)  # 5.0 ==> int / int = float
print(revenue)

salary = 12.878

print(salary)

by_quarter = YEARLY_BONUS / 4  # float
print("By Quarter", by_quarter)  # float

by_quarter = YEARLY_BONUS // 4

print("By Quarter", by_quarter)  # floor division

# string formatting: round float number with f
# How to format float to N decimal places

#  https://dev.to/jerrynsh/3-useful-python-f-string-tricks-you-probably-don-t-know-2o54

salary = 343.6765666

print("{:.2f}".format(salary))  # 343.68

print(f"{salary:.2f}")  # # 343.68


# Turn float into a pretty currency value
total_revenue = 3142671.763453

print(f"${total_revenue:,.2f}")  # $3,142,671.76


class Currency:
    DOLLAR = "$"
    EUR = "€"
    SAR = "SAR"
    EGY = "EGY"


class Revenue:

    __CURRENCY = Currency.DOLLAR

    __DECIMAL_PLACES = 2

    def __init__(self, value):
        self.value = value

    @property
    def to_int(self):
        return int(self.value)

    @property
    def to_currency(self):
        return f"{self.__CURRENCY} {self.value:,.{self.__DECIMAL_PLACES}f}"

    @property
    def to_pretty(self):
        return f"{self.value:.{self.__DECIMAL_PLACES}f}"

    @property
    def to_words(self):
        return inflect.engine().number_to_words(self.value)

    @classmethod
    def change_currency(cls, currency):
        cls.__CURRENCY = currency
        return cls.__CURRENCY


def main():
    print(type(34))  # <class 'int'>
    print(type(23.65))  # <class 'float'>

    q1_revenue = Revenue(1_200_150.345)
    print(q1_revenue.to_int)
    print(q1_revenue.to_currency)
    print(q1_revenue.to_pretty)
    print(
        q1_revenue.to_words
    )  # one million, two hundred thousand, one hundred and fifty point three four five

    print(q1_revenue.change_currency(Currency.SAR))
    print(q1_revenue.to_currency)


if __name__ == "__main__":
    main()
