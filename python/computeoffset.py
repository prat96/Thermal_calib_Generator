import os
import numpy as np

from gain import compute_gain
from read_pgm_file import get_data


def compute_offsetdirectory():
    directory = '../datasets/offset/'
    offsetdirectories = []
    i = 0

    for d in os.walk(directory):
        # print(d)
        d[1].sort()
        # print(d[1])
        # print(len(d[1]))
        while i < len(d[1]):
            offsetnumber = d[1][i]
            # print(offsetnumber)
            offsetdirectory = '../datasets/offset/' + offsetnumber + '/'
            # print('offset directories = ', offsetdirectory)
            offsetdirectories.append(offsetdirectory)
            i = i + 1
    return offsetdirectories


def compute_avg_offsetmats(x):
    i = 0
    k = 0
    avgimg_offset = 0
    avg_offset_Mats = []
    while (k < len(x)):
        for e in os.walk(x[k]):
            # print('e = ', e[2])
            print('directory number = ', x[k])
            while i < 60:
                offsetfile = e[2][i]
                # print('offsetfile = ', offsetfile)
                image = np.array(get_data(x[k] + offsetfile), dtype=np.float)
                # np.memmap(filename, dtype='uint16', mode='r').reshape(480, 648)
                # print(image)
                avgimg_offset = image + avgimg_offset
                i = i + 1
        averaged_offset = avgimg_offset / 60
        # print(averaged_offset)
        avg_offset_Mats.append(averaged_offset)
        i = 0
        k = k + 1
        avgimg_offset = 0
    return avg_offset_Mats


def compute_offsetmats(x, g_low, g_high):
    Offset_Mats = []
    gainfile = ('./results/Gain_mat_' + str(g_low) + '_' + str(g_high))
    Gainmat = np.array(np.loadtxt(gainfile))

    k = 0
    while (k < len(x)):
        # print('offsetmat number ', k)
        GI = np.multiply(np.nan_to_num(Gainmat), np.nan_to_num(x[k]))
        medianGI = np.median(GI)
        # print('GI medain = ', medianGI)
        Offsetmat = GI - medianGI  # This is Offset Coefficient for the image to which nuc has to apply
        # print(Offsetmat)
        k = k + 1
        Offset_Mats.append(Offsetmat)

    return Offset_Mats


def save_offsetmats(x, t_low, t_high, t_step):
    filename = []
    k = 0
    for i in range(t_low, t_high, t_step):
        filename.append('./results/Offset_Mat_' + str(i))
        np.savetxt(filename[k], x[k], fmt="%2.7f")
        k = k + 1
    print('Saved Offset_Mats')


def main(g_low, g_high, t_low, t_high, t_step):
    offset_directories = compute_offsetdirectory()
    avg_offsetmats = compute_avg_offsetmats(offset_directories)
    offset_Mats = compute_offsetmats(avg_offsetmats, g_low, g_high)
    save_offsetmats(offset_Mats, t_low, t_high, t_step)
