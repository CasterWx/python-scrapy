# coding=utf-8
import random
from math import log
from sklearn.model_selection import KFold
import numpy as np

def splitDataSet(dataSet,axis,value):
    retDataSet = []

    for featVec in dataSet:
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reduceFeatVec)

    return retDataSet


''' 
 
'''

def SplitData(dataSet, k, seed):
    testSet = []
    trainSet = []
    random.seed(seed)
    for user, item in dataSet:
        if random.randint(0,10) == k:
            testSet.append([user,item])
        else:
            trainSet.append([user,item])
    return testSet, trainSet


def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0])-1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain =0.0
    bestFeature = -1

    for i in range(numFeatures):
        featList = [sample[i] for sample in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)

        infoGain = baseEntropy - newEntropy

        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i

    return bestFeature

def calcShannonEnt(dataSet):
    countDataSet = len(dataSet)
    labelCounts={}
    for featVec in dataSet:
        currentLabel=featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    getshang = 0.0

    for key in labelCounts:
        prob = float(labelCounts[key])/countDataSet
        getshang -= prob * log(prob,2)
    return getshang



def createDataSet():
    dataSet = [
                [1, 1, 'yes'],
                [1, 0, 'no'],
                [1, 1, 'yes'],
                [0, 1, 'no'],
                [0, 0, 'no'],
                [1, 0, 'no'],
                [0, 1, 'no'],
                [1, 0, 'no'],
                [1, 1, 'yes'],
                [0, 1, 'no']
               ]

    labels = ['no surfacing','flippers']

    return dataSet, labels

if __name__ == '__main__':
    myDat,label =  createDataSet()
    train = np.array(myDat)
    loop = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    kf = KFold(n_splits=10)

    for train_index, test_index in kf.split(train):
        print("train:",train_index, "test:", test_index)
        X_train, X_test = train[train_index], train[test_index]
        y_train, y_test = loop[train_index], loop[test_index]
        print(calcShannonEnt(train[train_index]))