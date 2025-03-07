

# height = input("How tall are you, in inches? ")
# height = int(height)

# if height >= 78:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

#letting the user choose when to quit
# prompt = "\nTell me something, and I will repeat it back to you:"   
# prompt += "\nEnter 'quit' to end the program. "

# active = True # flag
# while active: #This loop will run as long as the active flag is True
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)


#using break to exit a loop
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

#using continue in a loop
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue

#     print(current_number)   

#avoiding infinite loops
# x = 1
# while x <= 5:
#     print(x)
#     x += 1

# x = 1
# while x <= 5:
#     print(x)
#     x += 1


#moving items from one list to another
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


#removing all instances of specific values from a list
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)


#filling a dictionary with user input
responses = {}  #empty dictionary

#set a flag to indicate that polling is active
polling_active = True

while polling_active:
    #prompt for the person's name and response
    name = input("\nWhat is your name? ") #prompt for the person's name
    response = input("Which mountain would you like to climb someday? ") #prompt for the person's response

    #store the response in the dictionary
    responses[name] = response 

    #find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
    
#polling is complete. Show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
    