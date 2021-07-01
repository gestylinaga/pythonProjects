#!/usr/bin/env python3
# The Collatz Sequence: the simplest impossible math problem
# atbswp chapter 3 practice project
# By: Gesty Linaga

# Title and Explanation
print('\nThe Collatz Sequence: The simplest impossible math problem')
print('''
    Even numbers are divided by 2,
    Odd numbers are multiplied by 3, then added to 1.

    The Collatz Sequence, when run repeatedly on a number, will always
    end up at 1.\n''')

def collatz(number):

    # Fun Number Messages
    if number == 69:
        print('Nice')
    elif number == 420:
        print('Blaze it')
    elif number == 666:
        print('Hail Satan!')
    elif number == 1:
        print(f'Well thats easy...{number}')

    # Main Program Loop
    while number != 1:              # Runs repeatedly until the number is 1
        if number % 2 == 0:         # On even numbers:
            number = number // 2    # (floor) divide by 2
            print(number)           # Shows new current number

        else:                       # On odd numbers:
            number = 3 * number + 1 # times 3, added to 1
            print(number)           # Shows new current number

    print('...see, told you')       # Smug

# User prompt, and Function Call, with Input Validation
try:
    number = int(input('Give me a starting point number: \n'))
    collatz(number)
except ValueError:
    print("That's NOT a number! Goodbye.")
