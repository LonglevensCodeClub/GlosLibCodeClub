from random import randint

def collectstickers(booksise):
    stickersbought = 0
    stickers = dict()
    
    
    while not (len(stickers) == booksise):
        stickersbought += 1
        s = randint(1, booksise)
        if s in stickers:
            stickers[s] += 1
        else:
            stickers[s] = 1
        
    return stickersbought

y = 100
x = collectstickers(y)

print("bought {} stickers for a collection".format(x))