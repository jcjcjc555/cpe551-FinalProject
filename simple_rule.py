#!/usr/bin/env python

import numpy
import matplotlib.pyplot as plt
import time

dataDir='/Users/chunji/PycharmProjects/627finalproj/'
file_name_user_rating = dataDir + 'output0.txt'
output_file = dataDir + 'output1.txt'

fIn = open(file_name_user_rating, 'r')
fOut = open(output_file, 'w')

allRating_vec = numpy.zeros(shape=(6,3))
lastUserID = -1

for line in fIn:
    arr_rate = line.strip().split('|')
    userID = arr_rate[0]
    trackID = arr_rate[1]
    track_rating = arr_rate[2]
    album_rating = arr_rate[3]
    artist_rating = arr_rate[4]
    genre_rating = []
    for i in arr_rate[5:]:
        genre_rating.append(float(i))

    if userID != lastUserID:
        ii = 0

    allRating_vec[ii, 0] = userID
    allRating_vec[ii, 1] = trackID
    allRating_vec[ii, 2] = 0*float(track_rating) + 0.7*float(album_rating) + 0.2*float(artist_rating) + 0.1*sum(genre_rating)# just sum the genre
    #allRating_vec[ii, 2] = 0*float(track_rating) + 0*float(album_rating) + 0*float(artist_rating)# get the mean rating of genre

    ii = ii + 1
    lastUserID = userID

    if ii == 6:
        sum_rating = [x[2] for x in allRating_vec]
        result = numpy.argsort(sum_rating)
        outStr = ['-1']*6
        for kk in range(6):
            outStr[kk] = '1' if kk in result[-3:] else '0'
        for nn in outStr:
            fOut.write(nn + '\n')

fIn.close()
fOut.close()