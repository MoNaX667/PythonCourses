# Libs loading:
import calendar
from datetime import datetime

# Get current day of week
day_number = datetime.today().weekday()
day_of_week = calendar.day_name[day_number]

# Variables area
bot_name = "Timofey"
weather = "stormy"

user_name = "Empty"


print("Hello! I'm AI assistant. My name is {0}".format(bot_name))
print("Message from {0}: What is your name?".format(bot_name))
user_name = input("Type your name here >> ")

print(f"Nice to meet you {user_name}")
print("Message from {0}:{2}, Today is {1}".format(bot_name,day_of_week,user_name))
print(f"Message from {bot_name}:{user_name}, The weather today is {weather}")