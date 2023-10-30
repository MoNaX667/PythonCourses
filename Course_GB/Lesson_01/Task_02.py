print("The task will convert time in seconds to the following format: <hh:mm:ss>")

# Getting data
source_Time = int(input("Please input the desired time in seconds >>>"))

# Calculation necessary data (hours, minutes, seconds
hours = source_Time // 3600
remaining_time = source_Time % 3600

minutes = remaining_time // 60
seconds = remaining_time % 60

# Formatting the values
if hours < 10:
    hours = f"0{hours}"

if minutes < 10:
    minutes = f"0{minutes}"

if seconds < 10:
    seconds = f"0{seconds}"

# Output
print(f"Target time is {hours}:{minutes}:{seconds}")
