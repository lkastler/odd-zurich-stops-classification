# odd-zurich-stops-classification - classifying public transport stops by surrounding.

[Open Data Day Zurich Hackathon 2017](http://zurich-r-user-group.github.io/hackathon.html)

The goal was to classify public transport stops by their surrounding landmarks, like universities or coworking_spaces, extracted from [OpenStreetMap](http://openstreetmap.org).

# Usage
- The tool chain uses make and python 3.6.
- create a ``data`` folder or change the Makefile variable.
- add the ``data-examples/haltepunkt.csv`` file to ``data``.
- run ``make``.

This will:
- extract all active stop point coordinates
- retrieve OpenStreetMaps landmarks with around these coordinates.
- eliminates duplicates.
- classifies the landmarks with the given classifiers.

# Limitations
- the proximity search of Overpass will most likely kick you out, because of too many requests. Solution for this is limiting the stop point coordinates.
