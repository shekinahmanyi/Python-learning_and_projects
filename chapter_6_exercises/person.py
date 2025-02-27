#Exercise 6.1 Person

person = {'first_name': 'John', 'last_name': 'Doe', 'age': 25, 'city': 'New York'} # this person has 4 key-value pairs first_name, last_name, age and city
#Making two new dictionaries for two different people and storing and storing all the three dictionaries in a list called people
person_1 = {'first_name': 'Jane', 'last_name': 'Doe', 'age': 30, 'city': 'Los Angeles'}
person_2 = {'first_name': 'Jack', 'last_name': 'Doe', 'age': 35, 'city': 'San Francisco'}
people = [person, person_1, person_2]
#Looping through the list of people
for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print("\n")



# print(person['first_name'])

# print(person['last_name'])

# print(person['age'])

# print(person['city'])

