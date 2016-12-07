class SequenceChecker:
	def __init__(self, expectedSteps, allowedSteps):
		self.allowedSteps = allowedSteps
		self.expectedSteps = expectedSteps
		self.index = 0
		for e in expectedSteps:
			assert e in allowedSteps, "Step %s not found in allowed steps %s" % (e, allowedSteps)
		
	def takeStep(self, nextStep):
		assert self.index < len(self.expectedSteps), "You have run off the end of the expected path"
		expectedChar = self.expectedSteps[self.index]
		assert expectedChar == nextStep, "Wrong Direction %s, expected %s" % (nextStep, expectedChar)
		if (expectedChar == nextStep):
			self.index += 1
		else:
			raise Exception("Wrong Direction %s, expected %s" % nextStep, expectedChar) 
	
	def checkFinished(self):
		if (self.index == len(self.expectedSteps)):
			print("SUCCESS: You have retraced the steps %s!" % self.expectedSteps)
			return True
		else:
			print("NOT QUITE: You have not reached your destination")
	
class MazeNavigator(SequenceChecker):
	def __init__(self, expectedSteps):
		allowedSteps=["north", "south", "east", "west"]
		super(MazeNavigator, self).__init__(allowedSteps=allowedSteps, \
											expectedSteps=expectedSteps)
	
	def north(self):
		return self.takeStep("north")
	def south(self):
		return self.takeStep("south")
	def east(self):
		return self.takeStep("east")
	def west(self):
		return self.takeStep("west")


class RoadNavigator(SequenceChecker):
	def __init__(self, expectedSteps):
		allowedSteps=["straight", "left", "right"]
		super(RoadNavigator, self).__init__(allowedSteps=allowedSteps, \
											expectedSteps=expectedSteps)
	
	def straight(self):
		return self.takeStep("straight")
	def left(self):
		return self.takeStep("left")
	def right(self):
		return self.takeStep("right")
