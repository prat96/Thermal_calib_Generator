import os
import numpy as np

from computeoffset import compute_offsetdirectory


def get_bolometer_mats(y):
    x = compute_offsetdirectory()
    print("Getting bolometer matrices\n")
    i = 0
    avgimg_bolo = 0
    avg_bolo_Mats = []
    mean_bolos = []
    for k, values in enumerate(x):
        for e in os.walk(x[k]):
            print('directory number = ', x[k])
            while i < 60:
                offsetfile = e[2][i]
                image = np.memmap(x[k] + offsetfile, dtype='uint16', mode='r').reshape(y)
                image = image[:, -3:]
                avgimg_bolo = image + avgimg_bolo
                avgimg_bolo = avgimg_bolo.astype('uint32')
                i = i + 1
        averaged_bolo = avgimg_bolo / 60
        avg_bolo_Mats.append(averaged_bolo)
        mean_bolo = np.mean(averaged_bolo)
        mean_bolos.append(mean_bolo)
        i = 0
        avgimg_bolo = 0
    return mean_bolos


def compute_bolo_coefficients(x, t_low, t_high, t_step):
    filename = ('./results/bolo_coefficients')
    y = np.arange(t_low, t_high, t_step)
    bolo_coefficients = np.polyfit(x, y, 1)
    print('\nBolometer coefficients =', bolo_coefficients, "\n")
    np.savetxt(filename, bolo_coefficients, fmt="%2.7f")


def main(t_low, t_high, t_step, columns):
    mean_bolos = get_bolometer_mats(columns)
    compute_bolo_coefficients(mean_bolos, t_low, t_high, t_step)
