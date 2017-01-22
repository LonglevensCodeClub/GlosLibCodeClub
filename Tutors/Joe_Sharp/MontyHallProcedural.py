from random import randint, choice

def playMontyHall(switch=False):
	# Randomly pick a correct door
	correctDoor = randint(0, 2)
	
	# Construct list of incorrect doors
	incorrectDoors = []
	for x in range(3):
		if not x == correctDoor:
			incorrectDoors.append(x)
			
	# Randomly pick a choice for the player
	initialGuess = randint(0, 2)
	
	# Which doors have not been chosen and are not the correct door?
	incorrectDoorsNotChosen = []
	for x in incorrectDoors:
		if not x == initialGuess:
			incorrectDoorsNotChosen.append(x)
			
	# Host reveals a door (choose from incorrect doors that have not already been chosen)
	hostReveal = choice(incorrectDoorsNotChosen)
	
	# Find the available door to 'switch' to
	for x in range(3):
		if (not x == hostReveal) and (not x == initialGuess):
			availableSwitchDoor = x
			
	if switch:
		finalGuess = availableSwitchDoor
	else:
		finalGuess = initialGuess
		
	return finalGuess == correctDoor

# Run statistical analysis
NUMBER_TESTS = 10000
winsByStrategy = dict()

# For each switching strategy (always True or always False)
for strategy in set([True, False]):
	
	# Run the game a number of times and count the wins
	winsByStrategy[strategy] = 0
	for x in range(NUMBER_TESTS):
		if playMontyHall(strategy):
			winsByStrategy[strategy] += 1
			
print("Wins By Switching: {}".format(winsByStrategy))

for strategy, wins in winsByStrategy.items():
	winPercent = 100 * wins / NUMBER_TESTS;
	print("If we always play switch: {} then the chances of winning are {}%".format(strategy, winPercent))
