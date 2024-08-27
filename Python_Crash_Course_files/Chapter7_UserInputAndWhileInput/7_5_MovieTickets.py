"""
Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket
"""
clients_age = {'John': 3, 'Jonathan': 4, 'Joan': 24, 'Jeferson': 76}
for client_name, client_age in list(clients_age.items()):
    if client_age < 3:
        print(f'{client_name} the ticket is free')
    elif client_age >= 3 and client_age <= 12:
        print(f'{client_name} you should pay $10')
    elif client_age > 12:
        print(f'{client_name} you should pay $15')
