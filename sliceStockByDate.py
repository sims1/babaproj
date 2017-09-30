#!/usr/local/bin/python3

# 2. ./sliceStockByDate -i file/folder -d 20001030 => stocks_date.csv
#
# 3. selecting stocks => output stocks_data.csv

import math
import optparse
import os

import cvsio
import utility
    

ratioNumberList = [21, 60, 200]
varNumberList = [21, 60, 200]
titleList = ['date', 'open', 'high', 'low', 'close', 'volume', 'turnover']
def pickStock(stockFile, outputFile, date):
    if not stockFile.endswith('.csv'):
        return

    reader = cvsio.Reader(stockFile)

    doNeedTitle = not os.path.isfile(outputFile)
    title = reader.getTitle() if doNeedTitle else None
    writer = cvsio.Writer(outputFile, title)

    if date == None:
        writer.write(reader.getLatest())
    else:
        writer.write(reader.getByDate(date))


def run():
    parser = optparse.OptionParser()
    parser.add_option('-d', '--date', action='store', dest='date',
        help='Selecting all the stock data for all stocks on date specified', default=None)
    parser.add_option('-i', '--input-stock', action='store', dest='inputStock',
        help='Expecting a stock folder or stock file, should be csv file(s)', default=None)
    parser.add_option('-o', '--output-file', action='store', dest='outputFile',
        help='Output file, if it is not specified, default is stocksByDate_{}.csv', default=None)
    parser.add_option('-f', action='store_true', dest='doOverwrite')

    options, args = parser.parse_args()

    date = options.date
    inputStock = options.inputStock
    outputFile = options.outputFile
    doOverwrite = options.doOverwrite

    if date != None:
        if not date.isdigit() or len(date) != 8:
            print('Error: \'{}\' is not valid date'.format(date))
            exit(-1)

    if outputFile == None:
        outputFile = 'stocksByDate_{}.csv'.format(date)

    if os.path.isfile(outputFile):
        if doOverwrite:
            os.remove(outputFile)
        else:
            print('Error: output file \'{}\' already exists, you can use -f option to allow overwrite'.format(outputFile))
            exit(-1)

    if os.path.isfile(inputStock):
        pickStock(inputStock, outputFile, date)
    elif os.path.isdir(inputStock):
        for stock in os.listdir(inputStock):
            stockDir = os.path.join(inputStock, stock)
            if os.path.isfile(stockDir):
                pickStock(stockDir, outputFile, date)
                print('.', end='', flush=True)
        print()
    else:
        print('Error: \'{}\' file/folder does not exists'.format(inputStock))
        exit(-1)



def main():
    utility.printStartTimeStamp()

    run()

    utility.printEndTimeStamp()



if __name__ == '__main__':
    main()

