"""
Start with your program from Exercise 9-1 (page 162).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.

Add a method called set_number_served() that lets you set the number of
customers that have been served. Call this method with a new number and print
the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a day of
business
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


obj = Restaurant()
obj.set_number_served(5)
print(obj.served)
obj.increment_number_served()
print(obj.served)
