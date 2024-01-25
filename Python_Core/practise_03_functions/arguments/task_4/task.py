from typing import List, Dict

def combine_dicts(*args:List[Dict[str, int]]) -> Dict[str, int]:
    '''
        Implement a function, that receives changeable number of dictionaries (keys - letters, values - numbers)
        and combines them into one dictionary.

        Dict values should be summarized in case of identical keys
    '''
    result_dict = {}

    if len(args) != 0:
        result_dict = args[0]

    count = 1

    while (count < len(args)):
        for elem in args[count].keys():
            if result_dict.keys().__contains__(elem):
                result_dict[elem] += args[count][elem]
            else:
                result_dict.update({elem:args[count][elem]})

        count += 1

    return result_dict

    pass



