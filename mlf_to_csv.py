# mlf_to_csv.py
# grabs mlf from the data/mlfs directory and creates a csv in 
# in the data/csvs directory with the date

from subprocess import call
import csv

natives = open('data/FWOA.txt').readlines()
natives = [x.strip() for x in natives]
foreigners = open('data/FWA.txt').readlines()
foreigners = [x.strip() for x in foreigners]

NUM_TRANSCRIPTS = 4

for i in range(NUM_TRANSCRIPTS):
	csv_filename = 'data/csvs/transcript_%d.csv' % i+1
	csv_file = open(csv_filename, 'wb')
	csv_writer = csv.writer(csv_file, delimeter = ',')

	for native in natives:
		filename = 'data/mlfs/native/%s_%d.mlf' % (native, i+1)
		mlf_data = open(filename).readlines()

		for 





