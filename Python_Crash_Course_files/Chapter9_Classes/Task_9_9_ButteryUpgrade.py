"""
Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capacity to 65 if it isn’t already. Make
an electric car with a default battery size, call get_range() once, and then
call get_range() a second time after upgrading the battery. You should see an
increase in the car’s range
"""


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Filling the tank with fuel"""
        print("The car is full")


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40) -> None:
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrades buttery to the 65 kWh"""
        if self.battery_size != 65:
            self.battery_size = 65
            print("We have upgraded battery to 65-kWh")
        else:
            print("Already upgraded!")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year, places):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.places = places
        self.battery = Battery()

    def fill_gas_tank(self):
        """The electic car cannot be fill with the fuel"""
        print("The electic car cannot be fulled with petrol")


my_leaf = ElectricCar('nissan', 'leaf', 2024, 10)
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
