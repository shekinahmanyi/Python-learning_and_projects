# Example code for if statements in Python
# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'audi': # check if the first value in the list is 'audi' and if it is, print it in uppercase
#         print(car.upper())
#     else:
#         print(car.title())

#Checking for Inequality
# requested_topping = 'mushrooms'

# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")

#Checking whether a value is in a list
# banned_users = ['martha', 'john', 'joe']
# user = 'martha'
# if user not in banned_users:
#     print(f"{user.title()}, you can post a response if you wish.")
# else:
#     print(f"{user.title()}, you are banned from posting responses.")

#Boolean Expressions
# game_active = True
# can_edit = False
# print(game_active)

#exercise
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')

# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')

#If-Else Statements
# age = 12
# if age >= 18:
#     print("You are old enough to vote!")
#     print("Have you registered to vote yet?")
# else:
#     print("Sorry, you are too young to vote.")
#     print("Please register to vote as soon as you turn 18!")

#The if-elif-else Chain
age = 12
if age < 4:
    price = 0
elif age < 18:
    price =25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")

#if age is even and greater than 20, print "Even and greater than 20"
# age = 22
# if age % 2 == 0 and age > 20:
#     print("Even and greater than 20")
#if age is odd or less than 20, print "Odd or less than 20"
# if age % 2 != 0 or age < 20:
#if age is even and in the inclusive range of 2 to 5, print "Even and in the inclusive range of 2 to 5"
# if age % 2 == 0 and age >= 2 and age <= 5:
