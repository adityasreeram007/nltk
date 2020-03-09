import os
import re
pos_file=open("positive sentinet.txt","r")
neg_file=open("negative sentinet.txt","r")
pl=[]
nl=[]
for (wrd1,wrd2) in zip(pos_file,neg_file):
    wrd1=wrd1.strip("\n")
    wrd2=wrd2.strip("\n")
    pl.append(wrd1)
    nl.append(wrd2)
print(pl)
print(nl)