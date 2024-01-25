from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    res_dictionary = {}
    target_num_array = range(1,num+1)

    for elem in target_num_array:
        res_dictionary.update({elem:pow(elem,2)})
    return res_dictionary
    pass
