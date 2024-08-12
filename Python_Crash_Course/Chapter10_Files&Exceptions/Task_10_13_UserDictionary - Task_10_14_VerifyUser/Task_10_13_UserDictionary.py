"""
The remember_me.py example only stores one piece of
information, the username. Expand this example by asking for two more pieces
of information about the user, then store all the information you collect in a
dictionary. Write this dictionary to a file using json.dumps(), and read it back
in using json.loads(). Print a summary showing exactly what your program
remembers about the user.
"""
import json
from pathlib import Path

# Путь к файлу
path = Path(
    "Python_Crash_Course/Chapter10_Files&Exceptions/Task_10_13_UserDictionary/remember_me.json")

# Загрузка имени из файла
with open(path, 'r') as file:
    first_name = json.load(file)  # Загрузка имени "John" из файла

# Запрос у пользователя возраста и фамилии
age = int(input("Input your age: "))
last_name = input("What is your last name? ")

# Создание словаря с данными пользователя
user_info = {
    "first_name": first_name,
    "age": age,
    "last_name": last_name
}

# Запись словаря обратно в файл
with open(path, 'w') as file:
    json.dump(user_info, file, indent=3)

# Вывод подтверждающего сообщения
print(f"We have saved your information: {user_info}")

# what we remember about user
print(user_info)
