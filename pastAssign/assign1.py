#!/usr/bin/python

# Across a period of time, find
#     - average
#     - medium
#     - first N modes


import os

import firstNMode
import simpleCalculate
import utility


def run(path, firstNModes):
    utility.printStartTimeStamp()
    
    targetList = utility.getPriceListFromFolder(path)
    assert(len(targetList) != 0)
    
    # Caution: there is no check for the consecutivity of the days
    print(utility.getTitle(path))
    
    average = simpleCalculate.getAverage(targetList)
    print('\taverage: {}'.format(average))

    medium = simpleCalculate.getMedium(targetList)
    print('\tmedium: {}'.format(medium))

    firstNModeToOccurences = firstNMode.getFirstNModeToOccurences(targetList, firstNModes)
    firstNMode.printFirstNModeToOccurences(firstNModeToOccurences)

    utility.printEndTimeStamp()


def main():
    firstNModes = 10;
    
    baseFolder = '/Users/ling/GitHub/babaProj'
    #stockList = ['000725', '000831', '600392']

    stockList = ['000831']

    for stock in stockList:
        path = os.path.join(baseFolder, stock)
        run(path, firstNModes)
        print('')

        

if __name__ == '__main__':
    main()

