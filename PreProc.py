import re
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
import csv
import os


def main():
    pwd = os.getcwd();
    norm_in = pwd + "/normal_with_past"
    norm_out = pwd + "/normal_with_past_PP"
    sarc_in = pwd + "/sarcastic_with_past"
    sarc_out = pwd + "/sarcastic_with_past_PP"
    stop = set(stopwords.words('english'))

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

    # inputFile = open("test_data.csv", "r")
    # outputFile = open("processed.csv", "w")
    # reader = csv.reader(inputFile)
    # writer = csv.writer(outputFile)
    # for row in reader:
    #     row[2] = preprocess(row[2])
    #     # print row[2]
    #     writer.writerow(row) 

def remove_punctuations(text_string):
        #defining a list of special characters to be used for text cleaning
        special_characters = [",",".","'",";","\n", "?", "!", ":", ")", "(", "@", "*", "{", "}", "#",":", "_", "+", "`", "~", "$", "%", "^", "&", ""] 
        cleaned_string = str(text_string)
        # removing stop words
        for ch in special_characters:
            cleaned_string = cleaned_string.replace(ch, "")
            cleaned_string = cleaned_string.lower()
        return cleaned_string

def remove_stop_words(document):
        pwd = os.getcwd()
        words_file = pwd + "/stop_words.txt"
        stop_word_list = []
        stop_word_list = [word for line in open(words_file, 'r') for word in line.split(",")]
        cleaned_doc = []
        for term in document.split(" "):
            # print term
            term = remove_punctuations(term)
            if term not in stop_word_list:
                cleaned_doc.append(term)
        return cleaned_doc   

def preprocess(tweet):
    tweet = tweet.replace("#sarcasm","")                                                    #Removes the sarcasm hashtag
    tweet = tweet.replace("#sarcastic","")
    tweet = tweet.replace("#not","")
    tweet = re.sub(r"(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)", "", tweet) 
    tweet = re.sub(r'(https?|ftp)://[^\s/$.?#].[^\s]*', '', tweet, flags=re.MULTILINE)      #Removes URL                                                   
    tweet = remove_stop_words(tweet)                                   
    tweet = " ".join(tweet)
    return tweet


if __name__=="__main__":
    main()

