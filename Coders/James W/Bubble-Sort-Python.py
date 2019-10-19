import random

itemsToSort=random.sample(range(100), 10)
print ("Items (start)\t" + str (itemsToSort))

def swapItems(fromIndex, toIndex):
    swap = itemsToSort[fromIndex]
    itemsToSort[fromIndex] = itemsToSort[toIndex]
    itemsToSort[toIndex] = swap


def testSwapItems():
    item3before = itemsToSort[3]
    item4Before = itemsToSort[4]
    swapItems(3,4)
    assert itemsToSort[4] == item3before, "item 4 has not been swapped"
    assert itemsToSort[3] == item4before, "item 3 has not been swapped"
    print ("swapItems() Succesfully passed test")

    def compareItems(fromIndex, toIndex):
        if (itemsToSort[fromIndex] > itemsToSort[toIndex]):
            swapItems(fromIndex,toIndex)

def testCompareItems(fromIndex, toIndex, exceptSwap):
    itemFromBefore= itemsToSort[fromIndex]
    itemToBefore = itemsToSort[toIndex]
    compareItems(fromIndex, toIndex)
    if (expectSwap):
        assert itemsToSort[fromIndex] == itemToBefore, 'swap from is wrong'
        assert itemsToSort[toIndex] == itemFromBefore, 'swap to is wrong'
        print("compareItems() test - Items correctly left alone")
    else:
        assert itemsToSort[fromIndex] == itemFromBefore, 'noSwap from is wrong'
        assert itemsToSort[toIndex] == itemToBefore, 'noSwap to is wrong'
        print("compareItems() test - Items correctly left alone")

        itemsToSort[4] = 56
        itemsToSort[5] = 66
        testCompareItems(4, 5, False)

        itemsToSort[7] = 31
        itemsToSort[8] = 12
        testCompareItems(7, 8, True)

        def sortItems():
            for top in reversed(range(1, len(itemsToSort))):
                for current in range(0, top):
                    compareItems(current,current + 1)

                    sortItems();
                    print("Items (end)\t" + str(itemsToSort))

def testSortItems():
    random.shuffle(itemsToSort) -1)
    sortItems();
    for x in range(0, len(itemsToSort) - 1):
        assert itemsToSort[x + 1] >= itemsToSort[x], "Items in wrong order"
     print("sortITems() test - Items in correct order")

                    

