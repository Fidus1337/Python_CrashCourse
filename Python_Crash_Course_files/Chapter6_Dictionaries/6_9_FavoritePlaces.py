"""
Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places for
each person. To make this exercise a bit more interesting, ask some friends to
name a few of their favorite places. Loop through the dictionary, and print each
person’s name and their favorite places.
"""
favorite_places_poll = {
    'Daniil': ['Portugalia', 'Ukraine', 'France'],
    'Illia': ['Norvegia', 'Britian', 'France'],
    'Alexander': ['Europe', 'USA', 'Ukraine']
}
for name, places in favorite_places_poll.items():
    print(f'{name}: {places}')
