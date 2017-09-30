#!/usr/local/bin/python3

# N天周期的移动平均EMA的计算公式：EMA = [当天的收盘价×2 + 前一天的EMA×（N-1)] / (N+1)
# 1. ./calculateMetrics.py [ -f folderName / -s stockName ]
# EMA21、EMA60、EMA200
# STD21、STD60、STD200
# VAR21、VAR60、VAR200
# (the std/var for the first N days is marked as 0)
# 
# 2. ./pickStockByDate -d 20001030 => stocks_date.csv
#
# 3. selecting stocks => output stocks_data.csv



import math
import optparse
import os

import cvsio
import simpleCalculate
import utility

def calculateStdVar(closeList, varN):
    if len(closeList) < varN:
        return []
    buffer = closeList[:60]
    resultStd = [0] * varN
    resultVar = [0] * varN

    i = varN
    while i < len(closeList):
        buffer.pop(0)
        buffer.append(closeList[i])
        calculator = simpleCalculate.Calculator(buffer)
        resultStd.append(calculator.getStdDeviation())
        resultVar.append(calculator.getVariance())

        i += 1

    return [resultStd, resultVar]


def calculateEma(closeList, emaN):
    if len(closeList) < 1:
        return []   # warning reported in csvio
    assert(emaN > 1)

    resultList = []
    resultList.append(closeList[0])

    i = 1
    while i < len(closeList):
        ema = (closeList[i] * 2 + resultList[i-1] * (emaN-1) ) / (emaN + 1)
        resultList.append(ema)
        i += 1

    return resultList
    

ratioNumberList = [21, 60, 200]
varNumberList = [21, 60, 200]
titleList = ['date', 'open', 'high', 'low', 'close', 'volume', 'turnover']
def runOnStock(stockFile, outputFolderName):
    if not stockFile.endswith('.txt'):
        return

    inputFileName = os.path.basename(os.path.normpath(stockFile)).replace('.txt', '')
    outputFileName = os.path.join(outputFolderName, inputFileName)

    readObject = cvsio.Reader(stockFile)
    emaList = []
    stdList = []
    varList = []

    for ratioN in ratioNumberList:
        emaResult = calculateEma(readObject.getCloseList(), ratioN)
        if len(emaResult) == 0:
            return  # calculation error, abort for this file

        stdVarResult = calculateStdVar(readObject.getCloseList(), ratioN)
        if len(stdVarResult) != 2 or len(stdVarResult[0]) == 0 or len(stdVarResult[1]) == 0:
            return  # calculation error, abort for this file

        emaList.append(emaResult)
        stdList.append(stdVarResult[0])
        varList.append(stdVarResult[0])
        
    writeObject = cvsio.Writer(outputFileName, titleList, ratioNumberList)
    writeObject.writeContent(readObject.getAllList(), emaList + stdList + varList)


def run():
    parser = optparse.OptionParser()
    parser.add_option('-f', '--base-folder', action='store', dest='baseFolder',
        help="Expecting folders with stock name under this folder", default=None)
    parser.add_option('-s', '--stock-file', action='store', dest='stockFile',
        help="Expecting folders with stock name under this folder", default=None)

    options, args = parser.parse_args()

    baseFolder = options.baseFolder
    stockFile = options.stockFile

    if baseFolder == None and stockFile == None:
        print('Error: no stock path specified, please run --help for more information')
        exit(-1)
    if baseFolder != None and stockFile != None:
        print('Error: base folder and stock file path cannot be both specified, please run --help for more information')
        exit(-1)

    outputFolderName = utility.getTimeStampedOutPutName()
    assert(not os.path.exists(outputFolderName))
    os.makedirs(outputFolderName)

    if stockFile != None:
        if not os.path.isfile(stockFile):
            print('ERROR: Path "{}" does not exist'.format(stockFile))
            exit(-1)

        runOnStock(stockFile, outputFolderName)

    if baseFolder != None:
        if not os.path.isdir(baseFolder):
            print('ERROR: Path "{}" does not exist'.format(baseFolder))
            exit(-1)
        for stock in os.listdir(baseFolder):
            stockDir = os.path.join(baseFolder, stock)
            if os.path.isfile(stockDir):
                runOnStock(os.path.join(baseFolder, stock), outputFolderName)
                print('.', end='', flush=True)
        print()



def main():
    utility.printStartTimeStamp()

    run()

    utility.printEndTimeStamp()



if __name__ == '__main__':
    main()

