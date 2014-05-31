import numpy as np
from collections import defaultdict
from matplotlib import pylab


person = 'elvis'
transcipt_number = 4
threshold = 1

transcript_1_words = set(['ONE','FOUR','ONE','FIVE','TWO','SIX','FIVE','FIVE','EIGHT','SEVEN','THREE','TWO','THREE','EIGHT','SIX','TWO','SIX','FOUR','THREE'])
transcript_2_words = set(['SIX','SEVEN','TWENTY','EIGHTY','TWO','ONE','HUNDRED','ONE','THIRTY','TWELVE','FIFTY','SIXTY','FOUR','NINETY','NINETY','NINE','THIRTEEN','FIVE'])
transcript_3_words = set(['INSPIRATION','IS','A','STIMULATING','FEELING','THAT','WE','SEEK','TO','MOTIVATE','US','TO','CONTINUE','PRESSING','FORWARD','THROUGH','HARDSHIPS','AND','TO','FIND','MEANING','AMIDST','CHAOS'])
transcript_4_words = set(['ACROSS','COMFORTABLE','PARADIGM','SPURIOUS','PICTURE','INFAMOUS','AWRY','BUSINESS'])
transcripts = [transcript_1_words,transcript_2_words,transcript_3_words,transcript_4_words]

filename = 'transcript_'+str(transcipt_number)+'.csv'
print filename

f = open(filename,'r')

mapping = defaultdict(list)


for line in f:
	splits=line.split(',')
	if splits[0] in transcripts[transcipt_number-1]:
		print 'hi'
		i=1
		while i<len(splits)-1:
			mapping[splits[0]+'_'+splits[i]].append(float(splits[i+1]))
			i+=2

# 
avgs = {x:np.average(mapping[x]) for x in mapping}
stdvs = {x:np.std(mapping[x]) for x in mapping}


print avgs

print stdvs


filename = open('transcript_foreigner_'+str(transcipt_number)+'.csv', 'r')

found_person = False

deviations = []
counter = 0
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

	if splits[0] in transcripts[transcipt_number-1]:
		i=1
		while i<len(splits)-1:
			diff = avgs[splits[0]+'_'+splits[i]]-float(splits[i+1]) 
			stddevs = diff/stdvs[splits[0]+'_'+splits[i]]
			#print 'diff:', diff
			#print 'stddevs',stddevs
			deviations.append(max(stddevs,0))
			if stddevs > threshold:
				print "Mispronunciation in word ",splits[0],' at phone ', splits[i], '.  ', stddevs,' std devs below mean.'
				pylab.annotate(splits[0]+'_'+splits[i], xy=(counter,stddevs), xytext=(counter,stddevs))
				print i, stddevs
			i+=2
			counter+=1



print deviations
pylab.ylabel("number of std dev below mean");
pylab.xlabel("indicies of phones in transcript")
pylab.title(person + " speaks transcript "+str(transcipt_number))
pylab.plot(deviations)
pylab.show()

