"""
Cubes: A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube.
"""

"""
Use a list comprehension to generate a list of the first
10 cubes.
"""

test_list1 = list(range(1, 10 + 1)) # first task
print(test_list1)
new_list = [] # it will be the list with multiplies

for value in test_list1:
    new_list.append(value ** 2)

print(f"List of cubes 1: {test_list1}")


test_list2 = [value ** 2 for value in range(1, 10 + 1)] # second task

print(f"List of cubes 2: {test_list2}")