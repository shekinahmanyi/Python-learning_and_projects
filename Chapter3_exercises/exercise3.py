#Exercise 3.1

guests_lists = ['Rose','Linda','Micheal','John','Peter','Paul','David','Mary'] #Created a Guest List for Invitees
# printing a message to each person, inviting them to dinner
print(f'Hello {guests_lists[0].title()} I will like to invite you to Dinner at my place this weekend!')
print(f'Hello {guests_lists[1].title()} I will like to invite you for Dinner at my place this weekend!')
print(f'Hello {guests_lists[1].title()} I will like to invite you for Dinner at my place this weekend!')
print(f'Hello {guests_lists[2].title()} I will like to invite you for Dinner at my place this weekend!')
print(f'Hello {guests_lists[3].title()} I will like to invite you for Dinner at my place this weekend!')
print(f'Hello {guests_lists[4].title()} I will like to invite you for Dinner at my place this weekend!')
print(f'Hello {guests_lists[5].title()} I will like to invite you for Dinner at my place this weekend!')
print(f'Hello {guests_lists[6].title()} I will like to invite you for Dinner at my place this weekend!')
print(f'Hello {guests_lists[7].title()} I will like to invite you for Dinner at my place this weekend!')
guests_lists[-1] = 'Shirley' #Replaced Mary because she said she will not be able to make it for the dinner
print(f'Hello {guests_lists[-1].title()} I will like to invite you for Dinner at my place this weekend!')
#I just found out that a bigger dinner place is available so I will be inviting 3 extra people using the insert() method
guests_lists.insert(0, 'Abraham') #Inserted Abraham at the beginning of the list
guests_lists.insert(4, 'Sarah') #Inserted Sarah at the middle of the List
guests_lists.append('Isaac')#Inserted Isaac at the end of the List
#Printing a Message to the added Invitees for Dinner at my place
print(f'Hello {guests_lists[0].title()} I will like to invite you for Dinner at my place this weekend!')
print(f'Hello {guests_lists[4].title()} I will like to invite you for Dinner at my place this weekend!')
print(f'Hello {guests_lists[-1].title()} I will like to invite you for Dinner at my place this weekend!')
#I just found out that the dinner table will not be available so I will only be able to invite 2 people
#I will be using the pop() method to remove the extra people from the List
guests_lists.pop(0)#Removed Abraham from the List using the pop() method
print(f'Sorry {guests_lists[0].title()} I can only invite 2 people for Dinner at my place this weekend!')
guests_lists.pop(4)#Removed Sarah from the List using the pop() method
print(f'Sorry {guests_lists[4].title()} I can only invite 2 people for Dinner at my place this weekend!')
guests_lists.pop(-1)#Removed Isaac from the List using the pop() method
print(f'Sorry {guests_lists[-1].title()} I can only invite 2 people for Dinner at my place this weekend!')
guests_lists.pop(1)#Removed Linda from the List using the pop() method
print(f'Sorry {guests_lists[1].title()} I can only invite 2 people for Dinner at my place this weekend!')
guests_lists.pop(3)#Removed Peter from the List using the pop() method
print(f'Sorry {guests_lists[3].title()} I can only invite 2 people for Dinner at my place this weekend!')
guests_lists.pop(-2)#Removed Paul from the List using the pop() method
print(f'Sorry {guests_lists[-2].title()} I can only invite 2 people for Dinner at my place this weekend!')
guests_lists.pop(-1)#Removed Shirley from the List using the pop() method
print(f'Sorry {guests_lists[-1].title()} I can only invite 2 people for Dinner at my place this weekend!')
guests_lists.pop(-3)#Removed David from the List using the pop() method


print(guests_lists)#Printing the List of Invitees for Dinner at my place this weekend


