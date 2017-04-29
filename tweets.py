import tweepy
import csv

CONSUMER_KEY='e5nIEhfbX0euH7yUFMFHQVh5G'
CONSUMER_SECRET='fOiXTUtspsE1rVAY4rNH8ONBSms0Z4iIkd5UxYyLMHt3E3TWVf'
ACESS_TOKEN='814458916570415104-Iu8BZ6PxPHafMRrPooq7WVTxwwmqAQt'
ACESS_TOKEN_SECRET='ItKv6fFT3vv31yoo5396JPKFynAGdEjDaGc5pjZUNyq76'


auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACESS_TOKEN, ACESS_TOKEN_SECRET)
api=tweepy.API(auth)

file=open('sarcasm_detection_dataset.csv')
file1=open('outfile.csv')
reader=csv.reader(file)
writer=csv.writer(file1)
k=0
for line in reader:
	k+=1
	tweet=api.get_status('385621497064083457')
	writer.write([tweet.text,tweet.created_at,tweet.author._json['screen_name']])
