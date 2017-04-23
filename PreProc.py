import re
import csv
import os
from ExtraPreProc import remove_punctuations

def main():
    pwd = os.getcwd();
    norm_in = pwd + "/normal_with_past"
    norm_out = pwd + "/normal_with_past_PP"
    sarc_in = pwd + "/sarcastic_with_past"
    sarc_out = pwd + "/sarcastic_with_past_PP"
    
    for f in os.listdir(norm_in):
        inputFile = open(os.path.join(norm_in,f),"r")
        outputFile = open(os.path.join(norm_out,f),"w")
        reader=csv.reader(inputFile)
        writer=csv.writer(outputFile)
        for row in reader:
            row[2]=preprocess(row[2])
            writer.writerow(row)
        inputFile.close()
        outputFile.close()
    for f in os.listdir(sarc_in):
        inputDest = os.path.join(sarc_in,f)
        outputDest = os.path.join(sarc_out,f)
        inputFile = open(inputDest,"r")
        outputFile = open(outputDest,"w")
        reader=csv.reader(inputFile)
        writer=csv.writer(outputFile)
        for row in reader:
            row[2]=preprocess(row[2])
            writer.writerow(row)
        inputFile.close()
        outputFile.close()

def preprocess(tweet):
    tweet = tweet.replace("#sarcasm","")                                                    #Removes the sarcasm hashtag
    tweet = tweet.replace("#sarcastic","")
    tweet = tweet.replace("#not","")
    tweet = re.sub(r"(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)", "", tweet)      #Removes mentions
    tweet = re.sub(r'(https?|ftp)://[^\s/$.?#].[^\s]*', '', tweet, flags=re.MULTILINE)      #Removes URL
    tweet = remove_punctuations(tweet)
    return tweet


if __name__=="__main__":
    main()