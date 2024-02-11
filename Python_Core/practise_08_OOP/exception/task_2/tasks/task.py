from typing import Union

def divide(str_with_ints: str) -> Union[float, str]:
    try:
        a, b = map(int, str_with_ints.split())
        return float(a) / float(b)
    except ValueError:
        return f"Error code: invalid literal for int() with base 10: '{str_with_ints.split()[1]}'"
    except ZeroDivisionError:
        return f"Error code: division by zero"