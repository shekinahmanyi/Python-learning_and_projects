
#Exercise 7-4: Pizza Toppings

prompt = "\nPlease enter a topping you would like on your pizza:"
prompt += "\n(Enter 'quit' when you are finished.) "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(f"Adding {message} to your pizza!")
    else:
        print("Your pizza is ready!")
        break   

    