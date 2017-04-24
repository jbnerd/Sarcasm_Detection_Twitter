import numpy
import curses
from curses.ascii import isdigit
import nltk
from syllables import *
from collections import Counter
import os
import csv
import math

def feature_syllables(tweet):
    words=0
    pollysyllable=0
    syllable=0
    for word in tweet:
        words+=1
        syllable += sylco(word)
        if syllable>2:
            pollysyllable+=1
        
    return [words, pollysyllable, syllable, pollysyllable/words, syllable/words]

def mode(lda):
    data = Counter(lda)
    return data.most_common(1)[0][0]

def word_length_distribution(tweet):
    lda=[0]*19
    for word in tweet:
        if(len(word))<20:
            lda[len(word)-1]+=1
    return lda

def word_length_distribution_feature(tweet):
    lda = word_length_distribution(tweet)
    arr=[]
    for i in range(19):
        if lda[i]>0:
           arr += [i+1]*lda[i]
    return (numpy.average(arr), numpy.median(arr), mode(lda), numpy.std(arr), max(lda), min(lda))

def JS(d1,d2):
    mean = [(float(x)+ float(y))/2 for x,y in zip(d1, d2)]
    div1 = KL(d1,mean)
    div2 = KL(d2,mean)
    return float(0.5*div1) + float(0.5*div2)

def KL(t1,t2):
    return sum([t1[i] * math.log(t1[i]/t2[i]) for i in range(len(t1)) if t1[i] != 0 if t2[i] != 0])

def writeFile(folder,csvfile):
   
    f2 = csv.writer(csvfile,delimiter=",")
    for f in sorted(os.listdir(folder)):
        inputFile = open(os.path.join(folder,f),"r")
        reader= list(csv.reader(inputFile))
        tweet = reader[1][2]
        prev_tweet = ""
        flist = []
        
        for i in range(2,len(reader)):
            prev_tweet += reader[i][2]
        
        d1 = word_length_distribution(tweet)
        d2 = word_length_distribution(prev_tweet)

        flist += feature_syllables(tweet)
        flist += word_length_distribution_feature(tweet)
        flist.append(JS(d1,d2))

        f2.writerow(flist)

        inputFile.close()

        
def main():
    pwd = os.getcwd()
    norm = pwd + "/normal_with_past_PP"
    sarc = pwd + "/sarcastic_with_past_PP"
    csvfile = open("feature2.csv","w")
    writeFile(norm,csvfile)
    writeFile(sarc,csvfile)
    csvfile.close()


if __name__=="__main__":
    main()