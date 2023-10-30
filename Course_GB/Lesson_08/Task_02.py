# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class MyZeroDivisionError(Exception):
    text = "Division on null is detected. It is prohibited"

    def __str__(self):
        return self.text


class Number(float):
    def __truediv__(self, other):
        if other is not None and not other:
            raise MyZeroDivisionError

        return Number(float(self) / float(other))


# Script body
exit_code = None

while exit_code != "Exit":
    user_input = input("Please input dividend and delimiter separated by space. Input 'Exit' to leave the program: ")

    if user_input.lower() == "exit":
        exit_code = "Exit"
        continue
    else:
        try:
            dividend, divider = map(Number, user_input.split())
            print(dividend / divider)
        except MyZeroDivisionError as exception:
            print(f"Error: {exception}")
        except ValueError as exception:
            print(f"Error: {exception}")
            break

print("Leaving the program. Have a nice day")
