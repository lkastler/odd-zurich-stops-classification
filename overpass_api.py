import overpy
import pystache
import csv
from decimal import *

api = overpy.Overpass()
template = '<osm-script output="json">' \
           '<bbox-query s="{{s}}" n="{{n}}" w="{{w}}" e="{{e}}"/>' \
           '<around radius="{{r}}"/>' \
           '<print mode="body"/></osm-script>'
space = Decimal(0.0001)


def get_data(lat, lon, r):
	"""
	receives objects with amenity tag from Overpass API at a given point.
	:param lat: latitude
	:param lon: longitude
	:param r: range to query for
	:return: yields objects with amenity tag in the given proximity.
	"""
	getcontext().prec = 6
	ds = Decimal(str(lat))
	dw = Decimal(str(lon))
	query = pystache.render(template, {'s': ds - space, 'n': ds + space, 'w': dw - space, 'e': dw + space, 'r': r})
	result = api.query(query)

	for x in result.nodes:
		if x.tags is not None:
			if 'amenity' in x.tags:
				yield [x.lat, x.lon, x.tags.get('amenity')]

with open('data/haltestellen_coordinates.csv') as coordinates:
	reader = csv.reader(coordinates)
	with open('data/overpass.csv', 'w') as out:
		writer = csv.writer(out)

		for row in reader:
			for x in get_data(row[0], row[1], 500):
				writer.writerow(x)