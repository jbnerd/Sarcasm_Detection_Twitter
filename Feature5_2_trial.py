
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
	

# Read from senti.txt
file_obj = open("senti.txt", "r")
lines = file_obj.readlines()

# Populate sentidict to contain the all sentiment loaded words (i.e. words with sentiment value >= 2 or <= -2)
sentidict = []

for li1 in range(len(lines)):
	if abs(int((lines[li1].strip().split("\t"))[1])) >= 2:
		sentidict.append((lines[li1].strip().split("\t"))[0])

# checking presence of repeated characters
repeatcharwordpresent = False
repeatcharsentiwordpresent = False

tweet = input("")                            #################
words = tweet.strip().split(" ")

for li1 in range(len(words)):
	retval = hasrepeatchar(words[li1], sentidict)
	if retval == 2:
		repeatcharwordpresent = True
		repeatcharsentiwordpresent = True
		break
	elif retval == 1:
		repeatcharwordpresent = True

		
# to append to feature list

print(repeatcharwordpresent, "\t", repeatcharsentiwordpresent)
featurelist = [repeatcharwordpresent,repeatcharsentiwordpresent]  ####################################











