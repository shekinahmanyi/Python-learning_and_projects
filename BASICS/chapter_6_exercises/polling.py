#List of People who should take the poll
number_of_polls = {
    'John': 'Yes',
    'Sara': 'No',
    'Tim': 'Yes',
    'Sue': 'No',
    'Mike': 'Yes',
    }
people = ['John', 'Sara', 'Tim', 'Sue', 'Mike', 'Jen', 'Tom', 'Tina', 'Tod', 'Tara']
for person in people:
    if person in number_of_polls:
        print(f"Thank you for taking the poll, {person}!")
    else:
        print(f"Please take the poll, {person}!")
