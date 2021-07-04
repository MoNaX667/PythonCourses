# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,

print("The program generates a range of number from your start point to next 10 values")

while True:

    try:
        user_start_number = int(input("Please input start number >>> "))
    except ValueError:
        print("It seems, you put not a number. Please try again ....")
        continue

    break

result_collection = [value for value in range(user_start_number, user_start_number + 10)]

print(f"You input the next start number: {user_start_number}")
print(f"Your collection: {result_collection}")
