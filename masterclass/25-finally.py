from typing import Any


def remove_one(values: list, value: Any):
    try:
        values.remove(value)
    
    except ValueError:
        return values
    
    else:
        # in the case of success
        print(f"Value {value} was removed")

    finally:
        print("Exiting Program")


print(remove_one([7, 6, 4, 5], 5))