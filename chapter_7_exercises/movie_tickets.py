# Exercise 7-5: Movie Tickets   

prompt = "\nPlease enter your age:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True: # this is an infinite loop
    age = input(prompt)
    if age == 'quit':
        break
    else: # this is the else block for the if statement
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age < 13:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")
        continue

print("Thank you for purchasing your tickets!") # this is outside the loop
    
