
#Start with some designs that need to be printed

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron'] #A list pf designs that need to be printed
# completed_models = [] #Thus is an empty list that tells us that no design has been printed yet\

#This first function is to handle the printing designs

def print_models(unprinted_designs, completed_models):

 """ Simulate printing each design, until none are left.
 Move each design to completed_models after printing."""

 while unprinted_designs:

    current_design = unprinted_designs.pop() #we are using pop to remove the unprinted designs and storing it in a variable called current design
    print(f"Printing model: {current_design}") #This shows the current model that is being printed
    completed_models.append(current_design) #We then append the current design to completed models

# This second function is to handle the prints that have been made
def show_completed_models(completed_models):
    """"Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model) 

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)