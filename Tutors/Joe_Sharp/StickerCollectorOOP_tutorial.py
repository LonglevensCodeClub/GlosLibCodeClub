from random import randint

class StickerBook():
	def __init__(self, name, collectionSize, packetSize):
		self.name = name
		self.collectionSize = collectionSize
		self.packetSize = packetSize
		
class StickerCollection():
	def __init__(self, book):
		self.book = book
		self.stickers = dict()
		self.packetsBought = 0
		
	def __str__(self):
		return "Packets Bought: {}, Stickers: {}".format(self.packetsBought, self.stickers)
		
	def buyPacket(self):
		self.packetsBought += 1
		for x in range(self.book.packetSize):
			s = randint(1, self.book.collectionSize)
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
			
	def swapWith(self, other):
		# Check that both people still need stickers, quit early
		if self.isComplete() or other.isComplete():
			return
		
		# Compose a set of stickers that can be swapped
		iHaveTheyNeed = set()
		theyHaveINeed = set()
		
		# For every sticker
		for x in range(1, self.book.collectionSize):
			# Do I have it, but they need it?
			if (x in self.stickers) and (x not in other.stickers):
				# Do I have a spare?
				if (self.stickers[x] > 0):
					iHaveTheyNeed.add(x)
			elif (x in self.stickers) and (x not in other.stickers):
				if (self.stickers[x] > 0):
					theyHaveINeed.add(x)
			
		# While there are stickers left in both piles
		while (len(iHaveTheyNeed) > 0) and (len(theyHaveINeed) > 0):
			# Pick one of mine and theirs to swap
			mine = iHaveTheyNeed.pop()
			theirs = theyHaveINeed.pop()
			
			# Receive sticker from other
			self.receiveSticker(mine)
			other.giveAwaySticker(mine)
			
			# Give sticker to other
			self.receiveSticker(theirs)
			other.giveAwaySticker(theirs)	
					
	def isComplete(self):
		return len(self.stickers) == self.book.collectionSize

def testSingleCollector():
	for x in range(5):

		# Create a book called 'Pokemon'
		pokemonBook = StickerBook(name="Pokemon", collectionSize=20, packetSize=3)	

		# Create a single collection of that book
		myPokemonCollection = StickerCollection(book=pokemonBook)

		while not myPokemonCollection.isComplete():
			myPokemonCollection.buyPacket()

		print("Collection Complete {} packets bought".format(myPokemonCollection.packetsBought))

## New code starting here
def testMultipleCollectors(numberCollectors):
	# Create a single book called 'World Cup 2014'
	worldCupBook = StickerBook(name="World Cup 2014", collectionSize=20, packetSize=3)	
		
	# Create an empty list of collections
	collections = []
	for x in range(numberCollectors):
		# Create a single collection and add it to the list
		coll = StickerCollection(book=worldCupBook)
		collections.append(coll)
		
	# Keep looping until all collections are complete
	incomplete = True
	while incomplete:
		# Each collector that has some remaining does a swap
		for c in collections:
			if not c.isComplete():
				c.buyPacket()
				
		for c in collections:
			for d in collections:
				c.swapWith(d)
		
		# Set incomplete to false and then try and prove otherwise
		incomplete = False
		for c in collections:
			if not c.isComplete():
				incomplete = True
	
	numberPacketsBought = 0
	for c in collections:
		numberPacketsBought += c.packetsBought
	return numberPacketsBought / len(collections)
	
for x in range(1, 30):
	howMany = 0
	for y in range(10):
		howMany += testMultipleCollectors(x)
	print("How many average with {} collectors {}".format(x, howMany / y))
