import random
import datetime

# Get hold of the day within the month
timeNow = datetime.datetime.now()
thisDay = timeNow.day

print("This day is " + str(thisDay))

# Define a seperate function for scrambling a way
def scrambleWord(word):
  # Generate a list of indexes, they are generated in order
  letterIndexes = list(range(0, len(word)))
  
  # Shuffle the indexes so they can be used to generate anagram
  random.shuffle(letterIndexes)
  
  # Start the scrambled value as an empty string
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
       print("Correct, please award youself one gift")

       return True
    else:
        print ("Incorrect, sorry, please try again")
        return False



testUser("strawberries")

# Compose the list of puzzles
puzzles = [   'snowball',
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
              'angle',
              'cracker',
              'nativity',
              'bauble',
              'sheperd',
              'stuffing',
              'tree',
              'sprouts',
              'sleigh']


testUser(puzzles[thisDay])

# Seed the solved indicators with False for all puzzles
solved = []
for puzzle in puzzles:
    solved.append(False)

def printPuzzles():
    for x in range(0, len(puzzles)):
        toPrint = "##########"
        if solved[x]:
            toPrint = puzzles[x]
        print("Puzzle for " +str(x + 1) + ":/t" + toPrint)

solved[21] = True
printPuzzles()

whichDay = 1
while True:
    whichDay = int(input("Please type in which day to solve (type 0 to quit): "))
    if (whichDay ==0):
        break
    if(whichDay <= thisDay):
        if testUser(puzzles[whichDay]):
            solved[whichDay] = True
        printPuzzles()
    else:
        print("You aren't allowed to solve this one yet")
