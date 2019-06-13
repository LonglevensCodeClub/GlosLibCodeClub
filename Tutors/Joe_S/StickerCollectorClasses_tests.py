import unittest
from StickerCollectorClasses import *

class TestCollectionMethods(unittest.TestCase):
	
	def setUp(self):
		self.book = StickerBook(name="Pokemon", collectionSize=50, packetSize=4)	
	
	def testReceiveSticker(self):
		collection = StickerCollection(book=self.book)
		
		collection.receiveSticker(45)
		collection.receiveSticker(35)
		collection.receiveSticker(45)
		collection.receiveSticker(20)
		collection.receiveSticker(6)
		
		self.assertEqual(4, len(collection.stickers))
		self.assertTrue(45 in collection.stickers)
		self.assertTrue(35 in collection.stickers)
		self.assertTrue(20 in collection.stickers)
		self.assertTrue(6 in collection.stickers)
		self.assertEqual(2, collection.stickers[45])
	
	def testGiveSticker(self):
		collection1 = StickerCollection(book=self.book)
		collection2 = StickerCollection(book=self.book)

		collection1.receiveSticker(1)
		collection1.receiveSticker(5)
		collection1.receiveSticker(8)
		collection1.receiveSticker(8)
		
		collection1.giveAwaySticker(8, collection2)
		
		self.assertEqual(1, len(collection2.stickers))
		self.assertTrue(8 in collection1.stickers)
		self.assertEqual(1, collection1.stickers[8])
		self.assertTrue(8 in collection2.stickers)
		self.assertEqual(1, collection2.stickers[8])
		
	def testSwaps(self):
		collection1 = StickerCollection(book=self.book)
		collection2 = StickerCollection(book=self.book)
		
		# Give collection1 a swap of 8
		collection1.receiveSticker(1)
		collection1.receiveSticker(5)
		collection1.receiveSticker(8)
		collection1.receiveSticker(8)
		
		# Give collection2 a swap of 9
		collection2.receiveSticker(1)
		collection2.receiveSticker(6)
		collection2.receiveSticker(9)
		collection2.receiveSticker(9)
		collection2.receiveSticker(10)
		collection2.receiveSticker(10)
		
		group = GroupOfCollections.withBookCollectionsAndSwapFunction(book=self.book,
								collections=[collection1, collection2],
								swapFunction=SwapFunctions.transactionalSwap)
		group.runSwaps()
		
		expected1 = set([1, 5, 8])
		self.assertTrue(expected1 < collection1.stickers.keys())
		self.assertTrue(9 in collection1.stickers or 10 in collection1.stickers)
		
		expected2 = set([1, 6, 8, 9, 10])
		self.assertEqual(expected2, collection2.stickers.keys())

if __name__ == '__main__':
    unittest.main()
