import cvsio

def calculate(timeList, buySellList):
    assert(len(timeList) != 0 and len(timeList) == len(buySellList))

    buyDict = {}
    sellDict = {}

    i = 0
    while i < len(timeList):
        if buySellList[i] == cvsio.TickType.BUY:
            buyDict[timeList[i]] = 0
        elif buySellList[i] == cvsio.TickType.SELL:
            sellDict[timeList[i]] = 0
        i += 1

    return len(buyDict) + len(sellDict)

'''
    buyCount = 0
    sellCount = 0

    i = 0
    currentTime = timeList[i]
    isBuy = False
    isSell = False
    while i < len(timeList):
        if timeList[i] != currentTime:
            if isBuy:
                buyCount += 1
            if isSell:
                sellCount += 1

            # update
            isBuy = False
            isSell = False
            currentTime = timeList[i]
        else:
            if buySellList[i] == cvsio.TickType.BUY:
                isBuy = True
            elif buySellList[i] == cvsio.TickType.SELL:
                isSell = True

        i += 1

    if isBuy:
        buyCount += 1
    if isSell:
        sellCount += 1

    return buyCount + sellCount
'''
