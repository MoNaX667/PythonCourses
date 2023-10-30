# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# Generation lists content
first_original_user_list = (input("Please input some values to generate first list. Use whitespace as separator >>>")
                            ).split()
second_original_user_list = (input("Please input some values to generate second list. Use whitespace as separator  >>>")
                             ).split()

# Swapping relevant index values
count = 0

while count < len(first_original_user_list) and count < len(second_original_user_list):
    first_original_user_list[count], second_original_user_list[count] = second_original_user_list[count], \
                                                                        first_original_user_list[count]
    count += 1

# Output results
print(f"Updated first list is {first_original_user_list}")
print(f"Updated second list is {second_original_user_list}")
