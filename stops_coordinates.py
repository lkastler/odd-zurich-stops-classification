import csv
from decimal import *


def extract_stop_coordinates(row, writer):
	"""
	extracts the stop coordinates from the given row and writes them out iff stop is active.
	:param row: stop point csv file row
	:param writer: csv writer to write results to.
	:return: the stop coordinates from the given row and writes them out iff stop is active.
	"""
	if row['GPS_Latitude'] and row['GPS_Longitude'] and row['halt_punkt_ist_aktiv'] == 'True':
		lat = Decimal(row['GPS_Latitude'].replace('"', '').replace(',', '.'))
		lon = Decimal(row['GPS_Longitude'].replace('"', '').replace(',', '.'))
		writer.writerow([lat, lon])


with open('data/haltepunkt.csv') as csv_input:
	reader = csv.DictReader(csv_input)

	with open('data/haltestellen_coordinates.csv', 'w+') as csv_output:
		writer = csv.writer(csv_output)

		for row in reader:
			extract_stop_coordinates(row, writer)