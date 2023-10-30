# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

source_file_path = "Task_04_Data.txt"
result_collection = []
translate_collection = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

try:
    with open(source_file_path, "r", encoding='utf-8') as lines:
        for line in lines:
            elements = line.split(" - ")
            print(f"Elements: {elements}")

            if elements[0] in translate_collection:
                new_translation_value = translate_collection[elements[0]]
                print(f"new_translation_value: {new_translation_value}")
                result_collection.append(f"{new_translation_value} - {elements[1]}")
except IOError:
    print(f"There is an IO issue on reading {source_file_path} file")

# Write output
try:
    file_input = open("Task_04_Updated.txt", "w", encoding='utf-8')
    file_input.writelines(result_collection)
except IOError:
    print("I\O error. Please double check the code input")
finally:
    file_input.close()
