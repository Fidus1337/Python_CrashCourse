"""
10-5. Guest Book: Write a while loop that prompts users for their name. Collect
all the names that are entered, and then write these names to a file called
guest_book.txt. Make sure each entry appears on a new line in the file.
"""
from pathlib import Path

path = Path(
    "Python_Crash_Course/Chapter10_Files&Exceptions/Task_10_4-10_5 Guest book/guest.txt")
poll_is_active = True
content = path.read_text()

while poll_is_active:
    input_name = input("What is your name? ")
    content += input_name + '\n'

    wants_continue_input = input("Do you want continue poll? (yes/no) ")
    if wants_continue_input.lower() == "yes":
        continue
    else:
        print("The poll is finished")
        break
path.write_text(content)

print(repr(content))

# Print all names
name_list = []
for line in content.splitlines():
    name_list.append(line.strip())
print(name_list)
