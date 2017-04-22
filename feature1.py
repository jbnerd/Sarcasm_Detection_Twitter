import sys 
from string import ascii_lowercase
import nltk 
from nltk import word_tokenize
from nltk import bigrams
import string
import re
import csv
from nltk.stem.snowball import SnowballStemmer
# reload(sys)  
# sys.setdefaultencoding('utf8')


def getSentiStrength(w):
	stemmer = SnowballStemmer("english",ignore_stopwords=True)
	w = stemmer.stem(w)
	sentidict = {}
	with open('senti.txt','r') as file2:
		for line in file2:
			temp = line.split()
			sentidict[temp[0]]=float(temp[1])


	if w in sentidict:
		return sentidict[w]
	else:
		for key,value in sentidict.iteritems():
			if key.find(w):
				return value
		#print w
		return 0 
		
def getAffect(w):
	affectdict ={}
	with open('affectscores.txt','r') as file1:
		for line in file1:
			temp = line.split()
			affectdict[temp[0]]=float(temp[1])

	if w in affectdict:
		return affectdict[w]
	else:
		for key,value in affectdict.iteritems():
			if key.find(w):
				return value
		#print w
		return 4.5

def contrastingFeatures(words):
	affectscores=[]
	sentiscores=[]
	bigrams = []
	trigrams = []
	bidict={}
	tridict={}
	poscount=0
	possum=0
	negcount=0
	negsum=0
	c=0
	new_words = []


	for w in words.split(" "):
		affectscores.append(getAffect(w))
		sentiscores.append(getSentiStrength(w))

	new_words+=(words.split(" "))
	l = len(new_words)

	while c<=l-2:
		bigrams.append(new_words[c]+new_words[c+1])
		c=c+1

	c=0
	while c<=l-3:
		trigrams.append(new_words[c]+new_words[c+1]+new_words[c+2])
		c=c+1

	with open('bigramscores.csv','r') as file2:
		for line in file2:
			temp = line.split()
			bidict[temp[0]]=float(temp[1])
	file2.close()

	with open('trigramscores.csv','r') as file2:
		for line in file2:
			temp = line.split()
			tridict[temp[0]]=float(temp[1])
	file2.close()

	for bi in bigrams:
		if bi in bidict:
			if bidict[bi]>0:
				possum+= bidict[bi]
				poscount=poscount + 1
				print "here1"
			else:
				negsum+=bidict[bi]
				negcount=negcount+1

	for tri in trigrams:
		if tri in tridict:
			if tridict[tri]>0:
				possum+= tridict[tri]
				poscount=poscount+1
				# print(poscount)
				# print(possum)
			else:
				negsum+=tridict[tri]
				negcount=negcount+1
	
	delta_affect = (max(affectscores) - min(affectscores))
	delta_sentiment= (max(sentiscores)-min(sentiscores))
	print(poscount)
	print(possum)
	print(negcount)
	print(negsum)

	print((trigrams))
	# print(len(bidict))

	output = [delta_affect, delta_sentiment, poscount, possum, negcount, negsum]

	output_file = open("feature1.csv", "w");
	writer = csv.writer(output_file)
	writer.writerow(output)

	return output



# tweet = "i love getting spam mails"

# contrastingFeatures(tweet)
# bigram_score(tweet)
