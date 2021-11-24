# 1- single line comment
# 2- multi line comment
# 3- doc string
# 4- show doc using __doc__

# 1- Multiline Python Comment


# this is
# multiline comment

"""
this is
multiline
comment
"""

# 2- Single line comment

# this is single line comment

"""
Docstrings Python Comment
The docstring comment is mostly used in the module, function, class or method. It is a documentation Python string.
"""


# 3- doc string
class HTMLElement:
    """
    base class to represent html element
    """

    def attributes(self):
        """
        get html element attributes
        :return:
        """


print(HTMLElement.__doc__)  # base class to represent html element

# print(attributes.__doc__)  # NameError: name 'attributes' is not defined

print(HTMLElement().attributes.__doc__)  # get html element attributes :return:

# Note: The docstring must be the first thing in the function; otherwise, Python interpreter cannot get the docstring.
