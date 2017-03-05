DATA=data
STOPS=${DATA}/haltepunkt.csv
COORDINATES=${DATA}/haltestellen_coordinates.csv
OVERPASS=${DATA}/overpass.csv
OVER_NO_DUPS=${DATA}/overpass.csv
OVER_CLASS=${DATA}/overpass_classes.csv

PYTHON=python3

@PHONY: classify
classify: ${OVER_NO_DUPS}
	${PYTHON} classify.py

${OVER_NO_DUPS}: ${OVERPASS}
	cat ${OVERPASS} | sort | uniq > ${OVER_NO_DUPS}
${OVERPASS}: ${COORDINATES}
	${PYTHON} overpass_api.py

${COORDINATES}: ${STOPS}
	${PYTHON} stops_coordinates.py

