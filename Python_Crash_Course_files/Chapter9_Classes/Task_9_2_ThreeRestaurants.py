"""
Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance
"""


class Restaurant:
    def __init__(self, restaurant_name='Gousto', cuisine_type='China') -> None:
        self.name = restaurant_name
        self.cuisine = cuisine_type

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

obj2 = Restaurant(restaurant_name='Who', cuisine_type='Yeah')
obj2.describe_restaurant()
obj2.open_restaurant()

obj3 = Restaurant(restaurant_name='Who you', cuisine_type='Nobody')
obj3.describe_restaurant()
obj3.open_restaurant()
