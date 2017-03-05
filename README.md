# odd-zurich-stops-classification - classifying public transport stops by surrounding.

[Open Data Day Zurich Hackathon 2017](http://zurich-r-user-group.github.io/hackathon.html)

The goal was to classify public transport stops by their surrounding landmarks, like universities or coworking_spaces, extracted from [OpenStreetMap](http://openstreetmap.org).

# usage
- The tool chain uses make and python 3.6.
- create a ``data`` folder or change the Makefile variable.
- add the ``data-examples/haltepunkt.csv`` file to ``data``.
- run ``make``.

The Make script will
- extract all active stop point coordinates
- retrieve OpenStreetMaps landmarks with around these coordinates.
- eliminates duplicates.
- classifies the landmarks with the given classifiers.
