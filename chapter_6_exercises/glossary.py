#Glossary
fav_programming_words = {'list': 'A collection of items in a particular order',
                          'tuples': 'A collection of items that cannot be changed',
                           'dictionary': 'A collection of key-value pairs', 
                            'string': 'A series of characters', 
                            'comments': 'A note in a program that the Python interpreter ignores',
                            'loop': 'Work through a collection of items, one at a time',
                            'conditional test': 'A comparison between two values',
                             'boolean expression': 'An expression that evaluates to True or False', 
                            'key-value pair': 'A set of values associated with each other',
                            'float': 'A numerical value with a decimal component'}

#using a loop to print out the key-value pairs
for word, definition in fav_programming_words.items():
    print(f"{word.title()}: {definition}")

