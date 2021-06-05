#!/usr/bin/python3
# catName
# builds a list of cat names, and displays them

catNames = []                    # empty list to hold cat names

while True:
    # User Prompt; converts the length of the list 'catNames' into a string; exit instructions
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()               # stores individual cat names as variable 'name'
    if name == '':               # breaks out of loop of input is left empty
        break
    catNames = catNames + [name] # list concatenation happens here

print('The cat names are:')
for name in catNames:            # for loop to run through each individual list item
    print(' ' + name)            # adds fake 'indent', and prints each item
