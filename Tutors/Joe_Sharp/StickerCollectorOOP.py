from functools import reduce
from random import randint

class Packet():
	def __init__(self, book):
		self.stickers = set()
		while len(self.stickers) < book.packetSize:
			s = randint(1, book.collectionSize)
			self.stickers.add(s)

class StickerBook():
	def __init__(self, name, collectionSize, packetSize):
		self.name = name
		self.collectionSize = collectionSize
		self.packetSize = packetSize
		
	def __str__(self):
		return "Sticker Book {} with {} stickers in packets of {}".format(self.name, self.collectionSize, self.packetSize)
		
	def printPacket(self):
		return Packet(self)
		
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
			
	def giveAwaySticker(self, whichSticker):
		if (whichSticker in self.stickers):
			self.stickers[whichSticker] -= 1
			if (self.stickers[whichSticker] == 0):
				del(self.stickers[whichSticker])
				return True
		return False
		
	def getSwaps(self):
		swaps = set(filter(lambda x: self.stickers[x] > 1, self.stickers.keys()))
		return swaps
				
	def isComplete(self):
		return len(self.stickers) == self.book.collectionSize

class GroupOfCollections():
	def __init__(self, numberCollectors, book):
		self.book = book
		self.collections = []
		self.swapsMade = 0
		for x in range(numberCollectors):
			c = StickerCollection(book=book)
			self.collections.append(c)
			
	def buyPackets(self):
		for c in self.collections:
			if not c.isComplete():
				packet = self.book.printPacket()
				c.receivePacket(packet)		
							
		for c in self.collections:
			for d in self.collections:
				if (c is not d):
					self.swapsMade += self.handleSwap(c, d)
	
	def handleSwap(self, first, second):
		swapsMade = 0
		# Check that both people still need stickers, quit early
		if first.isComplete() or second.isComplete():
			return swapsMade
				
		# Get the list of swaps
		firstSwaps = first.getSwaps()
		secondSwaps = second.getSwaps()
				
		# Compose a set of stickers that can be swapped
		firstHasSecondNeeds = set(filter(lambda x: x not in second.stickers, firstSwaps))
		secondHasFirstNeeds = set(filter(lambda x: x not in first.stickers, secondSwaps))
			
		# While there are stickers left in both piles
		while (len(firstHasSecondNeeds) > 0) and (len(secondHasFirstNeeds) > 0):
			# Pick one of mine and theirs to swap
			fromFirst = firstHasSecondNeeds.pop()
			fromSecond = secondHasFirstNeeds.pop()
			
			# First gives sticker to second
			if first.giveAwaySticker(fromFirst):
				second.receiveSticker(fromFirst)
			
			# Second gives sticker to first
			if second.giveAwaySticker(fromSecond):
				first.receiveSticker(fromSecond)
				
			swapsMade += 1
			
		return swapsMade
	
	def getPacketsBought(self):
		packetsBought = map(lambda x: x.packetsBought, self.collections)
		total = reduce((lambda x, y: x + y), packetsBought)
		return total
			
	def isComplete(self):
		for c in self.collections:
			if not c.isComplete():
				return False
		return True

def testSingleCollector(numberTests, collectionSize, packetSize):
	for x in range(numberTests):
		# Create a book called 'Pokemon'
		pokemonBook = StickerBook(name="Pokemon", collectionSize=collectionSize, packetSize=packetSize)	

		# Create a single collection of that book
		myPokemonCollection = StickerCollection(book=pokemonBook)

		while not myPokemonCollection.isComplete():
			myPokemonCollection.buyPacket()

		print("Collection Complete {} packets bought".format(myPokemonCollection.packetsBought))

## New code starting here
def testMultipleCollectors(numberCollectors, collectionSize, packetSize):
	# Create a single book called 'World Cup 2014'
	worldCupBook = StickerBook(name="World Cup 2014", collectionSize=collectionSize, packetSize=packetSize)	
	collectors = GroupOfCollections(numberCollectors=numberCollectors, book=worldCupBook)
		
	x = 0
	while not collectors.isComplete() and x < 500:
		collectors.buyPackets()
		x += 1
	
	return collectors
	
for numberCollectors in range(1, 8):
	collectors = testMultipleCollectors(numberCollectors, 100, 6)
	av = collectors.getPacketsBought() / numberCollectors
	print("Average Packets Bought by {} collectors: {}, Swaps made: {}".format(numberCollectors, av, collectors.swapsMade))
