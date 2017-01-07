from PasswordGuesser import *

#
# This first example goes North then East 3 times, then South twice
#

myExample1 = MazeNavigator(expectedSteps=[	"north", \
											"east", \
											"north", \
											"east", \
											"north", \
											"east", \
											"south", \
											"south"])

#
# This code shows us using two loops to efficiently navigate the maze
#
for i in range(3):
	myExample1.north()
	myExample1.east()

for i in range(2):
	myExample1.south()

# Call this at the end to see if you were successful
myExample1.checkFinished()
