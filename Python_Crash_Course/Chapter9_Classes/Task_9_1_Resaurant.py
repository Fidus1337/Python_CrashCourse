"""
Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
"""


class Restaurant:
    def __init__(self, restaurant_name='Gousto', cuisine_type='China', number_served=0) -> None:
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.served = number_served

    def describe_restaurant(self):
        """This method"""
        print(f"This is the most beatiful restaurant named {
              self.name}. There you would be met with {self.cuisine} cuisine")

    def open_restaurant(self):
        """Tell everybody that restauran is opened"""
        print("We are opened!")


obj = Restaurant()
obj.describe_restaurant()
obj.open_restaurant()
