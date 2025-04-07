#Using a Dictionary to store people's favorite numbers
fav_numbers = {
    'jen': 7,
    'sarah': 3,
    'edward': 5,
    'phil': 9,
}
#Loop through the dictionary and print the person and their favorite number
for name, number in fav_numbers.items():
    print(f"{name.title()}'s favorite number is {number}.")