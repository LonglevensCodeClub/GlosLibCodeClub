from StickerCollectorClasses import *

book = StickerBook(name="Pokemon", collectionSize=50, packetSize=4)	
numberCollections=4
testsPerFunction=1000

swapFunctions = SwapFunctions.all()

for swapFunction in swapFunctions:
	group = GroupOfCollections.withBookCountAndSwapFunction(book=book,
												numberCollections=numberCollections,
												swapFunction=swapFunction)

	totalPackets = 0
	for x in range(testsPerFunction):
		while not group.isComplete():
			group.buyPackets()
			group.runSwaps()

		totalPackets += group.getPacketsBought()

	average = totalPackets / (numberCollections * testsPerFunction)

	print("Algorithm {} group of {} bought {} packets each (on average)".format(swapFunction.__name__, numberCollections, average))
