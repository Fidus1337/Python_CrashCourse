"""
Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dumps() to store this number in a file. 
Write a separate program that reads in this value and prints the message 
“I know your favorite
number! It’s _____.”
"""
from pathlib import Path
import json

path = Path(
    "Python_Crash_Course/Chapter10_Files&Exceptions/Task_10_11-10_12_FavoriteNumber/favorite_number.json")
if path.exists():
    with open(path, 'r') as file:
        favorite_number = json.load(file)
    print(f"Your favorite number is {favorite_number}")
else:
    favorite_number = input("Input your favorite number: ")
    with open(path, 'w') as file:
        json.dump(favorite_number, file)
    print("Program remembers your favorite number")
