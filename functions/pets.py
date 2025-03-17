
def describe_pets(animal_type, pet_name):

    """ Display Information about a pet """
    print(f"\nI have an {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

describe_pets(animal_type='hamster', pet_name='harry')
# describe_pets('dog', 'William') #here this can take as many parameters as needed