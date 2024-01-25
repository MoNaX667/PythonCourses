from typing import Any, Tuple, List


def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    counter = 0
    result_list = []

    if( len(lst) == 1):
        return []

    while (counter < len(lst) - 1):
        result_list.append(tuple((lst[counter], lst[counter + 1])))
        counter += 1

    return result_list

