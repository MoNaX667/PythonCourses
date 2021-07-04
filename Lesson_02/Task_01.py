#Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

# Data
different_types_list = [1, 2, "SomeValue", ("blue", "green")]

# Determining an element's type
for element in different_types_list:
    print(
        f"element {element} has type {type(element)}"
    )
