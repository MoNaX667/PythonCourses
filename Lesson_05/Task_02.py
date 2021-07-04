# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

user_file_path = "Example_02.txt"
counter = 0

with open(user_file_path) as user_file:
    for line in user_file:
        counter += 1
        words_number = len(line.split(" "))

        print(f"String {counter} contains {words_number} word(s)")
        print(f"Line context: {line}")

print(f"The file {user_file_path} contains {counter} string(s)")