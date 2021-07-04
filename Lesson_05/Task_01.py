# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

user_string = "No Data"
user_file = "UserData.txt"
user_file_stream = open(user_file, 'w')

while(user_string != ""):
    user_string = input("Please input any string. Leave an empty string and press Enter to leave the program: ")
    user_file_stream.write(f"{user_string}\n")

# Closing write stream
user_file_stream.close()

# Output data, opening read stream
user_file_stream = open(user_file, 'r')
print(f"The file contains:\n {user_file_stream.read()}")

# Closing read stream
user_file_stream.close()
