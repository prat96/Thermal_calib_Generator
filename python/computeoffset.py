import os
import numpy as np


def image_data(sensor, image):
    if sensor == "Atto":
        return image[:, 1:-3]
    if sensor == "VGA":
        return image[:, 4:-4]
    if sensor == "Pico":
        return image[:, :-4]


def compute_offsetdirectory():
    directory = '../datasets/offset/'
    offsetdirectories = []

    directories = os.listdir(directory)
    directories.sort(key=int)
    for index, values in enumerate(directories):
        offsetdirectories.append(directory + values + '/')

    return offsetdirectories


def compute_avg_offsetmats(x, y, sensor):
    i = 0
    avgimg_offset = 0
    avg_offset_Mats = []
    for k, values in enumerate(x):
        for e in os.walk(x[k]):
            print('directory number = ', x[k])
            while i < 60:
                offsetfile = e[2][i]
                image = np.memmap(x[k] + offsetfile, dtype='uint16', mode='r').reshape(y)
                image = image_data(sensor, image)
                avgimg_offset = image + avgimg_offset
                avgimg_offset = avgimg_offset.astype('uint32')
                i = i + 1
        averaged_offset = avgimg_offset / 60
        avg_offset_Mats.append(averaged_offset)
        i = 0
        avgimg_offset = 0
    return avg_offset_Mats


def compute_offsetmats(x, g_low, g_high):
    Offset_Mats = []
    gainfile = ('./results/Gain_mat_' + str(g_low) + '_' + str(g_high))
    Gainmat = np.array(np.loadtxt(gainfile))

    for k, values in enumerate(x):
        GI = np.multiply(np.nan_to_num(Gainmat), np.nan_to_num(x[k]))
        medianGI = np.median(GI)
        Offsetmat = GI - medianGI  # This is Offset Coefficient for the image to which nuc has to apply
        Offset_Mats.append(Offsetmat)

    return Offset_Mats


def save_offsetmats(x, t_low, t_high, t_step):
    filename = []
    k = 0
    for i in range(t_low, t_high, t_step):
        filename.append('./results/Offset_Mat_' + str(i))
        np.savetxt(filename[k], x[k], fmt="%2.6f")
        k = k + 1
    print('Saved Offset_Mats\n')


def main(g_low, g_high, t_low, t_high, t_step, columns, sensor):
    print("Computing offset Mats\n")
    offset_directories = compute_offsetdirectory()
    avg_offsetmats = compute_avg_offsetmats(offset_directories, columns, sensor)
    offset_Mats = compute_offsetmats(avg_offsetmats, g_low, g_high)
    save_offsetmats(offset_Mats, t_low, t_high, t_step)
