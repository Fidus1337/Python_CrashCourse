"""
Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle.”
"""
def print_dreams(transport_arr):
    """Function for filling comments about the dream transport in an array"""
    for element in transport_arr:
        element[1] = input(f'What do you think about {element[0]}? - ')

dream_transport = [['Hundai',['blank']],
                   ['Aeroplane',['blank']],
                   ['Sudno',['blank']]]
print_dreams(dream_transport) # using the function
print(dream_transport)
