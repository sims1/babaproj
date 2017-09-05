#!/usr/bin/python

# for each day, calculate
#     - average
#     - medium
#     - mode (one mode)
#     - stdDeviation
#     - variance
#     - kurtosis
#     - skewness
#     - range
#     - min
#     - max


import argparse
import math
import os

import cvsio
import firstNMode
import simpleCalculate
import tickCountCalculate
import utility


def calculate(priceList, timeList, buySellList):
    calculator = simpleCalculate.Calculator(priceList)

    frequency = calculator.getN()
    tickCount = tickCountCalculate.calculate(timeList, buySellList)

    average = calculator.getAverage()
    medium = calculator.getMedium()

    modeList = map(lambda x: utility.floatToString(x, 2), firstNMode.getModes(priceList))
    modes = '/'.join(modeList)

    variance = calculator.getVariance()
    stdDeviation = calculator.getStdDeviation()

    kurtosis = calculator.getKurtosis()
    skewness = calculator.getSkewness()

    range = calculator.getRange()
    min = calculator.getMin()
    max = calculator.getMax()

    # the first element in the list will be replaced by file name
    return [0,
            str(frequency),
            str(tickCount),
            utility.floatToString(average, 2),
            utility.floatToString(medium, 2),
            modes,
            utility.floatToString(stdDeviation, 4),
            utility.floatToString(variance, 4),
            utility.floatToString(skewness, 4),
            utility.floatToString(kurtosis, 4),
            utility.floatToString(range, 2),
            utility.floatToString(min, 2),
            utility.floatToString(max, 2)
            ]


title = ['date', 'frequency', 'tickCount', 'mean', 'medium', 'mode', 'stdDeviation', 'variance', 'skewness', 'kurtosis', 'range', 'min', 'max']
def run(stockFolder):
    writeObject = cvsio.Writer(len(title))
    writeObject.write(title)
    
    files = os.listdir(stockFolder)
    for fileName in files:
        if not fileName.endswith('.csv'):
            continue
        
        path = os.path.join(stockFolder, fileName)
        readObject = cvsio.Reader(path)

        resultList = calculate(readObject.getPriceList(), readObject.getTimeList(), readObject.getBuySellList())
        resultList[0] = fileName.replace('.csv', '')
        writeObject.write(resultList)

def main():
    utility.printStartTimeStamp()

    #parser = argparse.ArgumentParser(description='.')
    #parser.add_argument('-f', 'baseFolder', help='.')
    #parser.add_argument('-s', 'stockSymbol', nargs=99999, action='append', help='stock symbols')
    #metavar=('url','name'),help='help:')
    #args = parser.parse_args()

    #baseFolder = args.baseFolder

    baseFolder = '/Users/ling/GitHub/babaProj/data'
    #stockList = ['000725', '000831', '600392']

    stock = '601699'

    path = os.path.join(baseFolder, stock)
    run(path)

    utility.printEndTimeStamp()

        

if __name__ == '__main__':
    main()

