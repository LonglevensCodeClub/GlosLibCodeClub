from MontyHallClasses import MontyHallGame
from random import randint

NUMBER_TESTS = 10000
winsByStrategy = dict()

# For each switching strategy (always True or always False)
for strategy in set([True, False]):
	
	# Run the game a number of times and count the wins
	winsByStrategy[strategy] = 0
	for x in range(NUMBER_TESTS):
		game = MontyHallGame.withRandomCorrectDoor()
		initialGuess = randint(0, 2)
		game.initialGuess(initialGuess)
		game.hostReveal()
		game.makeSwitch(strategy)
		if game.checkIfWon():
			winsByStrategy[strategy] += 1
			
print("Wins By Switching: {}".format(winsByStrategy))

for strategy, wins in winsByStrategy.items():
	winPercent = 100 * wins / NUMBER_TESTS;
	print("If we always play switch: {} then the chances of winning are {}%".format(strategy, winPercent))
