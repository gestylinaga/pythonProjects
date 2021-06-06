#!/usr/bin/python3
# a Random Numbers Guessing Game

import random, time

def userGuess(x):
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

def compGuess(y):
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


print("Guess the Number Game! Make a choice: (1 or 2)")
try:
    choice = int(input(" 1. You Guess the Computer's Number \
        2. The Computer Guesses your Number\n"))
    while choice != 1 or 2:
        if choice == 1:
            ugLimit = int(input("Choose an upper limit to guess (I suggest 10):\n"))
            userGuess(ugLimit)
            break
        elif choice == 2:
            print("Think of a Number between 1-1000, and I will try to guess it...")
            time.sleep(2.0)
            print("Ready? Starting in 5 seconds...") 
            time.sleep(5.0)
            compGuess(1000)
            break
        else:
            print(f"You entered: {choice}. Please enter a 1 or a 2")
except ValueError:
    print("Invalid input, please enter a number.")
