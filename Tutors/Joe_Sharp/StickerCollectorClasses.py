from functools import reduce
from random import randint

class Packet():
	def __init__(self, stickers):
		self.stickers = stickers
			
	@classmethod
	def fromRandomSelection(cls, book):
		stickers = set()
		while len(stickers) < book.packetSize:
			s = randint(1, book.collectionSize)
			stickers.add(s)
		return cls(stickers)
		
	@classmethod
	def fromSpecifiedStickers(cls, book, stickers):
		return cls(stickers)
		

class StickerBook():
	def __init__(self, name, collectionSize, packetSize):
		self.name = name
		self.collectionSize = collectionSize
		self.packetSize = packetSize
		
	def __str__(self):
		return "Sticker Book {} with {} stickers in packets of {}".format(self.name, self.collectionSize, self.packetSize)
		
	def printPacket(self):
		return Packet.fromRandomSelection(self)
		
class StickerCollection():
	def __init__(self, book):
		self.book = book
		self.stickers = dict()
		self.packetsBought = 0
		
	def __str__(self):
		return "Packets Bought: {}, Stickers: {}".format(self.packetsBought, self.stickers)
		
	def receivePacket(self, packet):
		self.packetsBought += 1
		for s in packet.stickers:
			self.receiveSticker(s)
				
	def receiveSticker(self, whichSticker):
		if whichSticker in self.stickers:
			self.stickers[whichSticker] += 1
		else:
			self.stickers[whichSticker] = 1
			
	def giveAwaySticker(self, whichSticker, recipient):
		if (whichSticker in self.stickers):
			self.stickers[whichSticker] -= 1
			if (self.stickers[whichSticker] == 0):
				del(self.stickers[whichSticker])
			recipient.receiveSticker(whichSticker)
			return True
		return False
		
	def getSwaps(self):
		swaps = set(filter(lambda x: self.stickers[x] > 1, self.stickers.keys()))
		return swaps
				
	def isComplete(self):
		return len(self.stickers) == self.book.collectionSize

class GroupOfCollections():
	def __init__(self, book, collections, swapFunction):
		self.book = book
		self.collections = collections
		self.swapsMade = 0
		self.swapFunction = swapFunction
			
	@classmethod
	def withBookCountAndSwapFunction(cls, book, numberCollections, swapFunction):
		collections = []
		for x in range(numberCollections):
			c = StickerCollection(book=book)
			collections.append(c)
			
		return cls(book, collections, swapFunction)
		
	@classmethod
	def withBookCollectionsAndSwapFunction(cls, book, collections, swapFunction):
		return cls(book, collections, swapFunction)
			
	def buyPackets(self):
		for c in self.collections:
			if not c.isComplete():
				packet = self.book.printPacket()
				c.receivePacket(packet)		
							
	def runSwaps(self):
		for c in self.collections:
			for d in self.collections:
				if (c is not d):
					self.swapsMade += self.swapFunction(c, d)
		
	def getPacketsBought(self):
		packetsBought = map(lambda x: x.packetsBought, self.collections)
		total = reduce((lambda x, y: x + y), packetsBought)
		return total
			
	def isComplete(self):
		for c in self.collections:
			if not c.isComplete():
				return False
		return True

class SwapFunctions():
	# Returns all the swap functions in a dictionary, each function is given a name.
	@staticmethod
	def all():
		allFunctions = []
		allFunctions.append(SwapFunctions.noSwap)
		allFunctions.append(SwapFunctions.transactionalSwap)
		allFunctions.append(SwapFunctions.generousSwap)
		return allFunctions

	# Given two collectors, this function works out which ones each needs that the other has as a swap
	# It returns both sets, which can be unpacked by the caller
	@staticmethod
	def getRespectiveNeeds(first, second):
		# Get the list of swaps
		firstSwaps = first.getSwaps()
		secondSwaps = second.getSwaps()
				
		# Compose a set of stickers that can be swapped
		firstHasSecondNeeds = set(filter(lambda x: x not in second.stickers, firstSwaps))
		secondHasFirstNeeds = set(filter(lambda x: x not in first.stickers, secondSwaps))
		
		return firstHasSecondNeeds, secondHasFirstNeeds
	
	# A swap handler which simply doesn't do swapping, used as a 'control' in measurements
	@staticmethod
	def noSwap(first, second):
		return 0
		
	# This method works out what both collectors need, and what swaps are available.
	# It then swaps an equal number of stickers from first to second and vice versa
	# This is transactional because a collector only gives with the expectation of receiving
	@staticmethod
	def transactionalSwap(first, second):
		swapsMade = 0
		
		# Check that both people still need stickers, quit early
		if first.isComplete() or second.isComplete():
			return swapsMade
								
		# Work out what everyone needs
		firstHasSecondNeeds, secondHasFirstNeeds = SwapFunctions.getRespectiveNeeds(first, second)
			
		# While there are stickers left in both piles
		while (len(firstHasSecondNeeds) > 0) and (len(secondHasFirstNeeds) > 0):
			# Pick one of mine and theirs to swap
			fromFirst = firstHasSecondNeeds.pop()
			fromSecond = secondHasFirstNeeds.pop()
			swapsMade += 1
			
			first.giveAwaySticker(fromFirst, second)
			second.giveAwaySticker(fromSecond, first)
			swapsMade += 1
			
		return swapsMade
		
	# In this method, when two people are swapping, they pay no attention to how many they receive compared to how many they give.
	# This is 'generous' because each collector seeks to help the other with their swaps regardless of what they get back
	@staticmethod
	def generousSwap(first, second):
		swapsMade = 0
		
		# Check that at least one of the collectors needs more stickers
		if first.isComplete() and second.isComplete():
			return swapsMade
								
		# Work out what everyone needs
		firstHasSecondNeeds, secondHasFirstNeeds = SwapFunctions.getRespectiveNeeds(first, second)
			
		# First gives all required swaps to second
		for fromFirst in firstHasSecondNeeds:
			first.giveAwaySticker(fromFirst, second)
			swapsMade += 1
			
		# Second gives all required swaps to first
		for fromSecond in secondHasFirstNeeds:
			second.giveAwaySticker(fromSecond, first)
			swapsMade += 1
			
		return swapsMade
