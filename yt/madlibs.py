#!/usr/bin/python3
# a simple Madlibs program
# starts at: 1:19

# This section gives a User prompt and saves their input as a variable
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Another Verb: ")
famous_person = input("Famous Person: ")

# this is the 'madlib' the variables are plugged in to
madlib = f"Computer prgramming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
# Notice the 'f' and the '{}' braces, this allows easy string concatenation/conversion
# also notice the '\' and lack of indent to indicat a line break

print(madlib) # this prints the final 'madlib', complete with the User's variables
