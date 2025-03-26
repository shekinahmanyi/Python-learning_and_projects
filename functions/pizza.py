
#This syntax works no matter how many parameter the function receives
def make_pizza(*toppings): #The asterisk tells python to make an empty tuple called toppings and pack whatever values it receives from the tuple

    """"Print the list of toppings that have been requested"""
    print("\nMaking a pizza with the following toppings:")

    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')