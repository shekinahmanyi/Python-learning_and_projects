
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

class ElectricCar(Car): #we are creating a child class of the parent class Car above

    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year) #this super function allows you to call a method from the parent class

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())