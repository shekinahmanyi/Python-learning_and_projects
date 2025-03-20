#RETURNING A DICTIONARY

def build_person(first_name, last_name, age=None): #Here we are making Age optional

    """Return a dictionary of information about a person"""

    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('Dunsin', 'Oyekan', age=40)
print(musician)