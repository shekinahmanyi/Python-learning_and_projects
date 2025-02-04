#This is a Practice Session of Learning Python by Creating a list and doing a lot with it.

friends_names = ['Shekinah', 'Manyi', 'Achidi', 'Salome', 'Gilda', 'Giren', 'Anje', 'Mc', 'Peter', 'Elijah', 'Hani'] #Created a List of Names
friends_names[-3] = 'Shirley' #Changed the third element to the end which is Peter to Shirley
friends_names.insert(0, 'Bernice') #Inserted Bernice at the beginning of the list
first_friend_name = friends_names.pop(0)#Removed Bernice from the List using the pop() method
last_friend_name = friends_names.pop()#Removed Hani from the List using the pop() method
print(f'Hello {last_friend_name.title()} I am so glad to see you again!')
print(f'Hello {first_friend_name.title()} I hope that I am able to see you again Very Soon!')
middle_friend_name = 'Giren'
friends_names.remove(middle_friend_name)#Removed Giren from the List using the remove() method
print(f'Hello {middle_friend_name.title()} Testing to see if you are still in the List!')

