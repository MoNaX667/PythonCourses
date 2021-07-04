# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

# Data
source_collection = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result_collection = [value for value in list(dict.fromkeys(source_collection))]

print(f"Original collection: {source_collection}")
print(f"Result collection: {result_collection}")