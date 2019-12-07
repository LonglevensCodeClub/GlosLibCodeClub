import random
import datetime

# Get hold of the day within the month
timeNow = datetime.datetime.now()
thisDay = timeNow.day

print("This day is " + str(thisDay))

#Define a seperate function for scrambling a word

def scrambleWord(word):
          
    # generate a list of indexes, they are generated in order
    letterIndexes = list(range(0, len(word)))

    # Shuffle the indexes so they can be used to generate the anagram
    random.shuffle(letterIndexes)

    # Start the scrambled value as empty string
    scrambled = ""

    # Work through the shuffled indexes, picking letters to append to our puzzle
    for x in letterIndexes:
      scrambled += word[x]

    return scrambled

print("Scrambled monkeys " + scrambleWord("monkeys"))
print("Scrambled turkey " + scrambleWord("turkey"))

def testUser(puzzle):
    answerGiven = input("Please type in the unscrambled " + scrambleWord(puzzle) + ": ")

    # Check the answer
    if puzzle == answerGiven:
        print("Correct, please award yourself one gift")
    else:
        print("Incorrect, sorry, please try again")
        return false

testUser("strawberries")

# Compose the list of puzzles
puzzles=[   'snowball',
            'santa',
            'holly',
            'reindeer',
            'presents',
            'turkey',
            'tinsel',
            'robin',
            'carols',
            'pudding',
            'wreath',
            'stocking',
            'star',
            'angel',
            'cracker',
            'nativity',
            'bauble',
            'sheperd',
            'stuffing',
            'tree',
            'sprouts',
            'sleigh']

testUser(puzzles[thisDay])
