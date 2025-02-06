#counting to twenty
numbers = list(range(1,21)) #List of numbers from 1 to 20
print(numbers)

#counting to a million
numbers = list(range(1,1000001)) #List of numbers from 1 to 1000000
print(numbers)

#summing a million
numbers = list(range(1,1000001)) #List of numbers from 1 to 1000000
print(sum(numbers))

#odd numbers
numbers = list(range(1,21,2)) #List of odd numbers from 1 to 20
print(numbers)

#threes
numbers = list(range(3,31,3)) #List of numbers from 3 to 30 in multiples of 3
print(numbers)

#Cubes
cubes = [value **3 for value in range(1,11)] #List comprehension to create a list of cubes
print(cubes)

#Cubes using a loop
cubes = []
for value in range(1,11): #Looping through the range of numbers from 1 to 10
    cubes.append(value**3) #Appending the cube of the value to the list
print(cubes)