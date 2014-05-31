# mlf_to_csv.py
# grabs mlf from the data/mlfs directory and creates a csv in 
# in the data/csvs directory with the date

from subprocess import call
import csv
import re


natives = open('data/FWOA.txt').readlines()
natives = [x.strip() for x in natives]
foreigners = open('data/FWA.txt').readlines()
foreigners = [x.strip() for x in foreigners]

NUM_TRANSCRIPTS = 4

for i in range(NUM_TRANSCRIPTS):

	csv_filename = 'data/csvs/transcript_%d.csv' % (i+1)
	csv_file = open(csv_filename, 'wb')
	csv_writer = csv.writer(csv_file,delimiter = ',')

	for native in natives:
		csv_writer.writerow('')

		row_string = ['person', '%s' % native]

		filename = 'data/mlfs/native/%s_%d.mlf' % (native, i+1)
		mlf_data = open(filename).readlines()

		pattern = re.compile('\d*\s\d*\s(.*)\s(\d*\.\d*)\s?(\w*)')

		for row in mlf_data:
			m = pattern.match(row)
			if m:
				if m.group(3):
					csv_writer.writerow(row_string)
					row_string = []
					row_string.append(m.group(3))

				row_string.append(m.group(1))
				row_string.append(m.group(2))

		csv_writer.writerow(row_string)


for i in range(NUM_TRANSCRIPTS):

	csv_filename = 'data/csvs/transcript_foreigner_%d.csv' % (i+1)
	csv_file = open(csv_filename, 'wb')
	csv_writer = csv.writer(csv_file,delimiter = ',')

	for foreigner in foreigners:
		csv_writer.writerow('')

		row_string = ['person', '%s' % foreigner]

		filename = 'data/mlfs/foreign/%s_%d.mlf' % (foreigner, i+1)
		try:
			mlf_data = open(filename).readlines()
		except:
			print "missing filename: ", filename
			continue

		pattern = re.compile('\d*\s\d*\s(.*)\s(\d*\.\d*)\s?(\w*)')

		for row in mlf_data:
			m = pattern.match(row)
			if m:
				if m.group(3):
					csv_writer.writerow(row_string)
					row_string = []
					row_string.append(m.group(3))

				row_string.append(m.group(1))
				row_string.append(m.group(2))

		csv_writer.writerow(row_string)








