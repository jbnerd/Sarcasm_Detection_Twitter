import numpy


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
            lda[len(i)]+=1
    arr=[]
    for i in range(20):
        for j in range(lda[i]):
            arr.append(i)
   
    return (numpy.average(arr), numpy.median(arr),mode(lda), numpy.std(arr), numpy.amax(lda), numpy.amin(lda)) 
        
sample="Hello world"

l=word_length_distribution(sample)
print(l)