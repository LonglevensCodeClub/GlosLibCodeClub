from random import randint

def collectStickers (bookSize):
    stickersBought = 0
    stickers = dict()


    while not (len(stickers) == bookSize):
        stickersBought+= 1
        s = randint(1, bookSize)
        if s in stickers:
         stickers [s] += 1
        else:
            stickers [s] = 1

        return stickersBought
    
myBookSize = 400
x = collectStickers(400)
print ("Bought {} stickers for a collection of 400" .format(x))

        

