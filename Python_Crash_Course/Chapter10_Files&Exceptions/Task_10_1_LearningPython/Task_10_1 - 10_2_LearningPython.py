from pathlib import Path

path = Path(
    "Python_Crash_Course/Chapter10_Files&Exceptions/Task_10_1_LearningPython/learning_python.txt")
content = path.read_text()
print(content)

lines = content.splitlines()
str = ""
for line in lines:
    str += line.strip()
print(str)

str = str.replace('python', 'C++')
print(str)
