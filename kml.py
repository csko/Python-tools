from lxml import objectify
from time import strptime
import sys

def get_tracks(fname):

    with open(fname) as f:
        doc = objectify.parse(f)

    nsmap = doc.getroot().nsmap
    if None in nsmap:
        nsmap['k'] = nsmap[None]
        del nsmap[None]

    tracks = doc.xpath("//gx:Track", namespaces = nsmap)

    track_result = []
    for track in tracks:
        times = track.xpath("./k:when", namespaces = nsmap)
        # TODO: more general format
        times = [strptime(str(x), "%Y-%m-%dT%H:%M:%SZ") for x in times]
        coords = track.xpath("./gx:coord", namespaces = nsmap)
        coords = [tuple([float(y) for y in str(x).split(' ')]) for x in coords]
        points = zip(times, coords)
        track_result += points
        del times
        del coords
    return track_result

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "USAGE: %s ABSOLUTE_PATH" % sys.argv[0]
        quit()

    print get_tracks(sys.argv[1])

