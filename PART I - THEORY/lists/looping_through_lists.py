#Chapter 4: Looping through lists
magicians_names = ['alice', 'david', 'carolina','Harry', 'Houdini']
for magician_name in magicians_names: #Created a temporary variable magician_name to hold the value of the list
    print(f'{magician_name.title()}, that was a great trick!') #Printed the value of the temporary variable
    print(f'I cannot wait to see your next trick, {magician_name.title()}.\n')
print('Thank you everyone, that was a great magic show!') #Printed a message after the loop ends
   