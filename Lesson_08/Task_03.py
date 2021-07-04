# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
# список только числами. Класс-исключение должен контролировать типы данных элементов списка.


class NotANumberError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


# Script body
my_list = []

while True:
    user_input = input("Please input a number for putting into the list or 'Print' to leave the program >>> ")

    if user_input.lower() == "print":
        break

    try:
        if not user_input.isdigit():
            raise NotANumberError(f"'{user_input}' has not a numerical format")

        my_list.append(int(user_input))
    except NotANumberError as exception:
        print(f"There is an exception: {exception}")

print(f"My data: {my_list}")
