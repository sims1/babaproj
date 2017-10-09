#!/usr/local/bin/python3

# 3. ./stockFilter.py -i inputFile -s -ema
# required options:
#         [ -i input file/folder name ]
#         [ -s strategy, current one is -ema, which is
#             close >= EMA21 && close >= EMA60 && close >= EMA200, and
#             close <= EMA21 * 1.10 ]


import math
import optparse
import os

import stockFilterIO
import utility
    

ratioNumberList = [21, 60, 200]
varNumberList = [21, 60, 200]
titleList = ['date', 'open', 'high', 'low', 'close', 'volume', 'turnover']
def pickStock(stockFile, outputFile):
    if not stockFile.endswith('.csv'):
        return

    reader = stockFilterIO.Reader(stockFile)

    # each entry of the list is [stockSymbol, ema21, ema60, ema200]
    stockToEmaList = reader.getStockToEmas()

'''

    doNeedTitle = not os.path.isfile(outputFile)
    title = reader.getTitle() if doNeedTitle else None
    writer = metricDataIO.Writer(outputFile, title)

    if date == None:
        writer.write(reader.getLatest())
    else:
        writer.write(reader.getByDate(date))
        '''


def run():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--input-stock', action='store', dest='inputStock',
        help='Expecting a file, should be csv file(s)', default=None)
    parser.add_option('-o', '--output-file', action='store', dest='outputFile',
        help='Output file, if it is not specified, print directly', default=None)
    parser.add_option('-f', action='store_true', dest='doOverwrite')

    options, args = parser.parse_args()

    inputStock = options.inputStock
    outputFile = options.outputFile
    doOverwrite = options.doOverwrite

    if not os.path.isfile(inputStock):
        print('Error: \'{}\' file does not exists'.format(inputStock))
        exit(-1)

    if os.path.isfile(outputFile):
        if doOverwrite:
            os.remove(outputFile)
        else:
            print('Error: output file \'{}\' already exists, you can use -f option to allow overwrite'.format(outputFile))
            exit(-1)

    
    filterStocks(inputStock, outputFile)



def main():
    utility.printStartTimeStamp()

    run()

    utility.printEndTimeStamp()



if __name__ == '__main__':
    main()

