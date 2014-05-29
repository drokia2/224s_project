import numpy as np
from collections import defaultdict
f = open('transcript_1.csv','r')

transcript_1_words = set(['ONE','FOUR','ONE','FIVE','TWO','SIX','FIVE','FIVE','EIGHT','SEVEN','THREE','TWO','THREE','EIGHT','SIX','TWO','SIX','FOUR','THREE'])
mapping = defaultdict(list)


for line in f:
	splits=line.split(',')
	if splits[0] in transcript_1_words:
		i=1
		while i<len(splits)-1:
			mapping[splits[0]+'_'+splits[i]].append(float(splits[i+1]))
			i+=2


# 
avgs = {x:np.average(mapping[x]) for x in mapping}
stdvs = {x:np.std(mapping[x]) for x in mapping}


