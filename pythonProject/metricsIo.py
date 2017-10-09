import datetime
import os

class Reader(object):
    allList = []
    closeList = []
    
    def __init__(self, fileName):
        assert(fileName.endswith('.txt'))

        self.allList = []
        self.closeList = []

        with open(fileName, 'r', encoding = 'ISO-8859-1') as fh:
            lines = fh.readlines()
            assert(len(lines) > 2)
            lines = lines[2:]

            for line in lines:
                if len(line) < 1:
                    continue
                line = line[:-1] # remove '\n'
                splittedLine = line.split('\t')
                if len(splittedLine) != 7:
                    continue

                self.allList.append(splittedLine)
                self.closeList.append(float(splittedLine[4]))

        #if len(self.closeList) < 2:
            #print('WARNING: file {} is abnormal, please manually inspect it.'.format(fileName))

    def getAllList(self):
        return self.allList

    def getCloseList(self):
        return self.closeList


class Writer(object):
    titleStr = None
    def __init__(self, fileName, titleList, ratioNumberList):
        self.fileName = fileName
        if Writer.titleStr == None:
            lst = titleList + list(map(lambda x: 'EMA' + str(x), ratioNumberList)) \
                            + list(map(lambda x: 'STD' + str(x), ratioNumberList)) \
                            + list(map(lambda x: 'VAR' + str(x), ratioNumberList))
            Writer.titleStr = ','.join(lst) + '\n'

    def writeContent(self, allList, listOfRatioList):
        assert(len(listOfRatioList) != 0)

        size = len(allList)
        for ratioList in listOfRatioList:
            assert(len(ratioList) == size)

        fd = open('{}.csv'.format(self.fileName), 'a+')
        fd.write(Writer.titleStr)

        i = 0;
        while i < size:
            lst = allList[i]
            for ratioList in listOfRatioList:
                lst.append(str(ratioList[i]))
            fd.write(','.join(lst) + '\n')
            i += 1

        fd.close()

