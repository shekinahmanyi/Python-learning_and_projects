
# A dictionary of similar objects
fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# language = fav_lang['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

for name, lang in fav_lang.items():
    print(f"{name.title()}'s favorite language is {lang.title()}.")