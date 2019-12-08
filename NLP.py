#!/usr/bin/env python3
from hw8_1 import getDict
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import string
import os
from matplotlib.pyplot import figure

#creates a mega set of all ngrams and sorts them alphabetically
def hugeDict(file1, file2, file3, file4, file5, file6) :
    dict1 = getDict(file1)
    dict2 = getDict(file2)
    dict3 = getDict(file3)
    dict4 = getDict(file4)
    dict5 = getDict(file5)
    dict6 = getDict(file6)
    bigSet = set()
    bigSet.update(dict1.keys())
    bigSet.update(dict2.keys())
    bigSet.update(dict3.keys())
    bigSet.update(dict4.keys())
    bigSet.update(dict5.keys())
    bigSet.update(dict6.keys())
    return bigSet

#makes a list of length alphabetSet. Iterates through alphabetSet. For each element, counts how
#many times it shows up in filename. Send the full list and filename to plotHisto to make six plots.
def countMaker(alphabetSet, filename) :
    countList = [0] * len(alphabetSet)
    diction = getDict(filename)
    dictionSet = set()
    dictionSet.update(diction.keys())
    count = 0
    for item in alphabetSet :
        for entry in dictionSet :
            if entry == item :
                countList[count] += 1
        count += 1
    plotHisto(countList, filename)

#plots histogram
def plotHisto(bars, filename, minrange = 0.0, maxrange = 100.0, plotinline = False) :
    figure(num=None, figsize=(8, 6), dpi=400, facecolor='w', edgecolor='k')
    mrange = maxrange - minrange
    binsize = mrange/len(bars)
    labels = [(mrange / len(bars)) * i + minrange for i in range(len(bars))]
    plt.bar(labels, bars, align = 'edge', width = binsize)
    newFile = os.path.splitext(filename)[0]
    if plotinline :
        pltshow()
    else :
        plt.savefig(newFile)
        #plt.show()
        plt.clf()

#gets text
def getText(filename) :
    with open(filename) as f :
        read_data = f.read()
    return read_data.splitlines()

#ngram preprocessing
#adds padding and makes text lowercase
def getNgrams(line) :
    var = "__"
    line = var + line + var
    line = line.lower()
    ngrams = []
    for i in range(len(line)-4) :
        ngrams.append(line[i:i+3])
    return ngrams

#creates dictionaries of ngrams
def getDict(filename) :
    stringList = getText(filename)
    ngram = []
    for i in stringList :
        ngram.extend(getNgrams(i))
    diction = {}
    diction = dict(Counter(ngram))
    return diction

#controls the sending of the 6 text files 
#this part can be replaces with any text files; it will work with text of any language
def main() :
    alphabetSet = hugeDict('ngrams/english.txt', 'ngrams/spanish.txt', 'ngrams/italian.txt', 'ngrams/french.txt', 'ngrams/german.txt', 'ngrams/portuguese.txt')
    test = countMaker(alphabetSet, 'ngrams/english.txt')
    countMaker(alphabetSet, 'ngrams/spanish.txt')
    countMaker(alphabetSet, 'ngrams/italian.txt')
    countMaker(alphabetSet, 'ngrams/french.txt')
    countMaker(alphabetSet, 'ngrams/german.txt')
    countMaker(alphabetSet, 'ngrams/portuguese.txt')
    countMaker(alphabetSet, 'ngrams/mystery.txt')
    
if __name__ == '__main__' :
    main()
