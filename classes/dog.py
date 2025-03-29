
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


