import os

import numpy as np
from read_pgm_file import get_data
from read_pgm_file import get_temperature_columns


def mat_conversion(file_path):
    image = get_data(file_path)
    bolo = get_temperature_columns(file_path)
    print(bolo.shape)
    bolo_avg = np.average(bolo)
    first_row = np.ones((1, 323)) * bolo_avg
    print(bolo_avg, image.shape, first_row.shape)
    image = np.vstack((first_row, image))
    np.savetxt(file_path.split('.')[0] + '.mat', image, fmt="%2.1f")


def multiple_folders(root_folder_dir):
    for folder in os.listdir(root_folder_dir):
        folder = root_folder_dir + folder + '/'
        mat_conversion_in_folder(folder)


def mat_conversion_in_folder(folder):
    pgms = [folder + file for file in os.listdir(folder) if 'pgm' in file]
    for pgm in pgms:
        mat_conversion(pgm)


if __name__ == '__main__':
    root_folder_dir = '/home/pratheek/Tonbo/Code/Generator/datasets/offset/'
    folder = '/home/pratheek/CALIBS/ULIS_datasets/100_frames/'

    multiple_folders(root_folder_dir)
