from typing import Dict

def get_dict(s: str) -> Dict[str, int]:
    s = s.lower()
    result_dictionary = {}

    for char in s:
        if result_dictionary.keys().__contains__(char):
            current_value = result_dictionary.get(char)
            result_dictionary[char] = current_value + 1
        else:
            result_dictionary.update({f"{char}": 1})

    return result_dictionary


