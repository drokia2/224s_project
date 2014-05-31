import numpy as np
from collections import defaultdict
from matplotlib import pylab

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


print avgs

print stdvs


filename = open('transcript_foreigner_1.csv', 'r')

found_person = False
person = 'elvis'

deviations = []

for line in filename:
	splits=line.split(',')
	if person in line:
		found_person = True
		continue
	if found_person == False:
		continue
	if splits[0] == 'person':
		found_person = False
		continue

	if splits[0] in transcript_1_words:
		i=1
		while i<len(splits)-1:
			diff = avgs[splits[0]+'_'+splits[i]]-float(splits[i+1]) 
			stddevs = diff/stdvs[splits[0]+'_'+splits[i]]
			#print 'diff:', diff
			#print 'stddevs',stddevs
			deviations.append(max(stddevs,0))
			if stddevs > 1:
				print "error in word ",splits[0],' at phone ', splits[i]
			i+=2



print deviations
pylab.plot(deviations)
pylab.show()

