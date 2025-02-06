# for value in range(0,5):
#     print(value)
# even_numbers = list(range(3,22,3))
# print(even_numbers)

# squares = []
# for value in range(1,11): #Looping through the range of numbers from 1 to 10
#     squares.append(value**2) #Appending the square of the value to the list
# print(squares)

# Using list comprehension
squares = [value **2 for value in range(2,11)] #List comprehension to create a list of squares
print(squares)