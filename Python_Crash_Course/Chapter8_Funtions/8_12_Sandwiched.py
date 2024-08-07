"""
Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich that’s
being ordered.
Call the function three times, using a different number of arguments each time
"""
desired_items = ['cucumber', 'pepper', 'banana', 'ketchup']


def make_sandwich(*desired_items_to_sandwich):
    """This function creates sandwich with desired items or filling"""
    print(f'So, your sandwich will have: {desired_items_to_sandwich}')


make_sandwich('cheese', 'cucumber')
make_sandwich('cheese', 'ketchup', 'ice_cream')
make_sandwich('banana')
