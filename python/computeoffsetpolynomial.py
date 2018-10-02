import os
import numpy as np

from computeoffset import *
from gain import *


def compute_offset_polynomial(x):
    t_lo = 10
    t_high = 51
    t_step = 4
    i = 0
    y = np.arange(t_lo, t_high, t_step)
    print(y)
    poly_coeffs = []
    k = 0

    while (i < len(y)):
        print('x[k] =', x[k])
        print(x[k].dtype)
        x[k] = np.array(x[k])
        x = np.asarray(x)
        polynomial_coefficients = np.polyfit(y, x, 2)
        print(polynomial_coefficients)

        poly_coeffs.append(polynomial_coefficients)
    k = k + 1

    print('poly coefficients = ', poly_coeffs)
    print(poly_coeffs.shape)


if __name__ == '__main__':
    offset_directories = compute_offsetdirectory()
    avg_offsetmats = compute_avg_offsetmats(offset_directories)

    offset_Mats = compute_offsetmats(avg_offsetmats)

    compute_offset_polynomial(offset_Mats)
