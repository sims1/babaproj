import datetime
import os

def printStartTimeStamp():
    print('start time: {}'.format(datetime.datetime.now()))

def printEndTimeStamp():
    print('finish time: {}'.format(datetime.datetime.now()))

def getTitle(path):
    stockNumber = os.path.basename(os.path.normpath(path))
    numOfDays = len(os.listdir(path))
    return '{} ({} days)'.format(stockNumber, numOfDays)

def floatToString(flt, num):
    if num == 2:
        return "{0:.2f}".format(flt)
    if num == 3:
        return "{0:.3f}".format(flt)
    if num == 4:
        return "{0:.4f}".format(flt)

    print("ERROR: illegal num for floatToString()")
    assert(0)

def getPriceListFromFile(filename):
    result = []
    with open(filename, 'r') as fh:
        lines = fh.readlines()
        for line in lines:
            splitted = line.split(',')
            if len(splitted) != 4:
                continue
            result.append(float(splitted[1]))
        return result

def getPriceListFromFolder(path):
    result = []
    filesInCurrentDir = os.listdir(path)
    for fileName in filesInCurrentDir:
        if not fileName.endswith('.csv'):
            continue

        fullPath = os.path.join(path, fileName)
        result += getPriceListFromFile(fullPath)
    return result

