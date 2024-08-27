"""
Modify your except block in Exercise 10-7 to fail
silently if either file is missing
"""
from pathlib import Path


def extract_text_from_file(path):
    try:
        path = Path(path)
        content = path.read_text()
        names = content.split()
        return names
    except FileNotFoundError:
        pass
    return None


# Try to extract lists from files
cats = extract_text_from_file(
    "Python_Crash_Course/Chapter10_Files&Exceptions/Task_10_8 - 10_9_Cats&Dogs/cats.txt")
dogs = extract_text_from_file(
    "Python_Crash_Course/Chapter10_Files&Exceptions/Task_10_8 - 10_9_Cats&Dogs/dogs.txt")

# Output lists
print(cats)
print(dogs)
