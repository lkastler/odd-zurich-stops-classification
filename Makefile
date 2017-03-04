STOPS=data/haltepunkt.csv
COORDINATES=data/haltestellen_coordinates.csv
OVERPASS=data/overpass.csv
OVER_NO_DUPS=data/overpass.csv
OVER_CLASS=data/overpass_classes.csv

PYTHON=python3

@PHONY: classify
classify: ${OVER_NO_DUPS}
	${PYTHON} classify.py

${OVER_NO_DUPS}: ${OVERPASS}
	${PYTHON} duplicate_elimination.py
${OVERPASS}: ${COORDINATES}
	${PYTHON} overpass_api.py

${COORDINATES}: ${STOPS}
	${PYTHON} stops_coordinates.py

