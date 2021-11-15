# todo #1 using **kwargs examples

# todo #2 identifiers
# refer to a name used to identify a variable, function, module, class, module or other objects.
# There are few rules to follow while naming the Python Variable.


def show_info(**kwargs):
    info = ""
    name = kwargs.get("name")
    age = kwargs.get("age")
    address = kwargs.get("address")

    if name:
        info = f"name: {name}\n"

    if age:
        info += f"age: {age}\n"

    if address:
        info += f"Address: {address}\n"

    return info if info else "No data to display"


def display_info(**kwargs):
    info = "\n".join([f"{key.title()}: {value}" for key, value in kwargs.items()])
    return info


def main():
    print(show_info(address="cairo", age=12, name="John"))
    print(display_info(age=12, name="John", address="Cairo"))


if __name__ == '__main__':
    main()
