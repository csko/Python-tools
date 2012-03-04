import mlpy
import os
import numpy as np

from kml import get_tracks

TRACKS_DIR="tracks/"

all_tracks = []

i = 0
for fname in os.listdir(TRACKS_DIR):
    tracks = get_tracks(TRACKS_DIR + fname)
    # TODO: multiple tracks
    all_tracks.append(tracks)
    print fname, i
    i += 1

def my_dtw(s1, s2, distfn):
    n = len(s1)
    m = len(s2)
    cost = np.empty((n, m))
    cost[0][0] = distfn(s1[0], s2[0])
    for i in range(2, n):
        cost[i][0] = distfn(s1[i], s2[0]) + cost[i-1][0]
    for j in range(2, m):
        cost[0][j] = distfn(s1[0], s2[j]) + cost[0][j-1]
    for i in range(2, n):
        for j in range(2, m):
            cost[i][j] = distfn(s1[i], s2[j]) + min(
                    cost[i-1][j],
                    cost[i-1][j-1],
                    cost[i][j-1]
                    )
    return cost[n-1][m-1]

def dist_abs(x, y):
    return sum([abs(x[i]-y[i]) for i in range(len(x))])
def dist_euc(x, y):
    return sum([(x[i]-y[i])*(x[i]-y[i]) for i in range(len(x))])

def track_distance(t1, t2):
    t1, t2 = [y for (x,y) in t1], [y for (x,y) in t2]
#   x = mlpy.dtw_std(t1, t2, dist_only=True) # mlpy 1D DTW
    x = my_dtw(t1, t2, dist_abs)
    return x

t1, t2 = all_tracks[0], all_tracks[1]
for i,j in enumerate(all_tracks):
    for k,m in enumerate(all_tracks[i+1:]):
        dist = track_distance(all_tracks[i], all_tracks[i+k+1])
        print i, i+k+1, dist

