from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    sum = 0
    for elem in sequence:
        if type(elem) == int:
            sum += elem
        else:
            interim_result = seq_sum(elem)
            sum += interim_result

    return sum
    pass

