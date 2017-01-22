from random import randint, choice

class MontyHallGame():
	# Creates a game with a fixed 'correct' door
	@staticmethod
	def withCorrectDoor(correctDoor):
		return MontyHallGame(correctDoor)
	
	# Creates a game with a random 'correct' door
	@staticmethod
	def withRandomCorrectDoor():
		correctDoor = randint(0, 2)
		return MontyHallGame.withCorrectDoor(correctDoor)
	
	# Constructor expects to be given the correct door, use one of the static methods
	def __init__(self, correctDoor):
		self.correctDoor = correctDoor
		self.incorrectDoors = [x for x in range(3) if not (x == self.correctDoor)]
		
	# Override string conversion so we can print something sensible
	def __str__(self):
		return "Correct Door: {}, Incorrect Doors: {}".format(self.correctDoor, self.incorrectDoors)
		
	# The player makes their initial guess, force to an integer so we can compare it with our 'doors'
	def initialGuess(self, guess):
		if type(guess) is int:
			self.initialGuess = guess
		elif type(guess) is str:
			self.initialGuess = int(guess)
		
	# Call upon the host to reveal one of the incorrect doors
	def hostReveal(self):
		incorrectDoorsNotChosen = [x for x in self.incorrectDoors if not x == self.initialGuess]
		self.hostReveal = choice(incorrectDoorsNotChosen)
		for x in range(3):
			if (not x == self.hostReveal) and (not x == self.initialGuess):
				self.availableSwitchDoor = x
			
		return self.hostReveal, self.availableSwitchDoor
		
	# Submit the players switching choice, this could be a Boolean (True/False) or a String (y/n)
	def makeSwitch(self, switch):
		# Convert the choice if necessary
		makeSwitch = switch
		if type(switch) is str:
			makeSwitch = switch in set(["y", "Y", "Yes", "yes"])
				
		# If the player switches, we switch to the other available door				
		if makeSwitch:
			self.finalGuess = self.availableSwitchDoor
		# Otherwise we kep with our initial guess
		else:
			self.finalGuess = self.initialGuess
	
	# We have won if the final guess matches the correct door
	def checkIfWon(self):
		return self.finalGuess == self.correctDoor
		

