# -*- coding: utf-8 -*-
"""
@author: Infaraway
@time: 2018/5/14 16:36
@Function:
"""
from FPgrowth import fp_growth


def test_fp_growth(minSup, dataSetDict, dataSet):
    freqItems = fp_growth(dataSetDict, minSup)
    freqItems = sorted(freqItems.iteritems(), key=lambda item: item[1])
    return freqItems


def loadDblpData(inFile, flag=' ', row_num=1):
    '''
    加载dblp的数据
    :param inFile:
    :return:
    '''
    dataSetDict = {}
    dataSet = []
    count = 0
    for line in inFile:
        # if count > row_num:
        #     break
        line = line.strip().split(':')
        line = line[1].strip().split(flag)
        dataSet.append(line)
        dataLine = [word for word in line]
        dataSetDict[frozenset(dataLine)] = dataSetDict.get(frozenset(dataLine), 0) + 1
        count += 1
    return dataSetDict, dataSet


if __name__ == '__main__':
    dataSetDict, dataSet = loadDblpData(open('weather_permission.txt'))
    f = open('weather_permission.txt')
    lines = len(f.readlines())
    min_sup = 0.2 * lines
    freqItems = fp_growth(dataSetDict, min_sup)
    freqItems = sorted(freqItems.iteritems(), key=lambda item: item[1], reverse=True)
    max = 0
    index = 0
    for i, item in enumerate(freqItems):

        if len(item[0]) > max:
            max = len(item[0])
            index = i
    print(freqItems[index], len(freqItems[index][0]))
        # print(item)