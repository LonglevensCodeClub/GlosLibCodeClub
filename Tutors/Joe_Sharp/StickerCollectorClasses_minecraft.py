from mcpi.minecraft import Minecraft
from mcpi import block
from StickerCollectorClasses import *
import time
import math

collectionId=1
collectionSize = 50
packetSize=2
book = StickerBook(	name="Pokemon", 
					collectionSize=collectionSize, 
					packetSize=packetSize)	

## Build a wall
mc = Minecraft.create()
x, y, z = mc.player.getTilePos()

wallDim = math.floor(math.sqrt(collectionSize) + 1)
expectedMaxSwaps=collectionSize
distanceAwayFromPlayer=10

mc.setBlocks(	x, y, z, 
				x+wallDim, y+wallDim, z+expectedMaxSwaps, 
				block.AIR)

def observer(colId, whichSticker, count):
	print("ColId: {}, Sti: {}, Count: {}".format(colId, whichSticker, count))
	tX = math.floor((whichSticker-1) % wallDim)
	tY = math.floor((whichSticker-1) / wallDim)
	blockType = block.WOOD if (count > 0) else block.COBBLESTONE
	mc.setBlocks(	x+tX, y+tY, z+distanceAwayFromPlayer-count, 
					x+tX, y+tY, z+distanceAwayFromPlayer, 
					blockType)
					
for i in range(1, collectionSize+1):
	observer(collectionId, i, 0)
	
collection = StickerCollection(book=book, collectionId=collectionId, observer=observer)

while not collection.isComplete():
	time.sleep(0.1)
	packet = book.printPacket()
	collection.receivePacket(packet)	
	
print("Done {}".format(collection))



