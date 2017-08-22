

def getAverage(targetList):
    assert(len(targetList) != 0)
    return sum(targetList) / len(targetList)

def getMedium(targetList):
    assert(len(targetList) != 0)

    middleIndex = len(targetList) / 2
    
    sortedList = sorted(targetList)
    if len(targetList) % 2 == 1:
        return sortedList[middleIndex]
    return (sortedList[middleIndex - 1] + sortedList[middleIndex]) / 2

