"""
Make a list of your favorite fruits, and then write a series of
independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit
is in your list. If the fruit is in your list, the if block should print a statement,
such as You really like bananas!
"""

favorite_fruits = ['banana', 'mango', 'apple']
favorite_fruit = input("What is you favorite fruit? ")
favorite_fruit.lower()

if favorite_fruit.lower() in favorite_fruits:
    print(f'You like {favorite_fruit}, it is in the list')
else:
    print(f'You like {favorite_fruit}')
