"""
Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet.
"""
pets_information = {
    'age': 5,
    'owner_name': 'Danil'
}

pets = {
    'Garik': pets_information,
    'Kisia': pets_information,
    'Mura': pets_information
}

for pet in pets:
    print(f'{pet}: {pets[pet]}')
