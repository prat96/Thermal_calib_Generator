import os
import numpy as np

from read_pgm_file import get_data
from read_pgm_file import read_pgm


def lowtemp_avg():
    directory = '../datasets/gain/low_temp/'
    i = 0
    avgimg_low = 0

    for d in os.walk(directory):
        # print(d)
        while i < 60:
            filename = d[2][i]
            # print filename
            image = np.array(get_data('../datasets/gain/low_temp/' + filename), dtype = np.uint16)
            print(image)
            avgimg_low = image + avgimg_low
            avgimg_low = avgimg_low / 2
            i = i + 1

    print(avgimg_low.shape)
    avgimg_lowval = np.average(avgimg_low)
    print(avgimg_lowval)
    global avgimg_low

def hightemp_avg():
    directory = '../datasets/gain/high_temp/'
    i = 0
    avgimg_high = 0

    for d in os.walk(directory):
        # print(d)
        while i < 60:
            filename = d[2][i]
            # print filename
            image = np.array(get_data('../datasets/gain/high_temp/' + filename), dtype = np.uint16)
            # print image
            avgimg_high = image + avgimg_high
            avgimg_high = avgimg_high / 2
            i = i + 1

    print(avgimg_high.shape)
    avgimg_highval = np.average(avgimg_high)
    print(avgimg_highval)
    global avgimg_high

def compute_gain():
    mlow = np.median(avgimg_low)
    print('median of low = ', mlow)
    mhigh = np.median(avgimg_high)
    print('median of high =', mhigh)

    avgdiff = (avgimg_high-avgimg_low)
    print('avgdiff')
    print(avgdiff)

    gain_mat = ((mhigh-mlow)/(avgimg_high-avgimg_low))
    np.abs(gain_mat)
    print('gain_mat -->')
    print(gain_mat)

if __name__ == '__main__':
    lowtemp_avg()
    hightemp_avg()
    compute_gain()