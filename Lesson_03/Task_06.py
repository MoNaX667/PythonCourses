# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def capitalise(user_word):
    """
    Function capitalise the word

    :param user_word:
    :return:
    """
    return user_word.capitalize()

def validate_latin_word(user_word):
    """
    Function ask user to input the string and validate the letters. The letters should be in the range a-z

    :param user_word: user word to validate
    :return: str, None
    """
    a_letter_code = ord("a")
    z_letter_code = ord("z")

    for char in user_word:
        if a_letter_code <= ord(char) and ord(char) <= z_letter_code:
            continue
        print(f"There is an incorrect symbol {char}. It should be in a range a-z")
        return None

    return user_word


sentence = str(input("Please input a string with usage letters from the next list a-z. "
                     "Incorrect words would not be capitalised >>> "))

result_collection = []
words_collection = sentence.split()

for word in words_collection:
    verification_result = validate_latin_word(word)
    result_word = word

    if verification_result is not None:
        result_word = capitalise(user_word=verification_result)
        print(f"User word {word} was capitalised to {result_word}")
    else:
        print(f"The word ({word}) would not be capitalised")

    result_collection.append(result_word)

print(f"Sentence was changed: {' '.join(result_collection)}")







