# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

# Get user data and generate words collection
original_string = input("Please input your words separated by whitespaces >>>")
user_words_collection = original_string.split()

print(f"Original string: {original_string}")

# Output words following by task rules
count = 1

for word in user_words_collection:
    output_word = word

    # Check the word's length
    if len(word) > 10:
        output_word = output_word[0:10]

    print(f"Word #{count}: {output_word}")
    count += 1
