"""
Write a function that stores information about a car in a dictionary. 
The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. 
Call the function with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:

car = make_car('subaru', 'outback', color='blue', tow_package=True)

Print the dictionary that’s returned to make sure all the information was
stored correctly.
"""


def make_car(model_name: str, manufacturer_name: str, **additional_information) -> dict:
    car_info = {'model': model_name, 'manufacturer': manufacturer_name}
    for key_info, val_info in list(additional_information.items()):
        car_info[key_info] = val_info
    return car_info


print(make_car('Subaru', 'Outback', color='green', price=123_000))
