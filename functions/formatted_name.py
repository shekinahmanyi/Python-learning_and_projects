
def get_formatted_name(first_name, last_name): #Here we are defining a function cal get_formatted_name

    """Return a Full name, neatly formatted""" #Docstring to tell what the function does
    full_name = f"{first_name} {last_name}"   #we are defining a variable that combines both the first name and the last name

    return full_name.title() #we now return the full name

#Sample cases on how to get the full name of various people with their different roles
#so the function above(get_formatted_name) is just a simple function we can use to get as many full names as possible
musician = get_formatted_name('Dunsin', 'Oyekan')
print(musician)

writer = get_formatted_name('Shekinah', 'Manyi')
print(writer)

farmer = get_formatted_name('Giren', 'Grace')
print(farmer)