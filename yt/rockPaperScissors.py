#!/usr/bin/python3
# the classic Rock, Paper, Scissors game as a program
# starts at: 21:16

import random                       # allows for .choice to randomely choose a rock/paper/scissors

def play():
    # \n adds a line break, .lower() converts the input to lowercase if need be
    user = input(" What's your choice? 'r' for rock, 'p' for paper, and 's' for scissors\n").lower()
    # r/s/p is chosen randomely, and saved as variable 'computer'
    computer = random.choice(['r', 'p', 's'])

    if user == computer:            # if the user and computer pick the same choice
        return "It's a tie!"        # tie game, no winner

    # r > s, s > p, p > r
    if is_win(user, computer):      # if the conditions for the function 'is_win' is met
        return 'You won!'           # user wins, computer loses

    return 'You Lost!'              # return this if no other condition is met

def is_win(player, opponent):       # return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True                 # r > s, s > p, p > r -- winning conditions

print(play())                       # calls the play() function and prints the results
