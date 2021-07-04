# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divideNumbers(devidend, devider):
    """
    Function divide two number. The function will return None, if divider or dividend are None, an error will be
    indicated. If divider is 0, an error will be indicated.
    :param devidend:
    :param devider:
    :return float or None:
    """
    print(f"Attempt to devide {devidend} on {devider}")

    if devider != 0 and devider is not None and devidend is not None:
        return devidend / devider

    print(f"You are trying to divide on {devider}. The operation would fail. Returning None ...")
    return None


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


# Preset data
user_dividend = askUserForNumber()
user_divider = askUserForNumber()

# Calculation
result = divideNumbers(user_dividend, user_divider)

print(f"Result: {result}")
