#!/usr/bin/env python
# coding: utf-8

# In[32]:


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


# In[67]:


class contigencyTable:
    def checkForTerm(self,file_name,target):
        with open(file_name) as f:
            data = json.loads(f.read())
        for words in data:
            word=words[0]
            if(word==target):
                return True
        return False
        
    def checkForRelevance(self,file_name,target):
        
        freq=0
        f = open(file_name)
        data = json.load(f)
        for words in data:
            if(target==words[0]):
                freq=words[1]
            
        
        if(int((freq*100)/data[0][1])>1):
            return True
        else:
            return False


# In[75]:


directory = '/Users/anilaswani/Desktop/Probabilistic information retrieval/WordCountJson'

docRelevanceValues = {}
obj = contigencyTable()

keywords = input("Enter what you want to search : ")
keywordSet = keywords.split(" ")
for words in keywordSet:
    contigencyTableValues = [0.5,0.5,0.5,0.5]
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            val1=obj.checkForTerm(f,words)
            val2=obj.checkForRelevance(f,words)

            if(val1==True and val2==True):
                contigencyTableValues[0]=contigencyTableValues[0]+1;
            elif(val1==True and val2==False):
                contigencyTableValues[1]=contigencyTableValues[1]+1;
            elif(val1==False and val2==True):
                contigencyTableValues[2]=contigencyTableValues[2]+1;
            else:
                contigencyTableValues[3]=contigencyTableValues[3]+1;
    ct = contigencyTableValues[0]*contigencyTableValues[3]
    ct=ct/contigencyTableValues[1]
    ct=ct/contigencyTableValues[2]
    
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            val1=obj.checkForTerm(f,words)
            if(val1==True):
                docRelevanceValues[f]=docRelevanceValues[f]+ct if f in docRelevanceValues else ct 
    
docRelevanceValues = (sorted(docRelevanceValues.items(), key=lambda kv: (kv[1], kv[0]),reverse=True))
print("")
for docs in docRelevanceValues:
    print(os.path.basename(docs[0]))
    

