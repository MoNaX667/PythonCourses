# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

user_input = input(
    "Please input numbers separated by spaces> ")

user_words = user_input.split(" ")
numbers = []

for word in user_words:
    possible_number = None

    try:
        possible_number = float(word)
    except ValueError:
        print(f"There is not a number: {word}")
        continue

    numbers.append(possible_number)

file_path = "Task5_05_Result.txt"

with open(file_path, 'w') as stream:
    print(*numbers, file=stream)

print(f"Numbers data in the following file: {file_path}")
print(f"Numbers sum: {sum(numbers)}")
