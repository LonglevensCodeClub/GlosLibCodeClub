
from random import randint

def collectStickers(bookSize, observer=None):
    stickersBought = 0
    stickers = dict() 
    packsbought = 0


    #tell the observer about the existence of all stickers
    if observer:
        for x in range(1, bookSize):
            observer(x, 0)


    while not (len(stickers) >= bookSize - 0):
    
        packSize = 5

        packsbought = packsbought + 1
        for a in range(packSize):
            stickersBought = stickersBought + 1
            s = randint(1, bookSize)
            if s in stickers:
                stickers[s] += 1
            else:
                stickers[s] = 1

            #update the obsever
            if observer:
                observer(s, stickers[s])
    

    mostSwaps = 0
    stickerSwap = 0
    for s in stickers.keys():
        if (stickers[s] > mostSwaps):
            mostSwaps = stickers[s]
            stickerSwap = s
    #print("Most swaps are {} for sticker {}.".format(mostSwaps, stickerSwap))
		
    return stickersBought

