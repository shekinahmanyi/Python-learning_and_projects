
#Using a Function with a while loop
def get_formatted_name(first_name, last_name, middle_name=''):

    """ Return a Full name, neatly formatted """
    
    if middle_name :
        full_name = f"{first_name} {last_name} {middle_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

#This is an Infinite Loop
while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' to quit at anytime)")

    f_name = input("First Name: ")
    if f_name == 'q': #Writing an If statement to stop the while loop
        break

    m_name = input("Middle_name: ")
    if m_name == 'q':
        break

    l_name = input("Last Name: ")
    if l_name == 'q': 
        break

    formatted_name = get_formatted_name(f_name, l_name,m_name)
    print(f"\nHello, {formatted_name}")