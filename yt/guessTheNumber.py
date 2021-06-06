#!/usr/bin/python3
# Guess the computer's number, a game program
# starts at: 6:55

import random                            # allows for .randint to generate a random number 

def guess(x): # parameter of 'x' so that the number can be easily changed later
    random_number = random.randint(1, x) # computer's number is randomly generated here
    guess = 0                            # sets initial guess, starts while loop (!=)
    while guess != random_number:        # continues loop if User hasn't guessed correctly yet
        # User prompt, with an fstring, converted to an integer, and saved as 'guess'
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:        # gives hint if guess is too low
            print('Nope, too low. ')
        elif guess > random_number:      # gives hint if guess is too high
            print('Uh uh, too high. ')

    # this line is only printed when the 'guess != random_number' loop returns 'False'
    print(f'Niiice! You Got it Dude! It was {random_number}! Sick guess!')
        
guess(10) # calls the function, passing it a number for the upper-limit of .randint
# changing the default '10' will change the computer's range of numbers to choose from
