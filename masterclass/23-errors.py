# 1- syntax error

# def welcome()   # SyntaxError: invalid syntax ==> missing ':'
#     pass

# ########### ########### ########### ########### ########### ########### ########### ##########
# 2- logical error


def add(n1, n2):
    return n1 * n2


print(add(2, 3))  # 6 NOT 5 ===> logical error


# ########### ########### ########### ########### ########### ########### ########### ##########

# 3- runtime error


def div(n1, n2):
    return n1 / n2


print(div(10, 2))  # float 5.0


# run time error  ===> in this case program will crash
# print(div(6, 0))   # ZeroDivisionError: division by zero


# import error
# import tensorflow  # ModuleNotFoundError: No module named 'tensorflow'
