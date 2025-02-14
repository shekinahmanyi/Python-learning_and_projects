#Understanding Dictionaries

# aliens = {'color': 'green', 'points': 5} # this aliens has 2 key-value pairs color and points

# print(aliens['color']) # we are accessing the value of color key
# print(aliens['points']) # we are accessing the value of points key

# aliens['x_position'] = 0 # adding a new key-value pair to the dictionary
# aliens['y_position'] = 25 # adding a new key-value pair to the dictionary

# print(aliens)

#Tracking the position of an alien that can move at different speeds
aliens = {'x_position': 2, 'y_position': 25, 'speed': 'medium'} # this aliens has 3 key-value pairs x_position, y_position and speed
print(f"Original position: {aliens['x_position']}")
aliens['speed'] = 'fast'
# Move the alien to the right
# Determine how far to move the alien based on its current speed
if aliens['speed'] == 'slow':
    x_increment = 1
elif aliens['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3
#The new position is the old position plus the increment
aliens['x_position'] = aliens['x_position'] + x_increment

print(f"New position: {aliens['x_position']}")

