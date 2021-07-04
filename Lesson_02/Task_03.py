# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Data
user_season_by_dictionary = None
user_season_by_list = None
user_defined_month = None

# Input data and check the number to match the condition from 1 to 12
while True:
    user_defined_month = int(input("Please input month's number from 1 to 12 >>> "))

    if 1 <= user_defined_month <= 12:
        break
    else:
        print("Hey, you input an incorrect number, please go back and try one more time")
        continue

# Seasons collections and service data(seasons tuple)
seasons_by_order = ("Winter", "Spring", "Summer", "Fall")
list_season_collection = [{1, 2, 12}, {3, 4, 5}, {6, 7, 8}, {9, 10, 11}]

dictionary_season_collection = {
    "Winter": {1, 2, 12},
    "Spring": {3, 4, 5},
    "Summer": {6, 7, 8},
    "Fall": {9, 10, 11}
}

# Working with list
count = 0

for season_index_set in list_season_collection:
    if user_defined_month in season_index_set:
        user_season_by_list = seasons_by_order[count]
        break
    else:
        count += 1

# Working with dictionary
for season in dictionary_season_collection.keys():
    if user_defined_month in dictionary_season_collection[season]:
        user_season_by_dictionary = season
        break

# Output data
print(f"User set the following month's value: {user_defined_month}")
print(f"Current user's season by list is {user_season_by_list}")
print(f"Current user's season by dictionary is {user_season_by_dictionary}")
