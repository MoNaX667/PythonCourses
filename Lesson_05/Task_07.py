# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
# фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:

# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json

profit_company_dictionary = {}
middle_revenue_dictionary = {}
profit = 0
profit_average = 0
counter = 0

with open('Task_07_Data.txt', 'r', encoding='utf-8') as data_list:
    for line in data_list:
        name, firm, earning, damage = line.split()
        profit_company_dictionary[name] = int(earning) - int(damage)

        if profit_company_dictionary.setdefault(name) >= 0:
            profit = profit + profit_company_dictionary.setdefault(name)
            counter += 1

    if counter != 0:
        profit_average = profit / counter
        print(f'Middle revenue - {profit_average:.2f}')
    else:
        print(f'Revenue is poor')

    middle_revenue_dictionary = {'Middle revenue': round(profit_average)}
    profit_company_dictionary.update(middle_revenue_dictionary)

    print(f'Each company revenue - {profit_company_dictionary}')

# Write Json file
with open('Task_07_results.json', 'w', encoding='utf-8') as write_stream:
    json.dump(profit_company_dictionary, write_stream)

