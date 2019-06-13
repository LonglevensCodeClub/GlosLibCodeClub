from MontyHallClasses import MontyHallGame

# Create the game
game = MontyHallGame.withRandomCorrectDoor()

# Get input from player
initialGuess = input("Please select a door to open 0, 1 or 2: ")

# Tell the game the initial guess
game.initialGuess(initialGuess)

# Call upon the host to reveal a door, and offer a switch
hostRevealed, availableSwitchDoor = game.hostReveal()

# Inform the player of the revealed door
print("The Host has revealed nothing behind door {}".format(hostRevealed))

# Capture the players choice regarding a door switch
switchDoors = input("Do you want to switch your choice from {} to {} y/n: ".format(game.initialGuess, game.availableSwitchDoor));

# Tell the game the users choice for their final guess
game.makeSwitch(switchDoors)

# Check if the player won, and print a message
won = game.checkIfWon()
if won:
	print("Congratulations! You won with door {}".format(game.finalGuess))
else:
	print("Sorry! You list with door {}, prize was behind".format(game.finalGuess, game.correctDoor))
