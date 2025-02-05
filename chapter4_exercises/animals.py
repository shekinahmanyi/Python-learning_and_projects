# This program demonstrates the use of for loops in Python
animals = ['dog', 'cat', 'bird', 'fish', 'cow'] #List of animals
for animal in animals: #Iterating through the list
    print(f'A {animal.title()} would make a great pet!') #Printing the value of the list
print('Any of these animals would make a great pet!') #Printing a message after the loop ends
print('\n') #Printing a newline character
print('The first three items in the list are:') #Printing a message
for animal in animals[:3]: #Iterating through the first three items in the list
    print(animal.title()) #Printing the value of the list