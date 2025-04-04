"""A class that can be used to represent a car.""" #A module level docstring that describes the purpose of the module.
class Car :

    """A simple attempt to represent a car."""
    def __init__(self, make, model, year) :
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Default Value
    
    def get_descriptive_name(self) :
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage): #Modifying an attribute value through a method
        # """Set the odometer reading to the given value."""
        # self.odometer_reading = mileage 
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles): #Incrementing an attribute value through a method
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car): #we are creating a child class of the parent class Car above

    """Represent aspects of a car, specific to electric vehicles.
     Then initialize attributes specific to an electric car."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year) #this super function allows you to call a method from the parent class
        self.battery_size = 75 #this is a default value for the battery size

    def describe_battery(self): #Here we are defining and adding more attributes to the child class ElectricCar
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        

#Moved this to the my_car.py file
# my_used_car = Car('subaru', 'outback', 2015) 
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()