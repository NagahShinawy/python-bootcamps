import random
import inflect

# private
# constants
# floating point
# decimal places
# N decimal places
# using property decorator
# using private access modifier
# from number to word using inflect

revenue = 130

print(revenue)

salary = 12.878

print(salary)


# string formatting: round float number with f
# How to format float to N decimal places

#  https://dev.to/jerrynsh/3-useful-python-f-string-tricks-you-probably-don-t-know-2o54

salary = 343.6765666

print("{:.2f}".format(salary))  # 343.68

print(f"{salary:.2f}")  # # 343.68


# Turn float into a pretty currency value
total_revenue = 3142671.763453

print(f"${total_revenue:,.2f}")  # $3,142,671.76


class Revenue:

    __CURRENCY = "$"
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
    def to_word(self):
        return inflect.engine().number_to_words(self.value)


def main():
    q1_revenue = Revenue(1_200_150.345)
    print(q1_revenue.to_int)
    print(q1_revenue.to_currency)
    print(q1_revenue.to_pretty)
    print(
        q1_revenue.to_word
    )  # one million, two hundred thousand, one hundred and fifty point three four five


if __name__ == "__main__":
    main()
