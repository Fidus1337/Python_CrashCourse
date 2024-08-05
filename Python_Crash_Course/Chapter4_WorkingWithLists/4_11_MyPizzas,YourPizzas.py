"""
My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56).
Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the
following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My
friend’s favorite pizzas are:, and then use a for loop to print the second list.
Make sure each new pizza is stored in the appropriate list
"""

my_pizzas = ["peperoni", "havaii", "threecheeses"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("new_pizza")  # 1 task

friend_pizzas.append("different_pizza")  # 2 task

# 3 task
print("My pizzas:")
for pizza in my_pizzas:
    print(pizza)


print("\nFriend's pizzas:")
for pizza in friend_pizzas:
    print(pizza)
