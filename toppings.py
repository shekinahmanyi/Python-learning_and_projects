#Using If Statements with Lists
# requested_topping = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_topping:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print(f"Adding {requested_topping}.")

# print("\nFinished making your pizza!")

#Checking That a List Is Not Empty
# requested_topping = []
# if requested_topping:
#     for requested_topping in requested_topping:
#         print(f"Adding {requested_topping}.")
# print("\nFinished making your pizza!")

#Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese'] #we first have a list of available toppings in the pizza shop
requested_toppings = ['mushrooms', 'french fries', 'extra cheese'] #then we have a list of requested toppings from the customer
for requested_topping in requested_toppings: #we loop through the requested toppings of the customer
    if requested_topping in available_toppings: #we check if the requested topping is in the list of available toppings
        print(f"Adding {requested_topping}.") #if the requested topping is in the list of available toppings, we print that we are adding the requested topping
    else: #if the requested topping is not in the list of available toppings, we print that we don't have the requested topping
        print(f"Sorry, we don't have {requested_topping}.") #if the requested topping is not in the list of available toppings, we print that we don't have the requested topping
print("\nFinished making your pizza!") #we print that we have finished making the pizza