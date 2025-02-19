
# A dictionary of similar objects
fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# language = fav_lang['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# for name, lang in fav_lang.items():
#     print(f"{name.title()}'s favorite language is {lang.title()}.")

# for name in fav_lang.keys():
#     print(name.title())

friends = ['phil', 'sarah', 'jen']
for name in fav_lang.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        lang = fav_lang[name].title()
        print(f"\t{name.title()}, I see you love {lang}!")
    
    elif 'erin' not in fav_lang.keys(): #check if a particular person was polled and if not, print a message
        print("Erin, please take our poll!")

#you might want to sort the output of a dictionary
# for name in sorted(fav_lang.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")