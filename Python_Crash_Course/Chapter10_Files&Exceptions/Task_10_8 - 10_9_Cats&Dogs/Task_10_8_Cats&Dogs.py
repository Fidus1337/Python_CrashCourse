"""
Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. 
Move one of the files to a different location on your system, 
and make sure the code in the except block
executes properly.
"""
from pathlib import Path


def extract_text_from_file(path):
    try:
        path = Path(path)
        content = path.read_text()
        names = content.split()
        return names
    except FileNotFoundError:
        print("We haven't found file")
        return None


# Try to extract lists from files
cats = extract_text_from_file(
    "Python_Crash_Course/Chapter10_Files&Exceptions/Task_10_8_Cats&Dogs/cats.txt")
dogs = extract_text_from_file(
    "Python_Crash_Course/Chapter10_Files&Exceptions/Task_10_8_Cats&Dogs/dogs.txt")

# Output lists
print(cats)
print(dogs)
