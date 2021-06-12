#!/usr/bin/env python3
# Using dicionaries to store birthday information

# The Dictionary -- `'Name': 'birthday'`
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# Main Program Loop
while True:
    print('Enter a name: (blank to quit)')                      # User Prompt
    name = input()                                              # saves user input as `name`

    if name == '':                                              # if input left blank
        break                                                   # breaks out of loop/program

    if name in birthdays:                                       # if input matches existing key
        print(birthdays[name] + ' is the birthday of ' + name)  # result

    else:                                                       # if not blank, or in database
        print('I do not have birthday information for ' + name) # feedback for user
        print('What is their birthday?')                        # new user prompt
        bday = input()                                          # saves new input as `bday`
        birthdays[name] = bday                                  # adds user input to dictionary
        print('Birthday database updated.')                     # feedback for user
