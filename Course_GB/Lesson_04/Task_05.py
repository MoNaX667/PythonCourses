# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
from functools import reduce

# Generate necessary range
generated_list = [value for value in range(100, 1001) if (value % 2) == 0]
print(f"Result Collection of numbers from 100 to 1001: {generated_list}")

# Multiply elements of the generated range
elements_sum = reduce(lambda first_element, second_element: first_element * second_element, generated_list)

print(f"The multiplication of generated elements is {elements_sum}")