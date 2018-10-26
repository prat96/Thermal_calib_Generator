import os
import numpy as np


def image_data(sensor, image):
    if sensor == "Atto":
        return image[:, 1:-3]
    if sensor == "VGA":
        return image[:, 4:-4]


def lowtemp_avg(x, sensor):
    avgimg_low = 0
    files = sorted(os.listdir('../datasets/gain/low_temp/'))

    for index, value in enumerate(files):
        # image = get_data('../datasets/gain/pgm/' + files[index], x)
        image = np.memmap('../datasets/gain/low_temp/' + value, dtype='uint16', mode='r').reshape(x)
        image = image_data(sensor, image)
        avgimg_low = image + avgimg_low
        avgimg_low = avgimg_low.astype('uint32')

    avgimg_low = avgimg_low / 60
    return avgimg_low


def hightemp_avg(x, sensor):
    avgimg_high = 0

    files = sorted(os.listdir('../datasets/gain/high_temp/'))
    for index, value in enumerate(files):
        image = np.memmap('../datasets/gain/high_temp/' + value, dtype='uint16', mode='r').reshape(x)
        image = image_data(sensor, image)
        avgimg_high = image + avgimg_high
        avgimg_high = avgimg_high.astype('uint32')

    avgimg_high = avgimg_high / 60
    print(avgimg_high.shape)
    return avgimg_high


def compute_gain(avgimg_low, avgimg_high, h, w, g_low, g_high):
    mlow = np.median(avgimg_low)
    print('median of low =', mlow)
    medlow = np.mean(avgimg_low)
    print('mean of low = ', medlow)

    mhigh = np.median(avgimg_high)
    print('median of high =', mhigh)
    I_ones = np.ones((h, w))

    gain_mat = np.divide(((mlow - mhigh) * I_ones), (avgimg_low - avgimg_high))
    gain_mat = np.absolute(gain_mat)
    gain_mat = np.nan_to_num(gain_mat)
    gain_mat = np.clip(gain_mat, 0, 2.0)

    gainfile = ('./results/Gain_mat_' + str(g_low) + '_' + str(g_high))
    np.savetxt(gainfile, gain_mat, fmt="%2.6f")
    print('Saved Gain mat.\n')
    return gain_mat


def main(height, width, g_low, g_high, columns, sensor):
    avg_low = lowtemp_avg(columns, sensor)
    avg_high = hightemp_avg(columns, sensor)
    compute_gain(avg_low, avg_high, height, width, g_low, g_high)