"""
A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the
change.
• The restaurant changes its menu, replacing two of the items with different
foods. Add a line that rewrites the tuple, and then use a for loop to print
each of the items on the revised menu
"""

menu = ("lazanna", "pizza", "pasta", "kebab")
for food in menu:
    print(food)

new_menu = [food for food in menu]
print(new_menu)

new_menu[0] = "another_food"
new_menu[1] = "another_food"

print(new_menu)
