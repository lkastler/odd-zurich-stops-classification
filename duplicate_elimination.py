import csv

dups = dict()

with open('data/overpass.csv') as csvfile:
	reader = csv.reader(csvfile)

	for row in reader:
		hash = str(row[0]) + '_' + str(row[1])
		if hash not in dups:
			dups[hash] = row

with open('data/overpass_no_dups.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)

	for h,x in dups.items():
		writer.writerow(x)