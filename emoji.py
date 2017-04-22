# -*- coding: utf-8 -*-

import re

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
	print features

	temp = re.findall(r"[\w']+", raw_tweet)
	features.append(len(filter(lambda x:x.isupper(),temp)))
	print features
	return features

# get_feature_1_2("/home/ameesha/Documents/data mining/feature1.2/user0.csv")
get_emoji_Features("Well i just cant stop singing/watching/humming #IkVaariAa !! ❤️🎤🎧 Its on loop..WOW What about you? 😜😁")
