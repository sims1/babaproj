#!/usr/bin/python

from heapq import nlargest
import datetime
import itertools
from multiprocessing.dummy import Pool as ThreadPool
import os



def printStartTimeStamp():
    print('start time: {}'.format(datetime.datetime.now()))

def printEndTimeStamp():
    print('finish time: {}'.format(datetime.datetime.now()))

def getPriceList(lines):
    result = []
    for line in lines:
        splitted = line.split(',')
        if len(splitted) == 4:
            result.append(float(splitted[1]))
    return result

def getPriceToOccurences(targetList):
    result = {}
    for i in targetList:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result

def getOccurencesToPrices(priceToOccurences):
    result = {}
    for price, occurences in priceToOccurences.items():
        if occurences in result:
            result[occurences].append(price)
        else:
            result[occurences] = [price]
    return result

def getTopNOccurences(occurencesToPrice, n):
    occurences = []
    for key in occurencesToPrice:
        occurences.append(key)
    return nlargest(n, occurences)

def debug_isListSorted(lst):
    sortedLst = sorted(lst, reverse=True)
    i = 0
    while i < len(lst):
        assert(lst[i] == sortedLst[i])
        i += 1

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

def getMedium(targetList):
    assert(len(targetList) != 0)

    middleIndex = len(targetList) / 2
    
    sortedList = sorted(targetList)
    if len(targetList) % 2 == 1:
        return sortedList[middleIndex]
    return (sortedList[middleIndex - 1] + sortedList[middleIndex]) / 2

def getAverage(targetList):
    assert(len(targetList) != 0)
    
    return sum(targetList) / len(targetList)


def mapFunction_getPriceList(filename):
    with open(filename, 'r') as fh:
        lines = fh.readlines()
        return getPriceList(lines)

def getTargetList(path):
    filesInCurrentDir = os.listdir(path)

    csvFiles = filter(lambda x: x.endswith('.csv'), filesInCurrentDir)
    csvFilesWithPath = map(lambda x: os.path.join(path, x), csvFiles)

    dataInSubLists = map(mapFunction_getPriceList, csvFilesWithPath)
    return list(itertools.chain.from_iterable(dataInSubLists))

def getTitle(path):
    stockNumber = os.path.basename(os.path.normpath(path))
    numOfDays = len(os.listdir(path))
    return '{} ({} days)'.format(stockNumber, numOfDays)

def printFirstNModeToOccurences(modeToOccurences):
    print("\tmodes:\n\tPrice\t\tOccurences")

    for i in modeToOccurences:
        assert(len(i) == 2)
        print("\t{}\t\t{}".format(i[0], i[1]))

def run(path, firstNModes):
    printStartTimeStamp()
    
    targetList = getTargetList(path)
    assert(len(targetList) != 0)
    
    # Caution: there is no check for the consecutivity of the days
    print(getTitle(path))
    
    average = getAverage(targetList)
    print('\taverage: {}'.format(average))

    medium = getMedium(targetList)
    print('\tmedium: {}'.format(medium))

    firstNModeToOccurences = getFirstNModeToOccurences(targetList, firstNModes)
    printFirstNModeToOccurences(firstNModeToOccurences)

    printEndTimeStamp()


def main():
    firstNModes = 10;
    
    baseFolder = '/Users/ling/GitHub/babaProj'
    #stockList = ['000725', '000831', '600392']

    stockList = ['000725']

    for stock in stockList:
        path = os.path.join(baseFolder, stock)
        run(path, firstNModes)
        print('')

        

if __name__ == '__main__':
    main()

