#exercise 6.8 Pets
#Making several dictionaries of Pets and storing them in a list called pets
pet_1 = {'name': 'dog', 'owner': 'John'}
pet_2 = {'name': 'cat', 'owner': 'Jane'}
pet_3 = {'name': 'parrot', 'owner': 'Jack'}
pets = [pet_1, pet_2, pet_3]
#Looping through the list of pets
for pet in pets:
    print(f"Pet Name: {pet['name']}")
    print(f"Owner: {pet['owner']}")
    print("\n")