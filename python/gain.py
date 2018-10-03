import os
import numpy as np

from read_pgm_file import get_data


def lowtemp_avg():
    directory = '../datasets/gain/low_temp/'
    i = 0
    avgimg_low = 0

    files = os.listdir('../datasets/gain/low_temp/')
    while i < 60:
        image = np.array(get_data('../datasets/gain/low_temp/' + files[i]), dtype=np.float)
        # np.memmap(filename, dtype='uint16', mode='r').reshape(480, 648)
        avgimg_low = image + avgimg_low
        i = i + 1

    avgimg_low = avgimg_low / 60.0
    return avgimg_low


def hightemp_avg():
    directory = '../datasets/gain/high_temp/'
    i = 0
    avgimg_high = 0

    files = os.listdir('../datasets/gain/high_temp/')
    while i < 60:
        image = np.array(get_data('../datasets/gain/high_temp/' + files[i]), dtype=np.float)
        avgimg_high = image + avgimg_high
        i = i + 1

    avgimg_high = avgimg_high / 60.0
    return avgimg_high

def compute_gain(avgimg_low, avgimg_high, h, w, g_low, g_high):
    mlow = np.median(avgimg_low)
    print('median of low =', mlow)
    mhigh = np.median(avgimg_high)
    print('median of high =', mhigh)
    I_ones = np.ones((h, w))

    gain_mat = np.divide(((mlow - mhigh) * I_ones), (avgimg_low - avgimg_high))
    gain_mat = np.absolute(gain_mat)
    gain_mat = np.nan_to_num(gain_mat)
    gain_mat = np.clip(gain_mat, 0, 2.0)

    gainfile = ('./results/Gain_mat_' + str(g_low) + '_' + str(g_high))
    np.savetxt(gainfile, gain_mat, fmt="%2.7f")
    # print(gain_mat)
    print('Saved Gain mat.')
    return gain_mat


def main(height,width,g_low,g_high):
    avg_low = lowtemp_avg()
    avg_high = hightemp_avg()
    compute_gain(avg_low, avg_high, height, width, g_low, g_high)
