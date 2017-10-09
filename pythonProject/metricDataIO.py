import datetime
import os

class Reader(object):
    latestDate = None # this is only useful for getLatest()

    def __init__(self, fileName):
        self.fileName = fileName
        assert(fileName.endswith('.csv'))
        self.stockSymbolWithComma = os.path.basename(fileName).replace('.csv', '') + ','
        self.dateToData = None

        #with open(fileName, 'r', encoding = 'ISO-8859-1') as fh:
        with open(fileName, 'r') as fh:
            lines = fh.readlines()
            assert(len(lines) > 1)
            self.lines = lines

    def getTitle(self):
        return 'stock,' + self.lines[0]

    def getLatest(self):
        if self.__getLatestDate() != Reader.latestDate:
            #print('Warning: file \'{}\' does not match the latest date \'{}\' '.format(self.fileName, Reader.latestDate))
            return ''
        return self.stockSymbolWithComma + self.lines[-1]

    def __getLatestDate(self):
        if Reader.latestDate == None:
            latestLine = self.lines[-1]
            Reader.latestDate = latestLine.split(',', 1)
        return Reader.latestDate

    def __loadDateToData(self):
        self.dateToData = {}

        dataLines = self.lines[1:]
        for line in dataLines:
            if len(line) < 1:
                continue
            splittedLine = line.split(',', 1)
            if len(splittedLine) < 2:
                continue
            dateKey = splittedLine[0]
            self.dateToData[dateKey] = line

    def getByDate(self, date):
        if self.dateToData == None:
            self.__loadDateToData()

        if date not in self.dateToData:
            #print('Warning: date \'{}\' does not exist in file \'{}\''.format(date, self.fileName))
            return ''
        return self.stockSymbolWithComma + self.dateToData[date]


class Writer(object):
    def __init__(self, fileName, title):
        self.fileName = fileName
        if title == None:
            return
        self.write(title)

    def write(self, content):
        with open(self.fileName, 'a') as fd:
            fd.write(content)


