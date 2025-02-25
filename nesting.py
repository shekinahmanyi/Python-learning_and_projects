# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30): # range() function returns a series of numbers.
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} # Create a new alien.
    aliens.append(new_alien) # Add the new alien to the list.


# Show the first 5 aliens.
for alien in aliens[:5]: # Slice the list to print the first 5 aliens.
    print(alien)
print("...") # Show how many aliens have been created.
# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")
