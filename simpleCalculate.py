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

    _min = None
    _max = None
    _range = None

    lst = None
    x_minus_mean_lst = None

    def __init__(self, lst):
        assert(len(lst) > 1)
        self.lst = lst

    def getN(self):
        if self.n is None:
            self.n = len(self.lst)
        return self.n

    def __calculateMinAndMax(self):
        self._min = self.lst[0]
        self._max = self.lst[0]
        for i in self.lst:
            if i > self._max:
                self._max = i
            if i < self._min:
                self._min = i

    def getMin(self):
        if self._min is None:
            self.__calculateMinAndMax()
        return self._min

    def getMax(self):
        if self._max is None:
            self.__calculateMinAndMax()
        return self._max

    def getRange(self):
        if self._range is None:
            self._range = self.getMax() - self.getMin()
        return self._range

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
            _sum = self.__get_power_of_xm_lst(2)
            self.variance = _sum / self.getN()
        return self.variance

    def getStdDeviation(self):
        if self.stdDeviation is None:
            self.stdDeviation = math.sqrt(self.getVariance())
        return self.stdDeviation

    def getKurtosis(self):
        if self.kurtosis is None:
            _sum = self.__get_power_of_xm_lst(4)
            quadraStd = math.pow(self.getStdDeviation(), 4)

            if quadraStd == 0:
                self.kurtosis = float('inf')
            else:
                self.kurtosis = ( _sum / (self.getN()-1) / quadraStd ) - 3
        return self.kurtosis

    def getSkewness(self):
        if self.skewness is None:
            _sum = self.__get_power_of_xm_lst(3)
            tripleSqrStd = math.pow(self.getStdDeviation(), 3)
            if tripleSqrStd == 0:
                self.skewness = float('inf')
            else:
                self.skewness = _sum / (self.getN()-1) / tripleSqrStd
        return self.skewness


