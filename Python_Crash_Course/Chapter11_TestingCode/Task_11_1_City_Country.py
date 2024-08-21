"""
Write a function that accepts two parameters: a city name
and a country name. The function should return a single string of the form
City, Country, such as Santiago, Chile. Store the function in a module called
city_functions.py, and save this file in a new folder so pytest won’t try to run the
tests we’ve already written.
Create a file called test_cities.py that tests the function you just wrote.
Write a function called test_city_country() to verify that calling your function
with values such as 'santiago' and 'chile' results in the correct string. Run the
test, and make sure test_city_country() passes.
"""


def format_location(city: str, country: str, population: int):
    """Return data in pretty format"""
    return f"city - {city.title()}, country - {country.title()}, population - {population}"


print(format_location("Santiago", "Chile", 500000))
