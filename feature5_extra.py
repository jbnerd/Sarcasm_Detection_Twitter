from nltk.tag import pos_tag
def structuralVariations(tweet):
	print(tweet)
	words = tweet.split(" ")
	print(words)
	tagged_sent = pos_tag(words)
	
	print(tagged_sent)
	print(tagged_sent[0])
	print(tagged_sent[0][0])

	count = 0
	pronounfeatures = [0,0,0,0]
	intensifierfeatures = [0,0]

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

	

	# no. of fps pronouns


string = input("")
structuralVariations(string)