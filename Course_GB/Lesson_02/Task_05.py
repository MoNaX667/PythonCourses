# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

# Data
numbers_collection = [3, 2, 1]

# Work cycle
while True:
    user_command = input("Please input your integer number. please input EXIT to leave the program >>> ")
    user_number = None

    # Parse user's input
    if user_command == "EXIT":
        print("Have a nice day")
        break
    else:
        try:
            user_number = int(user_command)
        except ValueError:
            print(f"Hey, you input a non integer number. You number is {user_command}. Please try again and read "
                  f"instructions carefully")
            continue

    # Adding a new element to the collection and order it following the rules
    numbers_collection.append(user_number)
    numbers_collection.sort()
    numbers_collection.reverse()

    # Output data
    print(f"User number: {user_number}")
    print(f"Updated collection state: {numbers_collection}")


