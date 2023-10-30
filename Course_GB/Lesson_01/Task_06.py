# Inputting data
first_day_distance = float(input("Please input your first day distance in km>>>"))
target_distance = float(input("Please input your desired distance >>>"))
current_distance = first_day_distance
days_in_train = 1

while True:
    # Check results
    if current_distance >= target_distance:
        print(f"You will reach your goal ({target_distance} km) on the {days_in_train}th day")

        break
    else:
        # Do train

        current_distance += (current_distance*0.1)
        days_in_train += 1

print("Work hard champion")
