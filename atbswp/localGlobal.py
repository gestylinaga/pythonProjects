#!/usr/bin/python3
# a practice program to display the difference between local/global scopes

def spam():
    eggs = 'spam local'  # local only to the spam function
    print(eggs)          # prints 'spam local'


def bacon():
    eggs = 'bacon local' # local only to the bacon function
    print(eggs)          # prints 'bacon local'
    spam()               # calls entire spam function
    print(eggs)          # prints 'bacon local'


eggs = 'global'          # this is the global variable
bacon()                  # recall that the spam function is called in the middle of this
print(eggs)              # prints 'global'

"""the output of this program will read: (in this specific order)

bacon local
spam local
bacon local
global

This shows that variable names are isolated within functions, and don't interfere with
global variable names
"""
