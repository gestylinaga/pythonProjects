#!/usr/bin/python3
# Magic 8 Ball
# a remake of fortune.py with the use of "lists"

import random
# allows for .randint() to select random index

messages = [ 'Yep!',             # yes
        'Very Positive',         # yes
        'Sure',                  # yes
        'Yes, of course',        # yes
        'Not a chance',          # no
        'No way!',               # no
        'Doesn\'t look good...', # no
        'Nope.',                 # no
        'hmm...']                # neutral

print(messages[random.randint(0, len(messages) - 1)])
# 'messages[]' to pull an index item
# 'random.randint()' to generate random number
#   '0' to set lower limit
#   'len()' to get length of list 'messages'
#       '- 1' to subtract 1 from list, gives valid upper limit
