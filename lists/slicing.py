#Slicing a List
players = ['charles', 'martina', 'micheal', 'florence','Eli','David'] #Created a List of Players
print("Here are the first players in my list :") #Writing a print statement for the first 3 players in the list
for player in players[:3]: #Created a for loop for the first three players in the List using a slice
    print(player.title())
