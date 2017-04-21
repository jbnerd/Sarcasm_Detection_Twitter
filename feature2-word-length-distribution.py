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