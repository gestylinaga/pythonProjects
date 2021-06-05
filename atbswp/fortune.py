#!/usr/bin/python3
# a 'Fortune-Teller' Program

import random
# allows use of .randint to generate random numbers

def getAnswer(answerNumber):
    # defines message to return for each number
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'Yes'
    elif answerNumber == 3:
        return 'Ask again later'
    elif answerNumber == 4:
        return 'My reply is no'
    elif answerNumber == 5:
        return 'Outlook is not good'
    elif answerNumber == 6:
        return 'For sure!'
    elif answerNumber == 7:
        return 'Definitely not'
    elif answerNumber == 8:
        return 'Nope'
    elif answerNumber == 9:
        return 'Yep'

# generates a random number 1-9 &
# passes it to, and calls the 'getAnswer' function &
# and prints the result
print(getAnswer(random.randint(1, 9)))
