
#This syntax works no matter how many parameter the function receives
def make_pizza(size,*toppings): #The asterisk tells python to make an empty tuple called toppings and pack whatever values it receives from the tuple

    """"Print the list of toppings that have been requested"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:") 
   
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')