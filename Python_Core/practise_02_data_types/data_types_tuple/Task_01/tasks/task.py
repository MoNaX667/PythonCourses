from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    s = str(num)
    interim_list = []

    for elem in s:
        interim_list.append(int(elem))

    result_tuple = tuple(interim_list)
    return result_tuple

