"""
All versions of foods.py in this section have avoided using
for loops when printing, to save space. Choose a version of foods.py, and
write two for loops to print each list of foods.
"""

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My pizzas:")
for pizza in my_foods:
    print(pizza)

print("\nFriend`s pizza:")
for pizza in friend_foods:
    print(pizza)
