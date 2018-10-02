import os
import numpy as np

from computeoffset import compute_offsetdirectory
from read_pgm_file import get_temperature_columns


def get_bolometer_mats():
    offsetdirects = compute_offsetdirectory()
    print(offsetdirects)
    x = offsetdirects
    i = 0
    k = 0
    avgimg_bolo = 0
    avg_bolo_Mats = []
    mean_bolos = []
    mean_bolo = 0
    while (k < len(x)):
        for e in os.walk(x[k]):
            # print('e = ', e[2])
            print('directory number = ', x[k])
            while i < 60:
                offsetfile = e[2][i]
                # print('offsetfile = ', offsetfile)
                image = np.array(get_temperature_columns(x[k] + offsetfile), dtype=np.float)
                # np.memmap(filename, dtype='uint16', mode='r').reshape(480, 648)
                # print(image)
                avgimg_bolo = image + avgimg_bolo
                i = i + 1
        averaged_bolo = avgimg_bolo / 60
        # print(averaged_bolo)
        print(averaged_bolo.shape)
        avg_bolo_Mats.append(averaged_bolo)
        mean_bolo = np.mean(averaged_bolo)
        mean_bolos.append(mean_bolo)
        i = 0
        k = k + 1
        avgimg_bolo = 0
    # print(avg_bolo_Mats[0])
    print(mean_bolos)
    # print('mean bolo 1 = ', np.mean(avg_bolo_Mats[0]))
    return mean_bolos


def compute_bolo_coefficients(x):
    t_lo = 10
    t_high = 51
    t_step = 4
    filename = ('./results/bolo_coefficients')

    y = np.arange(t_lo, t_high, t_step)
    print(y)

    bolo_coefficients = np.polyfit(x, y, 1)
    print(bolo_coefficients)
    np.savetxt(filename, bolo_coefficients, fmt="%2.7f")

if __name__ == '__main__':
    mean_bolos = get_bolometer_mats()
    compute_bolo_coefficients(mean_bolos)
