#=============================================================================================

import re
import matplotlib.pyplot as plt
import numpy as np
import array as arr
import pandas as pd
import json 
import os
import seaborn as sns
import nltk
from collections import Counter
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

#=============================================================================================

ps = PorterStemmer()

#=============================================================================================

directory = '/Users/anilaswani/Desktop/Probabilistic information retrieval/DocumentCorpus'
obj = FrequencyCount()
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        obj.count_word(f)

#=============================================================================================

class FrequencyCount:

#=============================================================================================

    def count_word(self,file_name):
        wordSet={""}
        wordCountDict = {"":0}
        with open(file_name,encoding='utf8') as file:
            words = file.read().split(" ")
            for w in words:
                w=w.replace('\n',' ')
                temp = w.split(" ")
                for t in temp:
                    wordSet.add(t);
            file = open(file_name, "r")
            data = file.read()
            for word in wordSet:
                wordCountDict[word] = data.count(word)
            
            wordCountDict = (sorted(wordCountDict.items(), key=lambda kv: (kv[1], kv[0])))
        
        json_object = json.dumps(wordCountDict, indent = 4)
        location = "/Users/anilaswani/Desktop/Probabilistic information retrieval/WordCountJson/"+os.path.basename(file_name).split('.txt')[0]
        with open(location, "w") as outfile:
            json.dump(wordCountDict, outfile)
        return
