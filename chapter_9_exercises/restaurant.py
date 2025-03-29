
class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 # Initialize number of customers served but not passed as an argument

    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Indicate that the restaurant is open."""
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self, number):
        """Set the number of customers served."""
        self.number_served = number

    def increment_number_served(self, number):
        """Increment the number of customers served."""
        self.number_served += number

my_restaurant = Restaurant("The Great Eatery", "Italian")
print(f"Restaurant Name: {my_restaurant.restaurant_name}")
print(f"Cuisine Type: {my_restaurant.cuisine_type}")
my_restaurant.describe_restaurant() 
my_restaurant.open_restaurant()
my_restaurant.set_number_served(10)
print(f"Number of customers served: {my_restaurant.number_served}")