
def greet_users(names):

    """Print a Simple greeting to each user in the List"""
    
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)