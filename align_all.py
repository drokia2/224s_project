#align_all.py  
#runs align all all of the sound file with there corresponding transcripts
#and dumps the files in data/mlfs/ directory
#The mlf files have the same naming scheme as the soudn files i.e. 'adriana_1.mlf'
#
#usage:
#   python align_all.py                 # to run alignment on all students
#   python align_all.py name+           #NOT IMPLEMENTED YET# to run alignment on one or more specific names listed; 
                                        # names are delimeted by spaces i.e. python align_all.py adriana sam ankit

# you might have to do sudo right before running this
# make sure there is a file called "TEXT_GRID.TextGrid" in the current directory

from subprocess import call

natives = open('data/FWOA.txt').readlines()
natives = [x.strip() for x in natives]
foreigners = open('data/FWA.txt').readlines()
foreigners = [x.strip() for x in foreigners]
print natives
print foreigners

NUM_TRANSCRIPTS = 4
TRANSCRIPTS = ['transcript_1.txt', 'transcript_2.txt', 'transcript_3.txt', 'transcript_4.txt']
TEXT_GRID = "TEXT_GRID.TextGrid"

for native in natives:
  for i in range(NUM_TRANSCRIPTS):
    transcript = './data/transcripts/%s' % TRANSCRIPTS[i]
    wav_file = './data/sounds/%s_%d.wav' % (native, i+1)
    failure = call(['python', 'align.py', wav_file, transcript, TEXT_GRID ])
    if (failure):
      print "ERROR WITH ", native , i+1
      print "\n"
    else:
      mlfs_paths = 'data/mlfs/native/%s_%d.mlf' % (native, i+1)
      copy_failure = call(['cp', 'tmp/aligned.mlf', mlfs_paths])
      if (copy_failure):
        print "shit the copy didnt work"

for foreigner in foreigners:
  for i in range(NUM_TRANSCRIPTS):
    transcript = './data/transcripts/%s' % TRANSCRIPTS[i]
    wav_file = './data/sounds/%s_%d.wav' % (foreigner, i+1)
    failure = call(['python', 'align.py', wav_file, transcript, TEXT_GRID ])
    if (failure):
      print "ERROR WITH ", foreigner , i+1
      print "\n"
    else:
      mlfs_paths = 'data/mlfs/foreign/%s_%d.mlf' % (foreigner, i+1)
      copy_failure = call(['cp', 'tmp/aligned.mlf', mlfs_paths])
      if (copy_failure):
        print "shit the copy didnt work"
    
