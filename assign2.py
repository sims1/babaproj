#!/usr/bin/python

# for each day, calculate
#     - average
#     - medium
#     - mode (one mode)
#     - stdDeviation
#     - variance
#     - skewness
#     - kurtosis


import math
import os

import cvsio
import firstNMode
import simpleCalculate
import utility


def calculate(targetList):
    average = simpleCalculate.getAverage(targetList)
    medium = simpleCalculate.getMedium(targetList)

    modeList = map(lambda x: utility.floatToString(x, 2), firstNMode.getModes(targetList))
    modes = '/'.join(modeList)

    variance = simpleCalculate.getVariance(targetList)
    stdDeviation = math.sqrt(variance)


    # the first element in the list will be replaced by file name
    return [0,
            utility.floatToString(average, 2),
            utility.floatToString(medium, 2),
            modes,
            utility.floatToString(stdDeviation, 4),
            utility.floatToString(variance, 4)
            ]


title = ['date', 'average', 'medium', 'mode', 'stdDeviation', 'variance', 'kurtosis', 'skewness']
def run(stockFolder):
    ioObject = cvsio.IO(len(title))
    ioObject.write(title)
    
    files = os.listdir(stockFolder)
    for fileName in files:
        if not fileName.endswith('.csv'):
            continue

        path = os.path.join(stockFolder, fileName)
        targetList = utility.getPriceListFromFile(path)

        resultList = calculate(targetList)
        resultList[0] = fileName.replace('.csv', '')
        ioObject.write(resultList)

def main():
    utility.printStartTimeStamp()

    baseFolder = '/Users/ling/GitHub/babaProj/data'
    #stockList = ['000725', '000831', '600392']

    stock = '601699'
    path = os.path.join(baseFolder, stock)
    run(path)

    utility.printEndTimeStamp()

        

if __name__ == '__main__':
    main()

