"""
Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.
"""
from pathlib import Path

path = Path(
    "Python_Crash_Course/Chapter10_Files&Exceptions/Task_10_4_Guest/guest.txt")
guests_name = input("Whais is your name sir? ")
path.write_text(guests_name.strip())

content = path.read_text()

print(repr(content))
