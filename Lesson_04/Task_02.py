# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

# Data
start_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = []

# Display list's element, which bigger than previous one
element_index = 1

while element_index < len(start_list):
    current_item = start_list[element_index]
    previous_element = start_list[element_index-1]

    if current_item > previous_element:
        result_list.append(current_item)

    element_index += 1

print(f"Start collection: {start_list}")
print(f"Result collection: {result_list}")
