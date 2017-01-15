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
			
			first.giveAwaySticker(fromFirst, second)
			second.giveAwaySticker(fromSecond, first)
				
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


