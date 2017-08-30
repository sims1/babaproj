import math

class Calculator:
    n = None
    average = None
    medium = None
    variance = None

    def getN(self, lst):
        if self.n is None:
            self.n = len(lst)
            assert(self.n != 0)
        return self.n

    def getAverage(self, lst):
        if self.average is None:
            self.average = sum(lst) / self.getN(lst)
        return self.average

    def getMedium(self, lst):
        if self.medium is None:
            middleIndex = self.getN(lst) / 2
            sortedList = sorted(lst)
            if len(lst) % 2 == 1:
                self.medium = sortedList[middleIndex]
            else:
                self.medium = (sortedList[middleIndex - 1] + sortedList[middleIndex]) / 2
        return self.medium

    def getVariance(self, lst):
        if self.variance is None:
            sum = 0
            for i in lst:
                sum += math.pow((i - self.getAverage(lst)), 2)
            self.variance = sum / self.getN(lst)
        return self.variance
    

