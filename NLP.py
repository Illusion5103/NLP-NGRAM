#!/usr/bin/env python3
from hw8_1 import getDict
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import string
import os
from matplotlib.pyplot import figure

def hugeDict(file1, file2, file3, file4, file5, file6) :
    #creates a mega set of all ngrams and sorts them alphabetically
    dict1 = getDict(file1)
    dict2 = getDict(file2)
    dict3 = getDict(file3)
    dict4 = getDict(file4)
    dict5 = getDict(file5)
    dict6 = getDict(file6)
    dict1keys = frozenset(dict1.keys())
    dict2keys = frozenset(dict2.keys())
    dict3keys = frozenset(dict3.keys())
    dict4keys = frozenset(dict4.keys())
    dict5keys = frozenset(dict5.keys())
    dict6keys = frozenset(dict6.keys())
    alphabetSet = frozenset([dict1keys, dict2keys, dict3keys, dict4keys, dict5keys, dict6keys])
    alphabetList = list(alphabetSet)
    x = sorted(alphabetList)
    return x

def countMaker(alphabetSet, filename) :
    #makes a list of length alphabetSet. Iterates through alphabetSet. For each element, counts how
    #many times it shows up in filename. Sets this value to list[i] where i == alphabetSet[i].
    #Sends the output and the filename to histo to make a plot.
    list = [] * len(alphabetSet)
    diction = getDict(filename)
    holder = 0
    for items in alphabetSet :
        holder = diction.get(items, 0)
        list.append(holder)
    plotHisto(list, filename)

def plotHisto(bars, filename, minrange = 0.0, maxrange = 100.0, plotinline = False) :
    #plots histograms
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

def getText(filename) :
    #opens files
    with open(filename) as f :
        read_data = f.read()
    return read_data.splitlines()

def getNgrams(line) :
    #Ngram preprocessing
    #adds padding and makes text lowercase
    var = "__"
    line = var + line + var
    line = line.lower()
    ngrams = []
    for i in range(len(line)-4) :
        ngrams.append(line[i:i+3])
    return ngrams

def getDict(filename) :
    #makes dictionary of ngrams
    stringList = getText(filename)
    ngram = []
    for i in stringList :
        ngram.extend(getNgrams(i))
    diction = {}
    diction = dict(Counter(ngram))
    return diction

def main() :
    #controls the sending of the 6 text files
    #this part can be replaced with any text files; it will work with any text of any language
    alphabetSet = hugeDict('ngrams/english.txt', 'ngrams/spanish.txt', 'ngrams/italian.txt', 'ngrams/fr$    countMaker(alphabetSet, 'ngrams/english.txt')
    countMaker(alphabetSet, 'ngrams/spanish.txt')
    countMaker(alphabetSet, 'ngrams/italian.txt')
    countMaker(alphabetSet, 'ngrams/french.txt')
    countMaker(alphabetSet, 'ngrams/german.txt')
    countMaker(alphabetSet, 'ngrams/portuguese.txt')

if __name__ == '__main__' :
    main()
