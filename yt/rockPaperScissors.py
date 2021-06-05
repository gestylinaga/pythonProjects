#!/usr/bin/python3
# the classic Rock, Paper, Scissors game as a program
# starts at: 21:16

import random

def play():
    user = input(" What's your choice? 'r' for rock, 'p' for paper, and 's' for scissors\n").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie!"

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'

    return 'You Lost!'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
