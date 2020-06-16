import csv
import sys
with open(sys.argv[1]) as csvfile:
	reader = csv.DictReader(csvfile)
	with open('output.txt','w') as finout:
		for row in reader:
			finout.write(row['Email']+'\n')