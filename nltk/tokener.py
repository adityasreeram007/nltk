import nltk
from textblob import TextBlob
# import csv
import pandas as pd

# from openpyxl import load_workbook

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

data = pd.read_csv("message.csv", encoding="latin1")
listdata = list(data["messages"])
stop_words = set(stopwords.words("english"))
# stop_words = set(stopwords.words('english'))
apps = list(data["App"])
appset = set(apps)
mapapptomessage = dict({x: [] for x in appset})
mapapptosentence=dict({x: [] for x in appset})
sentimenet=dict({x:None for x in appset})
for i in range(len(apps)):
    mapapptosentence[apps[i]].append(listdata[i])

count = 0
for i in listdata:
    word_tokens = word_tokenize(i)
    # print(word_tokens)
    count += 1
    # print(count)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    try:
        mapapptomessage[apps[count]].append(word_tokens)
    except:
        break

# print(word_tokens)
# print(filtered_sentence)
#print(mapapptomessage["1None Best Foods for You"])
#print(mapapptosentence)
for i in appset:
    summ=0
    for x in mapapptosentence[i]:
        d=TextBlob(x)
        summ+=d.sentiment.polarity
    avg=summ/len(mapapptosentence[i])
    sentimenet[i]=avg
#print(sentimenet)
for i in sentimenet:
    if(sentimenet[i]>0.03):
        print(i+"\t\t\t"+"fraud")
    else:
        print(i+" \t\t\t"+"Genuine")
