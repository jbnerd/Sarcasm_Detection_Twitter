import os,csv

def hashtag(words):
	feature =[] 	
	hashtags_part1 =0 
	hashtags_part2=0
	hashtags_part3 =0	
	for i in range(0,len(words)):
		if(words[i].startswith('#')):
			if(i< len(words)/3):
				hashtags_part1=hashtags_part1+1
			elif(i<( len(words)*2)/3): 
				hashtags_part2=hashtags_part2+1
			else:
				hashtags_part3=hashtags_part3+1 
	feature.append(hashtags_part1)
	feature.append(hashtags_part2)
	feature.append(hashtags_part3)
	return feature


def writeFile(folder,csvfile):
    f5 = csv.writer(csvfile,delimiter=",")
    for f in sorted(os.listdir(folder)):
        inputFile = open(os.path.join(folder,f),"r")
        reader= list(csv.reader(inputFile))
        tweet = reader[1][2]
        f5.writerow(hashtag(tweet.split(" ")))
        inputFile.close()




def main():
    pwd = os.getcwd()
    norm = pwd + "/normal_with_past"
    sarc = pwd + "/sarcastic_with_past"
    csvfile = open("hash5.csv","w")
    writeFile(norm,csvfile)
    writeFile(sarc,csvfile)
    csvfile.close()


if __name__=="__main__":
    main()