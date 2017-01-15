import unittest
from StickerCollectorOOP import *

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
		pass

if __name__ == '__main__':
    unittest.main()
