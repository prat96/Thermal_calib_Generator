import os
import numpy as np

from computeoffset import *
from gain import *


def get_offset_Mats():
    t_lo = 10
    t_high = 51
    t_step = 4
    y = np.arange(t_lo, t_high, t_step)
    filename = []
    offset_array = np.zeros((len(y), 640, 480))
    k = 0

    for i in range(t_lo, t_high, t_step):
        filename.append('./results/Offset_Mat_' + str(i))
        offset_m = np.loadtxt(filename[k])
        offset_array[k] = offset_m
        k = k + 1
    return offset_array, y


def compute_offset_polynomial(offset_array, y):
    offset_polynomial = np.zeros((3, 640, 480))
    pix_offset_Acc = []
    t_lo = 10
    t_high = 51
    t_step = 4
    #    print(offset_array[[0], [639], [479]])

    for i in range(0, 640, 1):
        for j in range(0, 480, 1):
            index = 0
            pix_offset_Acc = []
            for k in range(t_lo, t_high, t_step):
                temp = k
                pix_offset_Acc.append(offset_array[[index], [i], [j]])
                index = index + 1
            #print('lenght = ', len(pix_offset_Acc))
            poly = np.polyfit(y, pix_offset_Acc, 2)
            #print(poly)
            offset_polynomial[[0],[i],[j]] = poly[0]
            offset_polynomial[[1],[i],[j]] = poly[1]
            offset_polynomial[[2],[i],[j]] = poly[2]


    print('c1 = ', offset_polynomial[0])
    np.savetxt("./results/c1_mat", offset_polynomial[0], fmt="%2.7f")
    np.savetxt("./results/c2_mat", offset_polynomial[1], fmt="%2.7f")
    np.savetxt("./results/c3_mat", offset_polynomial[2], fmt="%2.7f")
#        polynomial_coefficients = np.polyfit(y, x, 2)


if __name__ == '__main__':
    offset_array, y = get_offset_Mats()
    compute_offset_polynomial(offset_array, y)
