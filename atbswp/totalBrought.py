#!/usr/bin/env python3
# a dictionary that stores picnic guests and items they brought
# displays total number of selected items

# Dictionary holding picnic guests and items they brought:
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
        'Bob': {'ham sandwhiches': 3, 'apples': 2},
        'Carol': {'cups': 3, 'apple pies': 1}}

# Calculates total number of items brought:
def totalBrought(guests, item):      # inputs name of guest, and name of item brought
    numBrought = 0                   # default number of item brought
    for k, v in guests.items():      # k = guest name; v = picnic item brought
        numBrought += v.get(item, 0) # if item exists (as a key), add to total; else `0`
    return numBrought                # returns final number of items brought

# Proof of Concept Printout:
print('Number of things being brought:')

# Syntax: functionName(dictName, 'stringToSearch')
print('Apples: ' + str(totalBrought(allGuests, 'apples')))
print('Cups: ' + str(totalBrought(allGuests, 'cups')))
print('Cakes: ' + str(totalBrought(allGuests, 'cakes')))
print('Ham Sandwhiches: ' + str(totalBrought(allGuests, 'ham sandwhiches')))
print('Apple Pies: ' + str(totalBrought(allGuests, 'apple pies')))
