#Dictionary of rivers and their countries
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
    } 
#Loop through the dictionary and print the river and the country
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
#Loop through the dictionary and print the rivers
for river in rivers.keys():
    print(river.title())
#Loop through the dictionary and print the countries
for country in rivers.values():
    print(country.title())