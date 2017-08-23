import datetime

import os

class IO(object):
    fd = None
    numOfEntries = 0

    def __init__(self, num):
        global fd
        global numOfEntries

        numOfEntries = num
        timeStamp = '{}'.format(datetime.datetime.now()).replace('-', '_')
        
        # \todo enable print by timeStamp
        #fd = open('output_{}'.format(timeStamp), 'w+')
        os.system('rm output.txt')
        fd = open('output.txt', 'w+')

    def __del__(self):
        fd.close()

    def write(self, lst):
        #assert(len(lst) == numOfEntries)
        fd.write(','.join(lst) + '\n')


