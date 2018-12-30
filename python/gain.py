import os

import numpy as np


def image_data(sensor, image):
    if sensor == "Atto":
        return image[:, 1:-3]
    if sensor == "VGA":
        return image[:, 4:-4]
    if sensor == "Pico-ulis":
        return image[:, 1:-3]
    if sensor == "Pico-222":
        return image[:, :-4]


def bpcr(image):
    y = [98, 273, 11, 262, 346, 69, 72, 19, 64, 77, 247, 17, 42, 17, 39, 7, 166, 12, 254, 255, 203, 162, 250, 100,
         112,
         203]
    x = [2, 2, 3, 10, 10, 15, 15, 24, 29, 30, 30, 36, 51, 53, 56, 62, 66, 67, 83, 83, 103, 167, 183, 240, 284, 286]

    index = 0
    while (index < len(x)):
        print("initial =", image[x[index], y[index]])
        image[x[index], y[index]] = image[x[index] - 1, y[index]]
        print("after =", image[x[index], y[index]])
        index = index + 1

    return image


def lowtemp_avg(x, sensor):
    avgimg_low = 0
    files = sorted(os.listdir('../datasets/gain/low_temp/camera/'))

    for index, value in enumerate(files):
        # image = get_data('../datasets/gain/pgm/' + files[index], x)
        image = np.memmap('../datasets/gain/low_temp/camera/' + value, dtype='uint16', mode='r').reshape(x)
        image = image_data(sensor, image)
        avgimg_low = image + avgimg_low
        avgimg_low = avgimg_low.astype('uint32')

    avgimg_low = avgimg_low / 60
    # avgimg_low = bpcr(avgimg_low)
    # print("avg_low", np.average(avgimg_low))
    return avgimg_low


def hightemp_avg(x, sensor):
    avgimg_high = 0

    files = sorted(os.listdir('../datasets/gain/high_temp/camera/'))
    for index, value in enumerate(files):
        image = np.memmap('../datasets/gain/high_temp/camera/' + value, dtype='uint16', mode='r').reshape(x)
        image = image_data(sensor, image)
        avgimg_high = image + avgimg_high
        avgimg_high = avgimg_high.astype('uint32')

    avgimg_high = avgimg_high / 60
    # avgimg_high = bpcr(avgimg_high)
    # print(np.average(avgimg_high))
    return avgimg_high


def compute_gain(avgimg_low, avgimg_high, h, w, g_low, g_high):
    w = w - 4
    mlow = np.median(avgimg_low)
    print('median of low =', mlow)
    # medlow = np.mean(avgimg_low)
    # print('mean of low = ', medlow)

    mhigh = np.median(avgimg_high)
    print('median of high =', mhigh)
    I_ones = np.ones((h, w))
    gain_mat = np.divide(((mlow - mhigh) * I_ones), (avgimg_low - avgimg_high))
    gain_mat = np.absolute(gain_mat)
    gain_mat = np.nan_to_num(gain_mat)
    gain_mat = np.clip(gain_mat, 0, 2.0)

    gainfile = ('./results/Gain_mat_' + str(g_low) + '_' + str(g_high))
    np.savetxt(gainfile, gain_mat, fmt="%2.6f")

    gain_mat = np.asarray(gain_mat).reshape(-1)
    np.savetxt('./results/final_gainmat', [gain_mat], fmt="%2.6f", newline=" ", delimiter=",")
    # np.savetxt("./results/final_gainmat", [gain_mat], fmt="%2.6f", newline=" ", delimiter=",")

    # t_gainmat = np.rot90(np.rot90(gain_mat))
    # t_gainmat= np.asarray(t_gainmat).reshape(-1)
    # np.savetxt('./final_results/t_gainmat', [t_gainmat], fmt="%2.6f", newline=" ", delimiter=",")

    print('Saved Gain mat.\n')
    return gain_mat


def main(height, width, g_low, g_high, columns, sensor):
    avg_low = lowtemp_avg(columns, sensor)
    avg_high = hightemp_avg(columns, sensor)
    print(height, width)
    compute_gain(avg_low, avg_high, height, width, g_low, g_high)
