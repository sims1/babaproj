#!/usr/local/bin/python3

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


import math
import optparse
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
def runOnStock(stockFolder):
    outputFileName = os.path.basename(os.path.normpath(stockFolder))

    writeObject = cvsio.Writer(outputFileName, len(title))
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



def run():
    parser = optparse.OptionParser()
    parser.add_option('-f', '--base-folder', action='store', dest='baseFolder',
        help="Expecting folders with stock name under this folder", default=None)
    parser.add_option('-s', '--stock-folder', action='store', dest='stockFolder',
        help="Expecting folders with stock name under this folder", default=None)

    options, args = parser.parse_args()

    baseFolder = options.baseFolder
    stockFolder = options.stockFolder

    if baseFolder == None and stockFolder == None:
        print('Error: no stock path specified, please run --help for more information')
        exit(-1)
    if baseFolder != None and stockFolder != None:
        print('Error: base folder and stock folder cannot be both specified, please run --help for more information')
        exit(-1)

    if stockFolder != None:
        if not os.path.isdir(stockFolder):
            print('ERROR: Path "{}" does not exist'.format(stockFolder))
            exit(-1)

        runOnStock(stockFolder)

    if baseFolder != None:
        if not os.path.isdir(baseFolder):
            print('ERROR: Path "{}" does not exist'.format(baseFolder))
            exit(-1)
        for stock in os.listdir(baseFolder):
            stockDir = os.path.join(baseFolder, stock)
            if os.path.isdir(stockDir):
                runOnStock(os.path.join(baseFolder, stock))



def main():
    utility.printStartTimeStamp()

    run()

    #parser.add_argument('-s', 'stockSymbol', nargs=99999, action='append', help='stock symbols')
    #metavar=('url','name'),help='help:')
    #args = parser.parse_args()

    #baseFolder = args.baseFolder



    #baseFolder = '/Users/ling/GitHub/babaProj/data'
    #stockList = ['000725', '000831', '600392']


    #stock = '601699'


    #path = os.path.join(baseFolder, stock)


    

    utility.printEndTimeStamp()



if __name__ == '__main__':
    main()

