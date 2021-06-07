#!/usr/bin/python3
# a Tutorial on fstrings
# by Gesty Linaga

import time                                         # allows for .sleep to pause time for reading

x = 420                                             # integer example
y = "texttexttext"                                  # string example
z = 6.9                                             # floating point number example

def fstrings():                                     # opening fstring example
    print(f"This is an integer: {x}")
    time.sleep(1)                                   # pauses time to allow for reading
    print(f"{y}, is a string")
    time.sleep(1)
    print(f"and {z} is a floating point number\n")  # '\n' adds a line break after the statement

def tutorial():                                     # tutorial section
    print("Python3 has 'fstring' magic, meaning theres no need for int(), str(), or float() anymore")
    time.sleep(2)
    print("All you need is an 'f' before the opening quotes, and '{variableName}' squirrely braces")
    print("Like so:\n")                             # another '\n' line break 
    time.sleep(5)                                   # 5 second pause for reading time
    print("someVariable = 666\n")                   # line breaks for readability
    time.sleep(2)
    print("print(")
    time.sleep(1)
    print("print(f <-- 'f' goes here")
    time.sleep(2)
    print("print(f\" <-- opening quote")            # '\' to escape the quote
    time.sleep(2)
    print("print(f\"someText <-- type your text")
    time.sleep(2)
    print("print(f\"someText {someVariable} <-- squirrely braces to hold the variable")
    time.sleep(2)
    print("print(f\"someText {someVariable}\") <-- close it up\n")
    time.sleep(2)
    print("That's it! That's all it takes! You're done!\n")
    print("The final output will read: 'someText 666'")

print("Fstring Tutorial:\n")                        # Title line
fstrings()                                          # calls fstring example
time.sleep(3)                                       # time to read
tutorial()                                          # calls the tutorial function
time.sleep(3)                                       # more time to read
print("Goodbye!")                                   # exit message
