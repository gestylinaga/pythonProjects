#!/usr/bin/env python3
# Random Quiz Generator
# creates quizzes with questions and answers in random order, along with the answer key
# US States and their Capitals

import random # used to `.shuffle(states)`, `.shuffle(answerOptions)`, and `.sample(wrongAnswers, 3)`

# US State as keys; State Capital as the value:
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
   'New Mexico': 'Santa Fe','New York': 'Albany','North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files
for quizNum in range(35):
    # Create the quiz and answer key files
    quizFile = open(f'captialsquiz{quizNum + 1}.txt', 'w') # opened in write mode 'w'
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w') # opened in write mode 'w'

    # Write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form {quizNum + 1})')
    quizFile.write('\n\n')

    # Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all 50 states, making a question for each
    for questionNum in range(50):
        # Get right and wrong answers
        correctAnswer = capitals[states[questionNum]]       # Saves correct answer into a variable
        wrongAnswers = list(capitals.values())              # Creates a list of answers
        del wrongAnswers[wrongAnswers.index(correctAnswer)] # deletes the correct answer from the list of answers
        wrongAnswers = random.sample(wrongAnswers, 3)       # randomly chooses 3 wrong answers
        answerOptions = wrongAnswers + [correctAnswer]      # combines answer options to make up 4 total
        random.shuffle(answerOptions)                       # shuffles the answer options

        # Write the question and answer options to the quiz file
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            # f-string, string slice (for options A-D), list indexing (for answer options)
            quizFile.write(f"    {'ABCD'[i]}. {answerOptions[i]}\n") 
            quizFile.write('\n')

        # Write the answer key to a file: f-string, string slice (for correct answer)
        answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")

    # Close both created files
    quizFile.close()
    answerKeyFile.close()
