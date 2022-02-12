#! /usr/bin/env python
#tell the operating system what version of Python to choose.
'''This is the first program from Hands-onPython Tutorial'''
#Quoted text is called a string

import sys

storyFormat='''
Once upon a time, deep in an ancient jungle, there lived a {animal}.This
{animal} liked to eat {food}, but the jungle had very little {food} to offer.
One day, an explorer found {animal} and discovered it liked {food}. The
explorer took the {animal} became homesick, so the explorer brought it back 
to the jungle, leaving a large suppy of {food}

The END
'''
#The equal sign tells the computer that this is an assignment statement.
#The computer will now associate the value of the expression between
#the triple quotes, a multi-line string with the name on the left, storyFormat

def tellStory():
    userPicks= dict()
    addPick('animal', userPicks)
    addPick('food',userPicks)
    addPick('city',userPicks)
    story = storyFormat.format(**userPicks)
    print(story)

def addPick(cue, dictionary):
    ''' Promt for a user response using the cue string, and place the 
    cue-response pair in the dictionary.'''
    promt='Enter an example for ' + cue + ': '
    response=input(promt)
    dictionary[cue] = response

tellStory()
input('Press Enter to end the program.')

# with open("test.txt", 'w') as sys.stdout:
#     print(tellStory())
