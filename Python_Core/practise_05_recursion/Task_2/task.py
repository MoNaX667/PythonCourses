from typing import Any, List
from collections.abc import Iterable

def linear_seq(sequence: List[Any]) -> List[Any]:
    res_list = list()

    for elem in sequence:
        if isinstance(elem, Iterable):
            for interim_elem in linear_seq(elem):
                res_list.append(interim_elem)
        else:
            res_list.append(elem)

    return res_list
    pass

