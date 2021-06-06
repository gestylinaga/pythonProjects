#!/usr/bin/python
# Computer Guesses Your Number game
# starts at: 13:15

import random
# allows for .randint to generate an upper/lower limit to guesses

def computer_guess(x):
    low = 1                   # initial lower limit for guesses
    high = x                  # initial upper limit for guessess (max number)
    feedback = ''             # initial user feedback set as empty
    while feedback != 'c':    # continues loop while guess != correct
        if low != high:       # when low == high, the computer has the correct answer
            guess = random.randint(low, high) # will continue guessing
        else:                 # sets new lower limit as previous guess
            guess = low       # could also be high b/c low = high
        # User prompt, with an fstring, converted to lowercase, and saved as feedback:
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (c)? ').lower()
        if feedback == 'h':   # adjusts upper limit based on user feedback
            high = guess - 1  # number to adjust by
        elif feedback == 'l': # adjusts lower limit based on user feedback
            low = guess + 1   # number to adjust by
    # this line is only printed when the 'feedback != c' loop returns 'False'
    print(f'Thats right...take that filthy human! Of course it was {guess}! EZ PZ! ')

computer_guess(1000) # calls the function, passing it a number for the upper limit guess
# changing the default '1000' will change the range of numbers you can choose from
