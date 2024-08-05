"""
Think of things you could store in a list. For example, you
could make a list of mountains, rivers, countries, cities, languages, or anything
else you’d like. Write a program that creates a list containing these items and
then uses each function introduced in this chapter at least once.
"""

random_list = ["Mountain", "Ship", "Coin", "John", "Thomas", "Elena"]

print(random_list)
print(f"Sorted list with sorted() funtion by alphabetical order: {sorted(random_list, reverse=False)}\n")

print(f"Sorted list with sorted() funtion by reversed-alphabetical order: {sorted(random_list, reverse=True)}\n")

print(f"Total number of titles with len() funtion: {len(random_list)}\n")

random_list.reverse()
print(f"Changing the order of the list with reverse() method: {random_list}\n")

random_list.reverse()
print(f"Changing back the order of the list with reverse() method: {random_list}\n")

random_list.sort()
print(f"Sorting list with sort() method, alphabetical sorting: {random_list}\n")

random_list.sort(reverse=True)
print(f"Sorting list with sort() method, reversed-alphabetical sorting: {random_list}\n")

print(f"Deleting the last element in list, with pop method: {random_list.pop()}")
print(random_list, "\n")

del random_list[0]
print(f"Deleting the first element, with del function: {random_list}\n")

random_list.append("Janna")
print(f"Adding new element 'Janna' with append function: {random_list}\n")

random_list.remove("John")
print(f"Removing the element with string 'John': {random_list}\n")