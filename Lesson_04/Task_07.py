# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

# Import functions
from math import factorial


def fact(max_factorial_value):
    """
    Function generates factorials from 1 to n
    :param max_factorial_value: max factorial value
    """
    for index in range(1, max_factorial_value + 1):
        yield factorial(index)


# Data
while True:
    try:
        max_factorial_value = int(input('Please input number (1 ... n) of factorials that you want to see >>>: '))

        if max_factorial_value < 1:
            print("Seems, you input negative number or null. Please try again")
            continue

        break
    except ValueError:
        print("Seems, you input non a number. Please try again")
        continue

print(f"You want to get factorials values for {max_factorial_value} element(s)")
result_generator = fact(max_factorial_value)

for element in result_generator:
    print(f"Factorial value: {element}")
