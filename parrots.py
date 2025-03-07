

# height = input("How tall are you, in inches? ")
# height = int(height)

# if height >= 78:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

#letting the user choose when to quit
prompt = "\nTell me something, and I will repeat it back to you:"   
prompt += "\nEnter 'quit' to end the program. "

active = True # flag
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# message = ""
# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)