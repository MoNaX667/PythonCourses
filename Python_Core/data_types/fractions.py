"""
Create a function that takes two parameters of string type which are fractions with the same denominator and returns a sum expression of these fractions and the sum result.

    For example:

    a_b = '1/3'
    c_b = '5/3'
    get_fractions(a_b, c_b)
    '1/3 + 5/3 = 6/3'

"""


def get_fractions(a_b: str, c_b: str) -> str:
    delimiter = a_b.split("/")[1]
    sum = int(a_b.split("/")[0]) + int(c_b.split("/")[0])
    calculation_result = f"{sum}/{delimiter}"

    return (f"{a_b} + {c_b} = {calculation_result}")

a_b = '1/3'
c_b = '5/3'

result = get_fractions(a_b, c_b)

print(f"{result}")
