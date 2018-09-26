import os
import numpy as np

from read_pgm_file import get_data
from read_pgm_file import read_pgm

"""
directory = './datasets/sample/'
i = 0
avgimg = 0

for d in os.walk(directory):
    #print(d)
    while i < 60:
        filename = d[2][i]
        #print filename 
        image = np.array(get_data('./datasets/sample/' + filename))
        #print image

        avgimg = image + avgimg
        avgimg = avgimg/2
        i = i + 1

np.absolute(avgimg)
print np.around(avgimg, decimals=-1)
print avgimg.shape
avgimgval = np.average(avgimg)
print np.around(avgimgval, decimals=-1)
"""


def lowtemp_avg():
    directory = '../datasets/gain/low_temp/'
    i = 0
    avgimg_low = 0

    for d in os.walk(directory):
        # print(d)
        while i < 60:
            filename = d[2][i]
            # print filename
            image = np.array(get_data('../datasets/gain/low_temp/' + filename))
            # print image
            avgimg_low = image + avgimg_low
            avgimg_low = avgimg_low / 2
            i = i + 1

    np.absolute(avgimg_low)
    print(np.around(avgimg_low, decimals=0))
    print(avgimg_low.shape)
    avgimg_lowval = np.average(avgimg_low)
    print(np.around(avgimg_lowval, decimals=0))


def hightemp_avg():
    directory = '../datasets/gain/high_temp/'
    i = 0
    avgimg_high = 0

    for d in os.walk(directory):
        # print(d)
        while i < 60:
            filename = d[2][i]
            # print filename
            image = np.array(get_data('../datasets/gain/high_temp/' + filename))
            # print image
            avgimg_high = image + avgimg_high   
            avgimg_high = avgimg_high / 2
            i = i + 1

    np.absolute(avgimg_high)
    print(np.around(avgimg_high, decimals=0))
    print(avgimg_high.shape)
    avgimg_highval = np.average(avgimg_high)
    print(np.around(avgimg_highval, decimals=0))


if __name__ == '__main__':
    lowtemp_avg()
    hightemp_avg()
