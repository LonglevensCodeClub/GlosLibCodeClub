from random import randint

# Defines the collection itself, is an abstract
class StickerBook():
	def __init__(self, name, collectionSize, packetSize):
		self.name = name
		self.collectionSize = collectionSize
		self.packetSize = packetSize
		
	def __str__(self):
		return "Name: {}, CollectionSize: {}, PacketSize: {}".format(
			self.name, 
			self.collectionSize, 
			self.packetSize)

class StickerCollection():
	def __init__(self, book):
		self.book = book
		self.stickers = dict()
		self.packetsBought = 0
	
	def __str__(self):
		return "Book: {}, Complete? {}, My Stickers: {}".format(
			self.book,
			self.isComplete(),
			self.stickers)
	
	def buyPacket(self):
		self.packetsBought += 1
		for x in range(self.book.packetSize):
			s = randint(1, self.book.collectionSize)
			if s in self.stickers:
				self.stickers[s] += 1
			else:
				self.stickers[s] = 1
		
	def isComplete(self):
		return len(self.stickers) == self.book.collectionSize
	
def buyPacketsUntilComplete(book):
	myCollection = StickerCollection(book=pokemonBook)

	while not myCollection.isComplete():
		myCollection.buyPacket()
	
	print("Collection Complete {} packets bought".format(myCollection.packetsBought))
	
	return myCollection.packetsBought
	
numberOfTests = 25
totalPackets = 0
pokemonBook = StickerBook(name = "Pokemon", collectionSize=20, packetSize=3)	
for x in range(numberOfTests):
	totalPackets += buyPacketsUntilComplete(pokemonBook)

print("We ran the entire collection {} times and averaged {} packets to complete it".format(
		numberOfTests,
		totalPackets / numberOfTests))
