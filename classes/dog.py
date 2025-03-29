
#Creating the Dog Class

class Dog: #We are creating a class called Dog

    """A Simple Attempt to Model a Dog"""

    def __init__(self, name, age): #This method is called a constructor and it is used to initialize the attributes of the class

        """Initiate name and age attributes"""

        self.name = name #Attribute for the dog's name

        self.age = age #Attribute for the dog's age

    def sit(self): #A function called Sit which is the same thing as the method because it is inside the class

        """Simulate a dog sitting in response to a command"""

        print(f"{self.name} is now sitting.")

    def roll_over(self): #A method called roll_over which is the same thing as a function

        """Simulate rolling over in response to a command"""

        print(f"{self.name} rolled over")

my_dog = Dog("Willie", 6) #Creating an instance of the Dog class called my_dog
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.") #Printing the name of the dog
print(f"My dog is {my_dog.age} years old.") #Printing the age of the dog


my_dog.sit() #Calling the sit method on the my_dog instance
my_dog.roll_over() #Calling the roll_over method on the my_dog instance

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit() #Calling the sit method on the your_dog instance
your_dog.roll_over() #Calling the roll_over method on the your_dog instance



