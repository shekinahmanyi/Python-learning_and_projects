
#Start with some designs that need to be printed

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron'] #A list pf designs that need to be printed

completed_models = [] #Thus is an empty list that tells us that no design has been printed yet
 # Simulate printing each design, until none are left.
 #  Move each design to completed_models after printing.

while unprinted_designs:

    current_design = unprinted_designs.pop() #we are using pop to remove the unprinted designs and storing it in a variable called current design
    print(f"Printing model: {current_design}") #This shows the current model that is being printed
    completed_models.append(current_design) #We then append the current design to completed models


# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model) #We use a for loop to show us the designs that we just appended that have been printed

    # print(completed_models)