# -*- coding: utf-8 -*-

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

    import os
    import math

    path = "D:\python\\freqpattern\count_permissions"
    dir_path = os.listdir(path)

    outfile = open("result.txt", "w")

    for dir in dir_path:
        total_permission_path = os.path.join(path, dir)
        for file in os.listdir(total_permission_path):

            f = open("%s/" % total_permission_path + file, "r")

            lines = len(f.readlines())

            if lines != 0:

                print(lines)

                f.seek(0)

                dataSetDict, dataSet = loadDblpData(f)

                f.close()

                min_sup = 0.1
                freqItems = fp_growth(dataSetDict, math.ceil(min_sup * lines))
                freqItems = sorted(freqItems.iteritems(), key=lambda item: item[1], reverse=True)

                for item in freqItems:
                   print(item)

                max = 0
                index = 0
                for i, item in enumerate(freqItems):
                    if len(item[0]) > max:
                        max = len(item[0])
                        index = i

                print(freqItems[index])

                outfile.write("%s" % dir + ": " + str(freqItems[index]) + " " + str(lines) + '\n')

    outfile.close()


















