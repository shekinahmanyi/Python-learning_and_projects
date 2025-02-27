#Dictionary in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
# Looping through the dictionary
for username, user_info in users.items(): # The items() method returns a list of key-value pairs.
    print(f"\nUsername: {username}") # Accessing the key of the dictionary.
    full_name = f"{user_info['first']} {user_info['last']}" # Accessing the values of the dictionary.
    location = user_info['location'] # Accessing the values of the dictionary.
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")