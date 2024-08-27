"""
An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote in
Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
will work; just pick the one you like better. Add an attribute called flavors that
stores a list of ice cream flavors. Write a method that displays these flavors.
Create an instance of IceCreamStand, and call this method.
"""


class Restaurant:
    """Restaurant work logic"""

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

    def set_number_served(self, new_value: int):
        """Set served variable"""
        self.served = new_value

    def increment_number_served(self):
        """Increase count of guests"""
        self.served += 1


class IceCreamStand(Restaurant):
    def __init__(self, flavors: list = ["Milk", "Salt-caramel"], restaurant_name='Gousto',
                 cuisine_type='China', number_served=0) -> None:
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.ice_cream_flavors = flavors

    def display_flavors(self):
        """Displays all flavors of ice cream available in this store"""
        print(self.ice_cream_flavors)


restaurant = IceCreamStand()
restaurant.display_flavors()
