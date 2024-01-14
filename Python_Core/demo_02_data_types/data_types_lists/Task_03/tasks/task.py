from typing import List


def foo(nums: List[int]) -> List[int]:
    result = []
    counter = 0

    while counter < len(nums):

        calculating_list = list(nums)
        calculating_list.remove(calculating_list[counter])
        new_elem = 1

        for elem in calculating_list:
            new_elem *= elem

        result.append(new_elem)
        counter += 1

    return result

