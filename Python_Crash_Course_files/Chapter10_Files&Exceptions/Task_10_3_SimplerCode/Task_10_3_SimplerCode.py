from pathlib import Path

path = Path(
    "Python_Crash_Course/Chapter10_Files&Exceptions/Task_10_3_SimplerCode/text_task.txt")

content = path.read_text()

for line in content.splitlines():
    print(line, end='hello')
