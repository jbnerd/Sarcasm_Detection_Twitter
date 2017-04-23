import numpy
import curses
from curses.ascii import isdigit
import nltk
from syllables import *
from collection import Counter


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
