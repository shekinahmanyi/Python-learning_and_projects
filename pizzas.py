# Store Information about a pizza being ordered.
pizza = { 
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'], # created a list of toppings in a dictionary
}
# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza " # Accessing the value of 'crust' key and we are using f-string to format the output.
      "with the following toppings:")
for topping in pizza['toppings']: # Accessing the value of 'toppings' key.
    print("\t" + topping)

