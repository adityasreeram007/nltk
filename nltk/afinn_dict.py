import os
import re
myfile=open("AFINN dictionary.txt","r")
res=[]
dict1={}
for wrd in myfile:
    res.append(re.split("\t",wrd))
regex=re.compile(r'-?[0-9]+')
print(res)
for l in res:
    v=list(int(d) for d in regex.findall(l[1]))
    v=v.pop(0)
    dict1[l[0]]=v
pos={}
less_pos={}
neutral={}
neg={}
les_neg={}
print(dict1)
for rank in dict1:
    if (dict1[rank]>=3):
        pos[rank]=dict1[rank]
    elif (dict1[rank]<3 and dict1[rank]>=1):
        less_pos[rank]=dict1[rank]
    elif (dict1[rank]==0):
        neutral[rank]=dict1[rank]
    elif (dict1[rank]<=0 and dict1[rank]>=-2):
        les_neg[rank]=dict1[rank]
    else:
        neg[rank]=dict1[rank]
print("Very Good")
print(pos)
print("Good")
print(less_pos)
print("Neutral")
print(neutral)
print("Bad")
print(les_neg)
print("very Bad")
print(neg)