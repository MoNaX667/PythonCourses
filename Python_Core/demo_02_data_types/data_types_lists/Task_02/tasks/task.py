from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    my_list = []

    for i in range(1,(n+1)):
        if not i%3 and not i%5:
            my_list.append("FizzBuzz")
        elif not i%3:
            my_list.append("Fizz")
        elif not i%5:
            my_list.append("Buzz")
        else:
            my_list.append(i)
    return my_list

