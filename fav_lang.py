
# A dictionary of similar objects
fav_lang = {
    'jen': ['python', 'ruby'], # A list of languages as values
    'sarah': ['c'], 
    'edward': ['ruby', 'go'], 
    'phil': ['python', 'haskell'],
}

#An If statement to check if a person has more than one favorite language
if len(fav_lang) > 1:
    print("The following people have more than one favorite languages:")
    for name in fav_lang:
        if len(fav_lang[name]) > 1:
            print(f"\t{name.title()}")  
else:
    print("No one has more than one favorite language.")
# Looping through the dictionary
# for name in fav_lang:
#     print(f"\n{name.title()}'s favorite languages are:")
#     for lang in fav_lang[name]:
#         print(f"\t{lang.title()}")

# language = fav_lang['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# for name, lang in fav_lang.items():
#     print(f"{name.title()}'s favorite language is {lang.title()}.")

# for name in fav_lang.keys():
#     print(name.title())

# friends = ['phil', 'sarah', 'jen']
# for name in fav_lang.keys():
#     print(f"Hi {name.title()}.")

#     if name in friends:
#         lang = fav_lang[name].title()
#         print(f"\t{name.title()}, I see you love {lang}!")
    
#     elif 'erin' not in fav_lang.keys(): #check if a particular person was polled and if not, print a message
#         print("Erin, please take our poll!")

#you might want to sort the output of a dictionary
# for name in sorted(fav_lang.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

#we can also use the values() method to return a list of values without any keys
# print("The following languages have been mentioned:")
# for lang in fav_lang.values():
#     print(lang.title())
#The method above is good but can lead to a repetition of values. To avoid this, we use the set() method
# print("The following languages have been mentioned:")   
# for lang in set(fav_lang.values()):
#     print(lang.title())