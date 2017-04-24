import sys 
from string import ascii_lowercase
import nltk 
from nltk import bigrams
import string
import re
import os
import csv
from nltk.stem.snowball import SnowballStemmer
from ExtraPreProc import remove_stop_words
# reload(sys)  
# sys.setdefaultencoding('utf8')

bidict={}
tridict={}

def getSentiStrength(w):
	try:
		stemmer = SnowballStemmer("english",ignore_stopwords=True)
		w = stemmer.stem(w)
	except:
		w = w
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

	for bi in bigrams:
		if bi in bidict:
			if bidict[bi]>0:
				possum+= float(bidict[bi])
				poscount=poscount + 1
				# print "here1"
			else:
				negsum+= float(bidict[bi])
				negcount=negcount+1

	for tri in trigrams:
		if tri in tridict:
			if tridict[tri]>0:
				possum+= float(tridict[tri])
				poscount=poscount+1
				# print "here2"
		
			else:
				negsum+=float(tridict[tri])
				negcount=negcount+1
	
	delta_affect = (max(affectscores) - min(affectscores))
	delta_sentiment= (max(sentiscores)-min(sentiscores))

	output = [delta_affect, delta_sentiment, poscount, possum, negcount, negsum]

	return output


def writeFile(folder, file_name):
	# checking presence of repeated characters
	output_file = open(file_name, "w")
	writer = csv.writer(output_file)

	for f in sorted(os.listdir(folder)):
		inputFile = open(os.path.join(folder,f),"r")
		reader = list(csv.reader(inputFile))
		tweet = reader[1][2]
		tweet = " ".join(remove_stop_words(tweet))
		print tweet
		output = contrastingFeatures(tweet)
		print output

		writer.writerow(output)
		print output

	return

def main():
	
	with open('bigramscores.csv','r') as file2:
		for line in file2:
			key = line.split(",")[0]
			val = line.split(",")[1]
			bidict[key]=float(val)
	file2.close()

	with open('trigramscores.csv','r') as file2:
		for line in file2:
			key = line.split(",")[0]
			val = line.split(",")[1]
			bidict[key]=float(val)
	file2.close()

	# tweet = "i love getting spam mails"
	# tweet = " ".join(remove_stop_words(tweet))
	# print tweet
	# contrastingFeatures(tweet)
	pwd = os.getcwd()
	normal = pwd + "/normal_with_past_PP"
	sarcastic = pwd + "/sarcastic_with_past"
	writeFile(normal, "feature1_norm.csv")
	writeFile(sarcastic, "feature1_sarcastic.csv")



if __name__ == "__main__":
	main()


# function to read tweets from preprocessed data and pass to contrastingFeatures()
