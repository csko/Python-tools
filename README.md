Random Python tools.
====================

kml.py
------

Provides a fuinction which extracts Track information from KML files. Hasn't been tested on a variety of KML files.

Requirements:

*  [lxml](http://lxml.de/)

dtw.py
------

A Python implementation of the multi-dimensional DTW algorithm with Manhattan distance. It's very slow.
Commented is a 1D DTW reference for the mlpy implementation, which is faster, but does not work on coordinates.

Usage:

* ``python dtw.py``

    Grabs the KML files from ``tracks/`` and displays the distance matrix for each pair of tracks.

Optional requirements:

* [mlpy](http://mlpy.sourceforge.net/)

pdfannot.py
-----------

Extracts basic annotation information from a PDF file. Uses the python poppler wrapper.
Highly extendable :).

Requirements:

*  [poppler-python](https://launchpad.net/poppler-python) (0.12+, )

Usage:

``python pdfannot.py ABSOLUTE_PATH``

