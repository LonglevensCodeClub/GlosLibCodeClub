from random import randint

def collectstickers(booksize):
    stickersBought = 0
    stickers = dict()
    while not (len(stickers) == booksize-300):
        stickersBought += 1
        s = randint(1,booksize)
        if s in stickers:
            stickers[s]+=1
        else:
            stickers[s] =1

    return stickersBought


x = collectstickers(400)
print("Bought {} stickers for a collection of 400". format(x))
