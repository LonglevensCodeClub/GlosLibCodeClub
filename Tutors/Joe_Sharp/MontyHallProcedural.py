from random import randint, choice

def playMontyHall(initialGuess=0, switch=False, interactive=False):
	# Randomly pick a correct door
	correctDoor = randint(0, 2)
	
	# Construct list of incorrect doors
	incorrectDoors = []
	for x in range(3):
		if not x == correctDoor:
			incorrectDoors.append(x)
			
	# Which doors have not been chosen and are not the correct door?
	incorrectDoorsNotChosen = []
	for x in incorrectDoors:
		if not x == initialGuess:
			incorrectDoorsNotChosen.append(x)
			
	# Host reveals a door (choose from incorrect doors that have not already been chosen)
	hostReveal = choice(incorrectDoorsNotChosen)
	
	# Interactive version
	if interactive:
		print("Host has revealed there is nothing behind door {}".format(hostReveal))
	
	# Find the available door to 'switch' to
	for x in range(3):
		if (not x == hostReveal) and (not x == initialGuess):
			availableSwitchDoor = x
			
	# Interactive version
	if interactive:
		switchStr = input("Do you want to switch doors to {} instead of {}? (y/n): ".format(availableSwitchDoor, initialGuess))
		switch = switchStr in set(["y", "Y", "Yes", "yes"])
			
	if switch:
		finalGuess = availableSwitchDoor
	else:
		finalGuess = initialGuess
		
	won = (finalGuess == correctDoor)
	
	# Interactive version
	if interactive:
		if won:
			print("Congratulations! You won with door {}".format(finalGuess))
		else:
			print("Sorry! You list with door {}, prize was behind {}".format(finalGuess, correctDoor))

	return won

initialGuess = int(input("Choose a door 0, 1 or 2: "));
playMontyHall(initialGuess=initialGuess, interactive=True)

def runStatisticalAnalysis():
	# Run statistical analysis
	NUMBER_TESTS = 10000
	winsByStrategy = dict()

	# For each switching strategy (always True or always False)
	for strategy in set([True, False]):
		
		# Run the game a number of times and count the wins
		winsByStrategy[strategy] = 0
		for x in range(NUMBER_TESTS):
			# Randomly pick a choice for the player
			initialGuess = randint(0, 2)
			if playMontyHall(initialGuess=initialGuess, switch=strategy):
				winsByStrategy[strategy] += 1
				
	print("Wins By Switching: {}".format(winsByStrategy))

	for strategy, wins in winsByStrategy.items():
		winPercent = 100 * wins / NUMBER_TESTS;
		print("If we always play switch: {} then the chances of winning are {}%".format(strategy, winPercent))
		
runStatisticalAnalysis()
