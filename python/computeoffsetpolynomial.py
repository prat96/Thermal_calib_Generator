import os
import numpy as np

from computeoffset import *
from gain import *


def get_offset_Mats(h, w, t_low, t_high, t_step):
    y = np.arange(t_low, t_high, t_step)
    filename = []
    offset_array = np.zeros((len(y), h, w))
    k = 0

    for i in range(t_low, t_high, t_step):
        filename.append('./results/Offset_Mat_' + str(i))
        offset_m = np.loadtxt(filename[k])
        offset_array[k] = offset_m
        k = k + 1
    return offset_array, y


def compute_offset_polynomial(offset_array, y, h, w, t_low, t_high, t_step ):
    offset_polynomial = np.zeros((3, h, w))
    pix_offset_Acc = []
    print('Computing offset polynomial matrices...')
    for i in range(0, h, 1):
        for j in range(0, w, 1):
            index = 0
            pix_offset_Acc = []
            for k in range(t_low, t_high, t_step):
                temp = k
                pix_offset_Acc.append(offset_array[[index], [i], [j]])
                index = index + 1
            poly = np.polyfit(y, pix_offset_Acc, 2)
            offset_polynomial[[0], [i], [j]] = poly[0]
            offset_polynomial[[1], [i], [j]] = poly[1]
            offset_polynomial[[2], [i], [j]] = poly[2]

    np.savetxt("./results/c1_mat", offset_polynomial[0], fmt="%2.7f")
    np.savetxt("./results/c2_mat", offset_polynomial[1], fmt="%2.7f")
    np.savetxt("./results/c3_mat", offset_polynomial[2], fmt="%2.7f")
    print('\nDone.')


def main(height, width, t_low, t_high, t_step):
    offset_array, y = get_offset_Mats(height, width, t_low, t_high, t_step)
    compute_offset_polynomial(offset_array, y, height, width, t_low, t_high, t_step)
