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

def get_community(theWord):
	wrd = ""
	if wn.morphy(theWord) is None:
		wrd = theWord
	else:
		wrd = str(wn.morphy(theWord))
		
	try:
		return str(((wn.synsets(wrd)[0]).hypernyms()[0]).lemma_names()[0])
	except IndexError:
		return wrd

for line in data.split("\n"):
    line+="\n"
    if pattern.search(line):
        i+=1
        bodies.append('')
    else:
        bodies[i]+=line
		
#print bodies[1]
location_array=[]
p=0
for locations in bodies:
    location_array.append(NL(bodies[p]).pnoun() + NL(bodies[p]).noun())
    p+=1
#print data

print location_array[1]

community_dictlist = []
for article in location_array:
	community_dict = {}
	for wordfreq in article:
		if get_community(wordfreq[0]) in community_dict:
			community_dict[get_community(wordfreq[0])] += wordfreq[1]
		else:
			community_dict[get_community(wordfreq[0])] = wordfreq[1]
	community_dictlist.append(community_dict)
	
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print community_dictlist[1]

