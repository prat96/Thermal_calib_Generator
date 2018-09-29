import os
import numpy as np

from gain import compute_gain
from read_pgm_file import get_data


def compute_offsetdirectory():
    global offset_matrix
    directory = '../datasets/offset/'
    i = 0
    avgimg_offset = 0
    offsetdirectories = []

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


def compute_offsetmats(x):
    print('recieved offset mats -->', x[1])
    Offset_Mats = []
    Gainmat = np.array(compute_gain())

    k = 0
    while (k < len(x)):
        print('offsetmat number ', k)
        GI = np.multiply(np.nan_to_num(Gainmat), np.nan_to_num(x[k]))
        np.abs(GI)
        medianGI = np.median(GI)
        print('GI medain = ', medianGI)
        Offsetmat = GI - medianGI  # This is Offset Coefficient for the image to which nuc has to apply
        np.abs(Offsetmat)
        # print(Offsetmat)
        k = k + 1
        Offset_Mats.append(Offsetmat)

    print(Offset_Mats)
    print(len(Offset_Mats))
    return Offset_Mats


if __name__ == '__main__':
    offset_directories = compute_offsetdirectory()
    avg_offsetmats = compute_avg_offsetmats(offset_directories)

    compute_offsetmats(avg_offsetmats)
