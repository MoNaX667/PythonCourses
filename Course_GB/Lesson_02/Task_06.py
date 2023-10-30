# *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.

# Data
goods_collection = []
analysis_collection = []

# Welcome
print("You are welcome in warehouse program!")

# Filling goods collection
goods_counter = 1

while True:

    # Goods characteristics
    good_name = None
    good_cost = None
    good_quantity = None
    good_unit = None
    operator_command = None

    operator_command = input("Please input a command (EXIT to leave the program, ADD to add a new good, ANALYSIS to "
                             "get current warehouse state) >>>")

    if operator_command == "ADD":

        # Filling good's data by user
        good_name = input("Please input good's name: ")

        # Validate costs and quantity number format
        while True:

            try:
                good_cost = float(input("Please input good's cost: "))
            except ValueError:
                print("Hey, seems you are trying to input an incorrect cost. Please try again.")
                continue

            try:
                good_quantity = float(input("Please input good's quantity: "))
            except ValueError:
                print("Hey, seems you are trying to input an incorrect quantity. Please try again.")
                continue

            break

        good_unit = input("Please input good's unit")

        # Adding new element
        goods_collection.append((goods_counter, {"Name": good_name, "Cost": good_cost, "Quantity": good_quantity, "Unit": good_unit}))
        print(f"New element was successfully added: {goods_collection[(goods_counter-1)]}")

        # Increment goods counter
        goods_counter += 1

    elif operator_command == "ANALYSIS":

        print(f"======= ANALYSIS =======")

        # ANALYSIS list data
        names_list = []
        costs_list = []
        quantity_list = []
        unit_list = []

        for good in goods_collection:
            names_list.append(good[1]["Name"])
            costs_list.append(good[1]["Cost"])
            quantity_list.append(good[1]["Quantity"])
            unit_list.append(good[1]["Unit"])

        # Generate ANALYSIS collection
        analysis_collection = {
            "Name": names_list,
            "Cost": costs_list,
            "Quantity": quantity_list,
            "Unit": unit_list
        }

        print(f"Warehouse data: ")

        for point in analysis_collection.keys():
            print(f"{point}: {analysis_collection[point]}")

    elif operator_command == "EXIT":

        print("Exiting the program ... Good luck")
        break

    else:
        print(f"Unknown command: <{operator_command}>.Please double check the instructions")
