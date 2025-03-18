
def get_formatted_name(first_name, last_name, middle_name=''): #Here we are defining a function cal get_formatted_name and making the middle name optional

    """Return a Full name, neatly formatted""" #Docstring to tell what the function does
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"   #we are defining a variable that combines both the first name and the last name
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title() #we now return the full name

#Sample cases on how to get the full name of various people with their different roles
#so the function above(get_formatted_name) is just a simple function we can use to get as many full names as possible
musician = get_formatted_name('Dunsin', 'Oyekan')
print(musician)

writer = get_formatted_name('Shekinah', 'Manyi','Achidi')
print(writer)

farmer = get_formatted_name('Giren', 'Grace')
print(farmer)