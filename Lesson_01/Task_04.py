# Input number
user_number = int(input("Please input positive integer number >>> "))
user_digits_collection = list(str(user_number))

counter = 0
max_Digit = 0

# Looking of the biggest digit
while counter < len(user_digits_collection):
    current_Digit = int(user_digits_collection[counter])
    print(f"Current digit is {current_Digit}")

    if current_Digit > max_Digit:
        max_Digit = current_Digit

    counter += 1

# Output data
print(f"The user number: {user_number}")
print(f"The max digit: {max_Digit}")
