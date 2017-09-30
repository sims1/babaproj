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
    parser.add_option('-i', '--input-stock', action='store', dest='inputStock',
        help='Expecting folders with stock name under this folder or a txt stock file', default=None)
    parser.add_option('-o', '--output-folder', action='store', dest='outputFolder',
        help='The calcualted matrics will be stored in the folder', default=None)
    parser.add_option('-f', action='store_true', dest='doOverwrite')

    options, args = parser.parse_args()

    inputStock = options.inputStock
    outputFolder = options.outputFolder
    doOverwrite = options.doOverwrite

    if inputStock == None:
        print('Error: no stock path not stock file specified, please run --help for more information')
        exit(-1)

    outputFolderName = ""
    if outputFolder == None:
        outputFolderName = utility.getTimeStampedOutPutName()
    else:
        outputFolderName = outputFolder

    if not doOverwrite:
        if os.path.exists(outputFolderName):
            print('Error: \'{}\' folder exists already, please use -f option, that allow you to overwrite it'.format(outputFolderName))
            exit(-1)
    os.makedirs(outputFolderName)

    if os.path.isfile(inputStock):
        runOnStock(inputStock, outputFolderName)
    elif os.path.isdir(inputStock):
        for stock in os.listdir(inputStock):
            stockDir = os.path.join(inputStock, stock)
            if os.path.isfile(stockDir):
                runOnStock(os.path.join(inputStock, stock), outputFolderName)
                print('.', end='', flush=True)
        print()
    else:
        print('Error: {} is neither a stock folder nor a stock file'.format(inputStock))
        exit(-1)



def main():
    utility.printStartTimeStamp()

    run()

    utility.printEndTimeStamp()



if __name__ == '__main__':
    main()

