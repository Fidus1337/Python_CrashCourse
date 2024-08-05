"""
Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do
each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.
"""
# Exercise 7_4
# chosen_toppings = []
# input_value = ''
# input_time = 0

# while (input_value.title() != 'Quit'):
#     input_time += 1
#     # User should input topping
#     input_value = input('Input topping or quit menu: ')
#     # We are checking if we have Quit value
#     if input_value.title() != 'Quit':
#         chosen_toppings.append(input_value)
#     else:
#         break

# # print toppings
# print(chosen_toppings)

# # print how long the cicle worked
# print(f'How much was used input: {input_time}')

# Exercise 7_5
input_age = 'Nothing'
input_name = 'Nothing'
index = 0
while (input_name.title() != 'Quit'):
    # inputting name or choosing quit menu
    input_name = input('Input your name or quit menu: ')
    if input_name.title() != 'Quit':
        # inputting age
        input_age = int(input(f'Input your age, {input_name}: '))
    else:
        break  # if we got something unpredictable

    # message about ticket price
    if input_age < 3:
        print('Your ticket is free!')
    elif input_age >= 3 and input_age <= 12:
        print('Your ticker costs 10$')
    elif input_age > 12:
        print('Your ticket costs 15$')
