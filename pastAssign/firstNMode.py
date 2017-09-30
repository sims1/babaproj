from heapq import nlargest

#from multiprocessing.dummy import Pool as ThreadPool

# private
def getPriceToOccurences(targetList):
    result = {}
    for i in targetList:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result

# private
def getOccurencesToPrices(priceToOccurences):
    result = {}
    for price, occurences in priceToOccurences.items():
        if occurences in result:
            result[occurences].append(price)
        else:
            result[occurences] = [price]
    return result

# private
def getTopNOccurences(occurencesToPrice, n):
    occurences = []
    for key in occurencesToPrice:
        occurences.append(key)
    return nlargest(n, occurences)

# private
def debug_isListSorted(lst):
    sortedLst = sorted(lst, reverse=True)
    i = 0
    while i < len(lst):
        assert(lst[i] == sortedLst[i])
        i += 1

def getModes(targetList):
    priceToOccurences = getPriceToOccurences(targetList)
    occurencesToPrice = getOccurencesToPrices(priceToOccurences)

    maxOccurence = -1
    modes = []
    for occurences, price in occurencesToPrice.items():
        if occurences > maxOccurence:
            maxOccurence = occurences
            modes = price
        elif occurences == maxOccurence:
            modes += price

    return modes


def getFirstNModeToOccurences(targetList, n):
    priceToOccurences = getPriceToOccurences(targetList)
    occurencesToPrice = getOccurencesToPrices(priceToOccurences)

    topNOccurences = getTopNOccurences(occurencesToPrice, n)
    #debug_isListSorted(topNOccurences)

    result = []
    for occurences in topNOccurences:
        priceLst = occurencesToPrice[occurences]
        for price in priceLst:
            result.append([price, occurences])
            if len(result) >= n:
                break
        if len(result) >= n:
                break

    return result

def printFirstNModeToOccurences(modeToOccurences):
    print("\tmodes:\n\tPrice\t\tOccurences")

    for i in modeToOccurences:
        assert(len(i) == 2)
        print("\t{}\t\t{}".format(i[0], i[1]))