# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def askUserForNumber(Positive=False):
    """
    The function asks user two input a number. If there is NaN, 0 will be returned
    :return:
    """
    user_number = 0

    try:
        if Positive == True:
            user_number = abs(float(input("Please input a number. Your number will be positive >>>")))
        else:
            user_number = -abs(int(input("Please input a number. Your number will be negative >>>")))

    except ValueError:
        print("[ERROR]: You input incorrect number. Returning 0 ...")
        return user_number

    return user_number


def my_func(positive_number, negative_number):
    """
    The function raises positive number exponent negative number
    :param positive_number:
    :param negative_number:
    :return: float
    """
    result = positive_number ** negative_number

    return result


# Data
positive_user_number = askUserForNumber(Positive=True)
negatve_user_number = askUserForNumber()

print(f"Attempt to pow {positive_user_number} and {negatve_user_number}")
print(f"Result: {my_func(positive_user_number,negatve_user_number)}")


