import csv
from decimal import *

with open('data/haltepunkt.csv') as csv_input:
	reader = csv.DictReader(csv_input)

	with open('data/haltestellen_coordinates.csv', 'w+') as csv_output:
		writer = csv.writer(csv_output)

		for row in reader:
			if row['GPS_Latitude'] and row['GPS_Longitude'] and row['halt_punkt_ist_aktiv'] == 'True':

				lat = Decimal(row['GPS_Latitude'].replace('"', '').replace(',','.'))
				lon = Decimal(row['GPS_Longitude'].replace('"', '').replace(',','.'))

				print(lat, lon)

				if lon >= 8.5272 and lon <= 8.5490 and lat >= 47.3726  and lat <= 47.3806:
					writer.writerow([lat, lon])