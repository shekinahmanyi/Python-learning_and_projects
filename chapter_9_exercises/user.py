
class User :
    """A class representing a user in the system."""
    def __init__(self, first_name, last_name, age, location):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0 # Initialize login attempts to 0

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User: {self.first_name} {self.last_name}, Age: {self.age}, Location: {self.location}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name}! Welcome back!")

    def increment_login_attempts(self):
        """Increment the number of login attempts."""
        self.login_attempts += 1

first_user = User("John", "Doe", 30, "New York")
second_user = User("Jane", "Smith", 25, "Los Angeles")
third_user = User("Alice", "Johnson", 28, "Chicago")
print(f"First User: {first_user.first_name} {first_user.last_name}, Age: {first_user.age}, Location: {first_user.location}")
print(f"Second User: {second_user.first_name} {second_user.last_name}, Age: {second_user.age}, Location: {second_user.location}")
print(f"Third User: {third_user.first_name} {third_user.last_name}, Age: {third_user.age}, Location: {third_user.location}")
first_user.describe_user()  
first_user.greet_user()
first_user.increment_login_attempts() # Increment login attempts
print(f"Login attempts for {first_user.first_name}: {first_user.login_attempts}")
second_user.describe_user()
second_user.greet_user()
second_user.increment_login_attempts() # Increment login attempts
print(f"Login attempts for {second_user.first_name}: {second_user.login_attempts}")
third_user.describe_user()
third_user.greet_user()
third_user.increment_login_attempts() # Increment login attempts
print(f"Login attempts for {third_user.first_name}: {third_user.login_attempts}")
# The code defines a User class with methods to describe the user, greet the user, and increment login attempts.