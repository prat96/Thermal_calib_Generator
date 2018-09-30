import os
import numpy as np

from read_pgm_file import get_data


def lowtemp_avg():
    global avgimg_low
    directory = '../datasets/gain/low_temp/'
    i = 0
    avgimg_low = 0

    for d in os.walk(directory):
        # print(d)
        while i < 60:
            filename = d[2][i]
            # print filename
            image = np.array(get_data('../datasets/gain/low_temp/' + filename), dtype=np.float)
            # np.memmap(filename, dtype='uint16', mode='r').reshape(480, 648)
            avgimg_low = image + avgimg_low
            i = i + 1

    avgimg_low = avgimg_low / 60.0
    print(avgimg_low.shape)
    avgimg_lowval = np.average(avgimg_low)
    print(avgimg_lowval)


def hightemp_avg():
    global avgimg_high
    directory = '../datasets/gain/high_temp/'
    i = 0
    avgimg_high = 0

    for d in os.walk(directory):
        # print(d)
        while i < 60:
            filename = d[2][i]
            # print(filename)
            image = np.array(get_data('../datasets/gain/high_temp/' + filename), dtype=np.float)
            avgimg_high = image + avgimg_high
            i = i + 1

    avgimg_high = avgimg_high / 60.0
    print(avgimg_high.shape)
    avgimg_highval = np.average(avgimg_high)
    print(avgimg_highval)


def compute_gain():
    lowtemp_avg()
    hightemp_avg()

    mlow = np.median(avgimg_low)
    print('median of low =', mlow)
    mhigh = np.median(avgimg_high)
    print('median of high =', mhigh)
    I_ones = np.ones((640, 480))

    gain_mat = np.divide(((mlow - mhigh) * I_ones), (avgimg_low - avgimg_high))
    gain_mat = np.absolute(gain_mat)
    gain_mat = np.nan_to_num(gain_mat)
    gain_mat = np.clip(gain_mat, 0, 2.0)
    print('gain_mat -->')
    print(gain_mat)
    return gain_mat


if __name__ == '__main__':
    compute_gain()
