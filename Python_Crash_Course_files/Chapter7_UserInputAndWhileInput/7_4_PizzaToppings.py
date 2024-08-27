"""
Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping, print
a message saying you’ll add that topping to their pizza.
"""
chosen_toppings = []
input_value = ''
while (input_value.title() != 'Quit'):
    # User should input topping
    input_value = input('Input topping or quit menu: ')
    # We are checking if we have Quit value
    if input_value.title() != 'Quit':
        chosen_toppings.append(input_value)
print(chosen_toppings)  # print values
