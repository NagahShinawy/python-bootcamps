WELCOME = "Welcome"
HELLO_WORLD = "Hello World"


def say_hello(name=""):
    if name:
        return f"{WELCOME} {name.title()}"
    return HELLO_WORLD


print(say_hello(name="john"))