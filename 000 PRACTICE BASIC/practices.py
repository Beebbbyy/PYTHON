# s='word'
# print('The full string is: ',s)
# n=len(s)
# for i in range(n):
#     print()
#     print('i=',i)
#     print('The letter at index i:', s[i])
#     print('The part before index i (if any):', s[:1])
#     print('The part before before index i+2' , s[:i+2])


def getKeys(formatString):
    keyList=list()
    end = 0
    repetitions = formatString.count('{')
    for i in range (repetitions):
        start=formatString.find('{', end) +1
        end=formatString.find('}', start)
        key = formatString[start:end]
        keyList.append(key)
    return set(keyList)

def addPick(cue, dictionary):
    promptFormat ='Enter a specific example for {name}: '
    prompt=promptFormat.format(name=cue)
    response=input(prompt)
    dictionary[cue] =response

def getUserPicks(cues):
    userPicks=dict()
    for cue in cues:
        addPick(cue, userPicks)
    return userPicks

def tellStory(storyFormat):
    cues=getKeys(storyFormat)
    userPicks=getUserPicks(cues)
    story=storyFormat.format(**userPicks)
    print(story)

def main():
    originalStory="""
Once upon a time, deep in an ancient jungle, there lived a  {animal} . This
{animal} liked to eat {food}, but the jungle had very little {food} to offer.
One day, an explorer found the {animal} and discovered it liked {food}. The
explorer took the {animal} back to {city}, where it could eat as much {food}
as it wanted. However, the {animal} become homesick, so the explorer brought
it back to the jungle, leaving a large supply of {food}

THE END

"""
    tellStory(originalStory)
    input("Press Enter to end the program")

main()