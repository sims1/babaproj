from functools import reduce
import math


class Calculator:

    n = None
    average = None
    medium = None
    variance = None
    stdDeviation = None
    kurtosis = None
    skewness = None

    lst = None
    x_minus_mean_lst = None

    def __init__(self, lst):
        self.lst = lst

    def getN(self):
        if self.n is None:
            self.n = len(self.lst)
            assert(self.n != 0)
        return self.n

    def getAverage(self):
        if self.average is None:
            self.average = sum(self.lst) / self.getN()
        return self.average

    def getMedium(self):
        if self.medium is None:
            middleIndex = self.getN() / 2
            sortedList = sorted(self.lst)
            if self.getN() % 2 == 1:
                self.medium = sortedList[middleIndex]
            else:
                self.medium = (sortedList[middleIndex - 1] + sortedList[middleIndex]) / 2
        return self.medium

    def __get_x_minus_mean_lst(self):
        if self.x_minus_mean_lst is None:
            self.x_minus_mean_lst = map(lambda x : x - self.getAverage(), self.lst)
        return self.x_minus_mean_lst

    def __get_power_of_xm_lst(self, power):
        result = 0
        for i in self.__get_x_minus_mean_lst():
            result += math.pow(i, power)
        return result

    def getVariance(self):
        if self.variance is None:
            sum = self.__get_power_of_xm_lst(2)
            self.variance = sum / self.getN()
        return self.variance

    def getStdDeviation(self):
        if self.stdDeviation is None:
            self.stdDeviation = math.sqrt(self.getVariance())
        return self.stdDeviation

    def getKurtosis(self):
        if self.kurtosis is None:
            sum = self.__get_power_of_xm_lst(4)
            quadraStd = math.pow(self.getStdDeviation(), 4)

            self.kurtosis = ( sum / (self.getN()-1) / quadraStd ) - 3
        return self.kurtosis

    def getSkewness(self):
        if self.skewness is None:
            sum = self.__get_power_of_xm_lst(3)
            tripleSqrStd = math.pow(self.getStdDeviation(), 3)
            self.skewness = sum / (self.getN()-1) / tripleSqrStd
        return self.skewness


