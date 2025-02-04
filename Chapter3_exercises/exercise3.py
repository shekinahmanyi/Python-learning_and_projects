#Exercise 3.1
guests_lists = ['Rose','Linda','Micheal','John','Peter','Paul','David','Mary']
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
print(guests_lists)