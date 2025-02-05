# Book: Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming Exercise 4.11 Pizzas
pizzas = ['pepperoni', 'margherita', 'hawaiian']
for pizza in pizzas:
    print(f'I like {pizza.title()} pizza.')
print('I really love pizza!')
print('\n')
friend_pizzas = pizzas[:] # Copying the list
pizzas.append('vegetarian') # Adding a new pizza to the original list
friend_pizzas.append('meat lovers') # Adding a new pizza to the copied list
print('My favorite pizzas are:') # Printing the original list
for pizza in pizzas: # Looping through the original list
    print(pizza.title()) # Printing the value of the Original list
print('\n')
print("My friend's favorite pizzas are:") # Printing the copied list
for friend_pizza in friend_pizzas: # Looping through the copied list
    print(friend_pizza.title()) # Printing the value of the list
print('\n')

