import numpy
import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict


d=cmudict.dict()

def nsyl(word):
    return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]]

def feature_syllables(tweet):
    i=0
    j=0
    k=0
    ls=tweet.split(" ")
    for word in ls:
        i+=1
        k+=nsyl(word)[0]
        if k>2:
            j+=1
        
    return [i,j,k,j/i,k/i]

print(feature_syllables('How you doing'))

def mode(lda):
    maxkey=1
    max=0
    for i in range(20):
        if lda[i]>max:
            maxkey=i
    return maxkey

def word_length_distribution(tweet):
    wordlist=tweet.split(" ")
    lda=[0 for x in range(0,20)]

    for i in wordlist:
        if(len(i))<=20:
            lda[len(i)-1]+=1
    arr=[]
    for i in range(20):
        for j in range(lda[i]):
            if lda[i]>0:
                arr.append(i)

    return (numpy.average(arr), numpy.median(arr),mode(lda), numpy.std(arr), numpy.amax(lda), numpy.amin(lda))

def JS(d1,d2):
    mean = [(float(x)+ float(y))/2 for x,y in zip(d1, d2)]
    div1 = KL(d1,mean)
    div2 = KL(d2,mean)
    return float(0.5*div1) + float(0.5*div2)

def KL(t1,t2):
    sum=0
    for i in range(len(t1)):
        x = float(t1[i])/float(t2[i])
        if x >0:
          value = math.log(x)*t1[i]
        else:
          value =0
        sum =sum+value
    return sum


