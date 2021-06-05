#!/usr/bin/python3
# a Simple ZigZaging Visual Toy Program

import time, sys
# 'time' allows for .sleep to pause the program
# 'sys' allows for .exit() to safely quit

indent = 0                                      # number of spaces to 'indent'
indentIncreasing = True                         # sets status to increasing

try:
    while True:                                 # main program loop
        print(' ' * indent, end='')             # handles the increasing 'indents'
        print('***************')                # makes up the 'zigzag' visual
        time.sleep(0.1)                         # pauses for 1/10th of a second

        if indentIncreasing:                    # this handles the indent's growth
            indent = indent + 1                 # 'grows' the amount in indentation
            if indent == 20:                    # upper limit of 'indents'
                indentIncreasing = False        # kills increase when upper limit is hit

        else:                                   # handles reverse growth
            indent = indent - 1                 # shrinks the amount of indentation
            if indent == 0:                     # lower limit of 'indents'
                indentIncreasing = True         # restarts growth when lower limit is hit

except KeyboardInterrupt:                       # <Ctrl> + <c> to exit program
    sys.exit()                                  # kills the program gracefully 
