#!/usr/bin/python3
# a Random Numbers Guessing Game
# a Combination of computerGuess.py and guessTheNumber.py with a Menu System
# by Gesty Linaga

import random, time

def userGuess(x): # User guesses the computer's number
    randomNumber = random.randint(1, x)
    guess = 0
    try:
        while guess != randomNumber:
            guess = int(input(f'Guess a number between 1 and {x}: '))
            if guess > randomNumber:
                print("Nope, too high. Try again.")
            elif guess < randomNumber:
                print("That's too low, try again.")
        print(f"Nice! It was {randomNumber}, Good guess!")
    except ValueError:
        print("That's not a number, please enter a number.")

def compGuess(y): # Computer guesses the user's number
    low = 1
    high = y
    feedback = ''
    try:
        while feedback != 'c':
            if low != high:
                guess = random.randint(low, high)
            else:
                guess = low
            feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?").lower()    
            if feedback == 'h':
                high = guess - 1
            elif feedback == 'l':
                low = guess + 1
            else:
                print(f"You entered, {feedback}. Please enter a valid command.")
        print(f"EZPZ, the number was {guess}!")
    except ValueError:
        print("Something went wrong...did you make a mistake somewhere?")


print("Guess the Number Game! Make a choice: (1 or 2)") # Opening Prompt
try:
    choice = int(input(" 1. You Guess the Computer's Number \
        2. The Computer Guesses your Number\n"))        # "Menu System"
    while choice != 1 or 2:                             # loops while no choice is made
        if choice == 1:                                 # User Guess game
            ugLimit = int(input("Choose an upper limit to guess (I suggest 10):\n")) # Game prompt
            userGuess(ugLimit)                          # passes upper limit choice to function
            break                                       # ends the program when complete
        elif choice == 2:                               # Computer Guess game
            print("Think of a Number between 1-1000, and I will try to guess it...") # Game prompt
            time.sleep(2.0)                             # pauses time, lets user think of a number
            print("Ready? Starting in 5 seconds...")    # 5 second warning
            time.sleep(5.0)                             # more time to think
            compGuess(1000)                             # calls the Computer Guess game
            break                                       # ends the program when complete
        else:                                           # only executed if '1' or '2' not selected
            print(f"You entered: {choice}. Please enter a 1 or a 2") # User error feedback
except ValueError:                                      # catches any ValueErrors to avoid crashes
    print("Invalid input. Sorry, Goodbye!")             # exit error message
