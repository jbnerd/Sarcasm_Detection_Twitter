from nltk.tag import pos_tag
import nltk
import os,csv

def structuralVariations(tweet):	
	words = nltk.tokenize.word_tokenize(tweet)
	tagged_sent = pos_tag(words)
	count = 0
	pronounfeatures = [0,0,0,0]
	intensifierfeatures = [0,0]
	f5 = []
	#lexical density to include nouns, verbs, adjectives, adverbs)
	for li1 in range(len(tagged_sent)):
		lexicallist = ['NN','NNS','NNP','NNPS','VB','VBD','VBG','VBN','VBP','VBZ','RB','RBR','RBS','WRB','JJ','JJR','JJS']

		if (tagged_sent[li1][1] in lexicallist):
			count += 1
		elif tagged_sent[li1][1] == 'PRP':
			pronounfeatures[0] += 1
		elif tagged_sent[li1][1] == 'PRP$':
			pronounfeatures[1] += 1
		elif tagged_sent[li1][1] == 'WP':
			pronounfeatures[2] += 1
		elif tagged_sent[li1][1] == 'WP$':
			pronounfeatures[3] += 1
		elif tagged_sent[li1][0] == "so":
			intensifierfeatures[0] += 1
		elif tagged_sent[li1][0] == 'very':
			intensifierfeatures[1] += 1
	lexicaldensity = count / len(words)
	f5 += pronounfeatures
	f5 += intensifierfeatures
	f5.append(lexicaldensity)
	return f5

def writeFile(folder,csvfile):
	f5 = csv.writer(csvfile,delimiter=",")
	for f in sorted(os.listdir(folder)):
		inputFile = open(os.path.join(folder,f),"r")
		reader= list(csv.reader(inputFile))
		tweet = reader[1][2]
		f5.writerow(structuralVariations(tweet))
		inputFile.close()



def main():
    pwd = os.getcwd()
    norm = pwd + "/normal_with_past_PP"
    sarc = pwd + "/sarcastic_with_past_PP"
    csvfile = open("feature5_extra.csv","w")
    writeFile(norm,csvfile)
    writeFile(sarc,csvfile)
    csvfile.close()


if __name__=="__main__":
    main()