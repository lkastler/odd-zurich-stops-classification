import csv

classes = {'kindergarden': 1, 'university': 1, 'doctors':2, 'dentist':2, 'coworking_space': 3, 'public_building':3}


with open('data/overpass_no_dups.csv') as csvfile:
	reader = csv.reader(csvfile)

	with open('data/overpass_classes.csv', 'w+') as output:

		writer = csv.writer(output)
		for row in reader:
			if row[2] in classes.keys():
				writer.writerow([row[0], row[1], classes.get(row[2])])