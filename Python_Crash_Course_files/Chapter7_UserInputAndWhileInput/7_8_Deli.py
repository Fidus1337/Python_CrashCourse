"""
Deli: Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop through
the list of sandwich orders and print a message for each order, such as I made
your tuna sandwich. As each sandwich is made, move it to the list of finished
sandwiches. After all the sandwiches have been made, print a message listing
each sandwich that was made.
"""
sandwich_orders = ['Barkado', 'Lavesa', 'Lotto', 'Cheeseburger']
finished_sandwiched = []

while sandwich_orders:
    for order_index, order in enumerate(sandwich_orders):
        # We ask cooker if he had made sandwich
        sandwich_is_ready = input(f'Have you made sandwich {order}? (yes/no):')
        # If he had done, then we append it to finished_sandwiches and delete from orders
        if sandwich_is_ready.lower() == 'yes':
            finished_sandwiched.append(sandwich_orders.pop(order_index))
            print(f'Sandwich {order} is ready')
        else:
            # If the sandwich is not ready, then we will ask cooker again in the future if is it done
            print(f'Sandwich {order} is not ready')
print(finished_sandwiched)
