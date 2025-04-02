cars = ['bmw', 'audi', 'toyota', 'subaru']
#cars.sort() # sort in alphabetical order
# cars.sort(reverse=True) # sort in reverse order
print('Here is the original list:')
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars)) # sorted() function sorts the list temporarily
print('\nHere is the original list again:')
print(cars)
cars.reverse() # reverse the order of the list
print('\nHere is the reversed list:')
print(cars)
print('\nHere is the length of the list:')
print(len(cars)) # length of the list