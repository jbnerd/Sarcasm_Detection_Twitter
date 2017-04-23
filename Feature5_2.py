import os
import csv

def hasrepeatchar(word, sentidict):
	retval = 0							# 0 = no repeated char, 1 = repeated char, not sentiment loaded, 2 = both
	index = 0
	while index < len(word) - 2:
		count = 0		
		if (word[index] == word[index + 1] == word[index + 2]):
			if retval == 0:
				retval = 1
			while index + count < len(word):
				if word[index + count] == word[index]:
					count += 1
				else:
					break
			word = word[:index] + word[index + count - 2:]		# trimming the repeated char substring to length of 2
			if word in sentidict:
				retval = 2
				break
			#print(word)
			word = word[:index] + word[index + 1:]				# trimming the repeated char substring to length of 1
			if word in sentidict:
				retval = 2
				break
			#print(word)
		index += 1
	return retval
	

def writeFile(folder,csvfile,sentidict):
	# checking presence of repeated characters
	f5 = csv.writer(csvfile,delimiter=",")
	for f in sorted(os.listdir(folder)):
		repeatcharwordpresent = 0
		repeatcharsentiwordpresent = 0
		inputFile = open(os.path.join(folder,f),"r")
		reader = list(csv.reader(inputFile))
		tweet = reader[1][2]
		words = tweet.strip().split(" ")
		for li1 in range(len(words)):
			retval = hasrepeatchar(words[li1], sentidict)
			if retval == 2:
				repeatcharwordpresent = 1
				repeatcharsentiwordpresent = 1
				break
			elif retval == 1:
					repeatcharwordpresent = 1
		featurelist = [repeatcharwordpresent,repeatcharsentiwordpresent]
		f5.writerow(featurelist)
		inputFile.close()


def main():
	pwd = os.getcwd()
	filename = pwd + "/senti.txt"
	file_obj = open(filename, "r")
	lines = file_obj.readlines()

	# Populate sentidict to contain the all sentiment loaded words (i.e. words with sentiment value >= 2 or <= -2)
	sentidict = []

	for li1 in range(len(lines)):
		if abs(int((lines[li1].strip().split("\t"))[1])) >= 2:
			sentidict.append((lines[li1].strip().split("\t"))[0])


	norm = pwd + "/normal_with_past_PP"
	sarc = pwd + "/sarcastic_with_past"
	csvfile = open("feature5_2.csv","w")
	writeFile(norm,csvfile,sentidict)
	writeFile(sarc,csvfile,sentidict)
	csvfile.close()



if __name__ == "__main__":
	main()
