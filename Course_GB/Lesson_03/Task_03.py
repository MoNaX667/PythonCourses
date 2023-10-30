# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a,b,c):
    """
    The function will return sum of two biggest numbers
    :param a: Argument a
    :param b: Argument b
    :param c: Argument c
    :return:
    """
    argument_list = [a, b, c]
    min_value = min(argument_list)

    argument_list.remove(min_value)

    return sum(argument_list)


def askUserForNumber():
    """
    The function asks user two input a number. If there is NaN, 0 will be returned
    :return:
    """
    user_number = 0

    try:
        user_number = float(input("Please input a number >>>"))
    except ValueError:
        print("[ERROR]: You input incorrect number. Returning 0 ...")
        return user_number

    return user_number


# Input data
user_argument_a = askUserForNumber()
user_argument_b = askUserForNumber()
user_argument_c = askUserForNumber()

result = my_func(user_argument_a, user_argument_b, user_argument_c)

print(f"my_func result is {result}")
