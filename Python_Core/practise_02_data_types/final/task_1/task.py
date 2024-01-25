from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    origin_data = lst
    result_data = set()

    for item in origin_data:

        for key in item.keys():
            if result_data.__contains__(item[key]):
                print(f"Contains {item[key]} ")
            else:
                result_data.add(item[key])


    return result_data
    pass

