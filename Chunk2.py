from Chunk1 import NL
from nltk import pos_tag, ne_chunk
from nltk.corpus import wordnet as wn, stopwords
import nltk
import re
from collections import Counter

date = r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d.*\d\s*$"
pattern=re.compile(date)

filename = 'Big_Four.txt'

with open(filename) as f:
    data = f.read(1024*1024*1)

bodies=[]
bodies.append('')
i=0

for line in data.split("\n"):
    line+="\n"
    if pattern.search(line):
        i+=1
        bodies.append('')
    else:
        bodies[i]+=line
 
clean_bodies=[]
j=0
for body in bodies:
    clean_bodies.append((re.findall(r'\b([a-zA-Z]+)\b',bodies[j])))
    j += 1
    

cleaner_bodies = []

for bod in clean_bodies:
    inner_body = []
    for word in bod:
        if word in stopwords.words('english'):
            pass
        elif wn.morphy(word) is None:
            inner_body.append(word)
        else:
            inner_body.append(str(wn.morphy(word)))
    cleaner_bodies.append(inner_body)
        
        
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print cleaner_bodies[1]

#community_dictlist = []
#for article in cleaner_bodies:
#   community_dict = {}
#    for word in article:
        
        
        
#location_array=[]
#p=0
#for locations in bodies:
#    location_array.append(NL(bodies[p]).pnoun())
#    p+=1
#print data
#location_array[2]