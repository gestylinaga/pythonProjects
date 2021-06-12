#!/usr/bin/env python3

# a Simplified Tic-Tac-Toe Game Program
# no win-condition, program exits when board is full (9 turns)

# Board as a dictionary: (blank)
theBoard = {'topL': ' ', 'topM': ' ', 'topR': ' ',
        'midL': ' ', 'midM': ' ', 'midR': ' ',
        'botL': ' ', 'botM': ' ', 'botR': ' '}

# Prints a visual 'Game Board' on screen:
def printBoard(board):
    print(board['topL'] + '|' + board['topM'] + '|' + board['topR'])
    print('-+-+-')
    print(board['midL'] + '|' + board['midM'] + '|' + board['midR'])
    print('-+-+-')
    print(board['botL'] + '|' + board['botM'] + '|' + board['botR'])

# User input game:
turn = 'X'                                               # initial turn

for i in range(9):                                       # runs a set number of times (9)
    printBoard(theBoard)                                 # prints current board status
    print('Turn for ' + turn + '. Move on which space?') # User Prompt
    print('Options: top, mid, bot + L,M,R (example: topR, midM, botL)') # Show Options
    move = input()                                       # saves input as `move`
    theBoard[move] = turn                                # overwrites chosen move with 'X' or 'O'
    if turn == 'X':                                      # after 'X' goes,
        turn = 'O'                                       # turn changes to 'O'
    else:                                                # if 'X' did not go,
        turn = 'X'                                       # turn changes to 'X'

printBoard(theBoard)
