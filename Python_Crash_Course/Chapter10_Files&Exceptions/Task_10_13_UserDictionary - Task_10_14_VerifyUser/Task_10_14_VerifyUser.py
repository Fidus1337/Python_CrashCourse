"""
The final listing for remember_me.py assumes either that the
user has already entered their username or that the program is running for the
first time. We should modify it in case the current user is not the person who last
used the program.
Before printing a welcome back message in greet_user(), ask the user if
this is the correct username. If it’s not, call get_new_username() to get the correct
username.
"""
import json


def get_new_username() -> str:
    """Asks user print his name"""
    new_name = input("What is your name? ")
    return new_name


def greet_user(name):
    """Greets user"""
    print(f"Hello, {name}!")


path = "Python_Crash_Course/Chapter10_Files&Exceptions/Task_10_13_UserDictionary - Task_10_14_VerifyUser/remember_me.json"

with open(path, 'r') as file:
    recorded_users_name = json.load(file)

# We ask user if recorded name is his
ask_user = input(f"Recorded name {recorded_users_name} is yours? (yes or no):")
if ask_user == "yes":
    greet_user(recorded_users_name)
else:
    new_name = input("Then what is your name? ")
    greet_user(new_name)
    with open(path, 'w') as file:
        json.dump(new_name, file, indent=2)
