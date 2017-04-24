# -*- coding: utf-8 -*-
import os,csv,re
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer


def remove_punctuations(text_string):
        #defining a list of special characters to be used for text cleaning
        special_characters = [",",".","'",";","\n", "?", "!", ":", ")", "(", "@", "*", "{", "}", "#",":", "_", "+", "`", "~", "$", "%", "^", "&", "","<",">","=","`","\"","'"] 
        cleaned_string = str(text_string)
        # removing special character
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
            term = remove_punctuations(term)
            if term not in stop_word_list:
                cleaned_doc.append(term)
        return " ".join(cleaned_doc)

def stem(tweet):
    tweet = tweet.split()
    # wnl = WordNetLemmatizer()
    # tweet = [wnl.lemmatize(w) for w in tweet]
    stemmer = SnowballStemmer("english",ignore_stopwords=True)
    tweetr=[]
    for w in tweet:
        try:
          tweetr.append(stemmer.stem(w))  
        except:
          tweetr.append(w)    
    # tweet = [stemmer.stem(w) for w in tweet]
    return " ".join(tweetr)
