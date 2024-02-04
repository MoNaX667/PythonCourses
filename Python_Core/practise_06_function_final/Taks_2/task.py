from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:
    result_collection = []
    prev_index = 0

    for index in indexes:
        if index > prev_index and index <= len(s):
            result_collection.append(s[prev_index:index])
            prev_index = index

    # Append the remaining part of the string
    result_collection.append(s[prev_index:])

    return result_collection

print(split_by_index("no luck", [42]))