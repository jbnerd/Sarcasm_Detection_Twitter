from textblob import TextBlob 

from PreProc import preprocess
import csv
# path_normal = os.path.abspath("/home/jayati/Documents/sarcasmdet/Python Code") + "/normal_with_past"
# fileListNormal  = os.listdir(path_normal)
def getSentiStrength(w):
	sentidict = {}
	with open('senti.txt','r') as file2:
		for line in file2:
			temp = line.split()
			sentidict[temp[0]]=float(temp[1])


	if w in sentidict:
		return sentidict[w]
	else:
		for key,value in sentidict.iteritems():
			if key.startswith(w):
				return value
		#print w
		return 0 


#accepts a file and returns a list of 10 features
def get_feature_1_2(filename):
# filename = "/home/ameesha/Documents/data mining/Sarcasm-Detection-/normal_with_past/user1.csv"
	with open(filename) as tweet_file:
		file_reader = csv.DictReader(tweet_file)
		num=0
		pos_pos=0
		pos_neg=0
		pos_neu=0
		neu_neg=0
		neu_pos=0
		neu_neu=0
		neg_pos=0
		neg_neg=0
		neg_neu=0
		f=[None]*10
		for row in file_reader:
			print "*******************************"
			# print num
			num=num+1
			# print row['tweet']
			#preprocessing of tweet to get a list of words (stemming required)
			words = preprocess(row['tweet'])

			# print words
			senti_score=0
			prev_score=-10
			for w in words:
				# print w + str(getSentiStrength(w))
				senti_score=senti_score+getSentiStrength(w)
			print senti_score
			
			if num==1:
				prev_score=senti_score
			else:
				print num, prev_score, senti_score
				if prev_score<0 and senti_score<0:
					neg_neg=neg_neg+1
					if num ==2:
						i=8
				elif prev_score<0 and senti_score>0:
					pos_neg=pos_neg+1
					if num ==2:
						i=2
				elif prev_score<0 and senti_score==0:
					neu_neg=neu_neg+1
					if num ==2:
						i=4
				elif prev_score>0 and senti_score<0:
					neg_pos=neg_pos+1
					if num ==2:
						i=7
				elif prev_score>0 and senti_score>0:
					pos_pos=pos_pos+1
					if num ==2:
						i=1
				elif prev_score>0 and senti_score==0:
					neu_pos=neu_pos+1
					if num ==2:
						i=5
				elif prev_score==0 and senti_score<0:
					neg_neu=neg_neu+1
					if num ==2:
						i=9
				elif prev_score==0 and senti_score>0:
					pos_neu=pos_neu+1
					if num ==2:
						i=3
				elif prev_score==0 and senti_score==0:
					neu_neu=neu_neu+1
					if num ==2:
						i=6							
				prev_score=senti_score
		print pos_pos
		print pos_neg
		print pos_neu
		print neu_neg
		print neu_pos
		print neu_neu
		print neg_pos
		print neg_neg
		print neg_neu
		total=pos_neu+pos_neg+pos_pos+neg_neu+neg_neg+neg_pos+neu_neu+neu_pos+neu_neg
		f[1]= float(pos_pos)/total
		f[2]= float(pos_neg)/total
		f[3]= float(pos_neu)/total
		f[4]= float(neu_neg)/total
		f[5]= float(neu_pos)/total
		f[6]= float(neu_neu)/total
		f[7]= float(neg_pos)/total
		f[8]= float(neg_neg)/total
		f[9]= float(neg_neu)/total
		f[0]= f[i]
		print f
		return f

