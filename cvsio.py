import datetime
import os

from enum import Enum

class TickType(Enum):
    BUY = 1
    SELL = 2

class Reader(object):
    timeList = []
    priceList = []
    buySellList = []
    tickNumList = []

    def __init__(self, fileName):
        assert(fileName.endswith('.csv'))
        with open(fileName, 'r') as fh:
            lines = fh.readlines()
            for line in lines:
                splitted = line.split(',')
                if len(splitted) != 4:
                    continue
                self.timeList.append(int(splitted[0]))
                self.priceList.append(float(splitted[1]))
                if splitted[2] == 'B':
                    self.buySellList.append(TickType.BUY)
                elif splitted[2] == 'S':
                    self.buySellList.append(TickType.SELL)
                else:
                    print('ERROR: unexpected buySell type')
                    exit(-1)
                self.tickNumList.append(int(splitted[3]))

    def getPriceList(self):
        return self.priceList

    def getTimeList(self):
        return self.timeList

    def getBuySellList(self):
        return self.buySellList

        

class Writer(object):
    fd = None
    numOfEntries = 0

    def __init__(self, num):
        global fd
        global numOfEntries

        numOfEntries = num
        timeStamp = '{}'.format(datetime.datetime.now()).replace('-', '_')
        
        # \todo enable print by timeStamp
        #fd = open('output_{}'.format(timeStamp), 'w+')
        fd = open('output.txt', 'w+')

    def __del__(self):
        fd.close()

    def write(self, lst):
        #assert(len(lst) == numOfEntries)
        fd.write(','.join(lst) + '\n')


