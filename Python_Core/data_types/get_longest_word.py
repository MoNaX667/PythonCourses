"""
Implement a function get_longest_word(s: str) -> str which returns the longest word in the given string. The word can contain any symbols except whitespaces
(' ', '\n', '\t' and so on). If there are multiple longest words in the string with the same length return the word that occurs first.
Example:

    get_longest_word('Python is simple and effective!')
    'effective!'

"""

def get_longest_word( s: str) -> str:
    words_array = s.split(" ")
    init_word = " "

    for i in words_array:
        if(len(init_word)<len(i)):
            init_word = i
        else:
            print(f"Current word {init_word} is bigger than {i}")

    return init_word

result = get_longest_word('Python is simple and effective!')

print(f"The longest word is \"{result}\"")
