# -*- coding: utf-8 -*-

import re
import nltk
import os
import csv


def get_pos_features(words):
	tags=[]
	# words=' '.join(i for i in wordsl)
	pos_tags ={
	'JJ':0,
	'JJR':0,
	'JJS':0,
	'MD':0,
	'NN':0,
	'NNP':0,
	'PR':0,
	'RB':0,
	'RBR':0,
	'RBS':0,
	'UH':0,
	'V':0,
	'W':0,
	}
	for item in words:
		print (item)
		print(type(item))
		print (item.lower())
		print (type(item.lower()))
		try:

			tokenized = nltk.word_tokenize(item.lower())
			print ('ok')
			tagged = nltk.pos_tag(tokenized)
			print ('here')
			print (tagged)
			tags.append(tagged[0][1])
		except Exception as e:
			# print(str(e))
			print ('except')
			pass
	# print (tags)

	probs=[]
	for i in pos_tags.keys():
			pos_tags[i]=tags.count(i)
	pos_tags['V']=tags.count('VB')+tags.count('VBD')+tags.count('VBG')+tags.count('VBN')+tags.count('VBP')+tags.count('VBZ')
	pos_tags['W']=tags.count('WDT')+tags.count('WP')+tags.count('WP$')+tags.count('WRB')
	pos_tags['PR']=tags.count('PRP')+tags.count('PRP$')
	w_count=float(len(words))
	if w_count!=0:
		print (words)
		probs=[x/w_count for x in pos_tags.values()]
		print (probs)
	# print (probs)
	else:
		probs=[0 for x in pos_tags.values()]
	return probs


def get_emoji_Features(raw_tweet):
	features=[]
	possum=0
	posnum=0
	negsum=0
	negnum=0
	emoji={
	'😀' : 3,
	'😃' : 4,
	'😄' : 3,
	'😁' : 4,
	'😆' : 5,
	'😅' : 2,
	'😂' : 5,
	'😊' : 3,
	'☺️' : 3,
	'😇' : 2,
	'🙂' : 1,
	'🙃' : 1,
	'😉' : 2,
	'😌' : 1,
	'😍' : 4,
	'😘' : 3,
	'😋' : 3,
	'😜' : 2,
	'😝' : 3,
	'😛' : 2,
	'😎' : 2,
	'😒' : -2,
	'😞' : -3,
	'😔' : -2,
	'😟' : -3,
	'😕' : -1,
	'🙁' : -2,
	'☹️' : -3,
	'😣' : -4,
	'😖' : -4,
	'😦' : -1,
	'😧' : -2,
	'😰' : -4,
	'😢' : -4,
	'😥' : -3,
	'✌️' : 2,
	'👍' : 2,
	'👎' : -2,
	'❤️' : 5,
	'💕' : 4,
	'❣️' : 4,
	'💔' : -4,
	'😭' : -5,
	'😓' : -4,
	'😪' : -3,
	'😠' : -3,
	'😡' : -5,
	'😣' : -5,
	'😖' : -4,
	'😫' : -4,
	'😩' : -5,
	}
	punct=['?','!','\"']
	for emo in emoji.keys():
		#features.append(raw_tweet.count(emo))
		if raw_tweet.count(emo)>0:
			if emoji[emo]<0:
				negnum += raw_tweet.count(emo)
				negsum += raw_tweet.count(emo)*emoji[emo]
			else:
				posnum += raw_tweet.count(emo)
				possum += raw_tweet.count(emo)*emoji[emo]
	features.extend((possum,negsum))
	# print features

	temp = re.findall(r"[\w']+", raw_tweet)
	print (temp)
	print (list(filter(lambda x:x.isupper(),temp)))
	pos_features = get_pos_features(list(filter(lambda x:x.isupper(),temp)))
	features.append(len(list(filter(lambda x:x.isupper(),temp))))
	# print features
	features.extend(pos_features)
	# print (features)
	return features

# get_feature_1_2("/home/ameesha/Documents/data mining/feature1.2/user0.csv")
# get_emoji_Features("Well i just CANT stop singing/watching/HUMMING #IkVaariAa !! ❤️🎤🎧 Its on loop..WOW What about you? 😜😁")
# get_emoji_Features("ARE YOU KIDDING ME?")

def writeFile(folder, csvfile):
	f5 = csv.writer(csvfile,delimiter=",")
	for f in sorted(os.listdir(folder)):
		inputFile = open(os.path.join(folder,f),"r")
		# print (inputFile)
		reader = list(csv.reader(inputFile))
		tweet = reader[1][2]
		tweet =tweet.strip()
		featurelist=get_emoji_Features(tweet)
		f5.writerow(featurelist)
		inputFile.close()		


pwd = os.getcwd()
norm = pwd + "/normal_with_past"
sarc = pwd + "/sarcastic_with_past"
csvfile = open("feature1_2.csv","w")
writeFile(norm,csvfile)
writeFile(sarc,csvfile)
csvfile.close()
