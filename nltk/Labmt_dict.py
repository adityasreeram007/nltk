import re
myfile=open("LabMT dict.txt","r")
res=[]
happy_rank={}
happy_avg={}
happy_SD={}
google_rank={}
twitter={}
lyrics={}
for wrd in myfile:
    res.append(re.split("\t",wrd))
res.pop(0)
print(res)
regex=re.compile(r'-?[0-9]+')
for l in res:
    h_r=list(int(float(d)) for d in regex.findall(l[1]))
    h_r=h_r.pop(0)
    happy_rank[l[0]]=h_r
    h_a = list(int(float(d)) for d in regex.findall(l[2]))
    h_a=h_a.pop(0)
    happy_avg[l[0]]=h_a
    h_s = list(int(float(d)) for d in regex.findall(l[3]))
    h_s=h_s.pop(0)
    happy_SD[l[0]]=h_s
    g_r = list(int(float(d)) for d in regex.findall(l[5]))
    g_r=g_r.pop(0)
    google_rank[l[0]]=g_r
    tw = list(int(float(d)) for d in regex.findall(l[4]))
    tw=tw.pop(0)
    twitter[l[0]]=tw
    ly = list(int(float(d)) for d in regex.findall(l[6]))
    ly=ly.pop(0)
    lyrics[l[0]]=ly
print(happy_rank)
print(happy_avg)
print(happy_SD)
print(twitter)
print(google_rank)
print(lyrics)
