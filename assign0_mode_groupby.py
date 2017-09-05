#!/usr/bin/python

from collections import Counter
import datetime
from itertools import groupby
import os

def printStartTimeStamp():
    print('start time: {}'.format(datetime.datetime.now()))

def printEndTimeStamp():
    print('finish time: {}'.format(datetime.datetime.now()))

def calculateMode(targetList):
    #targetList = [5, 7, 3, 2, 5, 6, 5, 9, 0, 3, 9, 9]

    if len(targetList) == 0:
        return []

    grouped = groupby(Counter(targetList).most_common(), lambda x:x[1])
    result = next(grouped)[1]
    return [val for val,count in result]

def getPriceList(lines):
    result = []
    for line in lines:
        splitted = line.split(',')
        if len(splitted) != 4:
            continue

        result.append(float(splitted[1]))
    return result

def getFirstNMode(targetList, n):
    result = []
    while len(result) < n:
        mode = calculateMode(targetList)
        if len(mode) == 0:
            return result

        result += mode
        targetList = filter(lambda x: x not in mode, targetList)
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

def getTargetList(path):
    result = []
    for filename in os.listdir(path):
        with open(os.path.join(path, filename), 'r') as fh:
            if not filename.endswith('.csv'):
                print('WARNING: {} file name suffix is not csv'.format(filename))
                continue
            
            lines = fh.readlines()
            result += getPriceList(lines)
    return result

def getTitle(path):
    stockNumber = os.path.basename(os.path.normpath(path))
    numOfDays = len(os.listdir(path))
    return '{} ({} days)'.format(stockNumber, numOfDays)


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

    firstNMode = getFirstNMode(targetList, firstNModes)
    print('\tmode: {}'.format(firstNMode))

    printEndTimeStamp()


def main():
    firstNModes = 10;
    
    baseFolder = '/Users/ling/GitHub/babaProj'
    stockList = ['000725', '000831', '600392']

    for stock in stockList:
        path = os.path.join(baseFolder, stock)
        run(path, firstNModes)
        print('')

        

if __name__ == '__main__':
    main()

