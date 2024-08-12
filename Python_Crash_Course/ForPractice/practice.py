from pathlib import Path
import json

path = Path('Python_Crash_Course/ForPractice/names.json')
if path.exists():
    contents = path.read_text()
    names = json.loads(contents)
    print(f"Welcome back, {names}!")
else:
    names = []  # We are going to load an array of names
    while True:
        username = input("What is your name? (or q to quit poll) ")
        contents = json.dumps(names)
        if username == 'q':
            break
        else:
            names.append(username)
    with open(path, 'w') as file:
        json.dump(names, file, indent=4)
    print("We'll remember you all when you come back!")
