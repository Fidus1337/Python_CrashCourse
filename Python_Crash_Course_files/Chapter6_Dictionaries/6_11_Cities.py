"""
Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information you have stored about it
"""
city_dict = {
    'population': 1_000_000,
    'squares': 856,
    'fact': 'it is beatiful city'
}

cities = {'Kiev': city_dict, 'Lissabon': city_dict, 'Bern': city_dict}

for key, value in cities.items():
    print(f'{key}: {value}')
