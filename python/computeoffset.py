import os
import numpy as np

from gain import compute_gain
from read_pgm_file import get_data

"""

function[OffsetMat] = ComputeOffset(GainMat, AvgImgMat, OffsetPath, T_amb)
GI = GainMat. * AvgImgMat; % GI = > Gain Corrected Image
medianGI = median(GI(:));
OffsetMat = round(100000 * (GI - medianGI)). / 100000; % This is Offset Coefficient for the image to which nuc has to apply

OffsetName = sprintf('Offset_Mats/Offset_%d.mat', T_amb);
OffsetFile = strcat(OffsetPath, OffsetName);
dlmwrite(OffsetFile, OffsetMat, ' ');
end

"""


# Gainmat = compute_gain()

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


def compute_offsetmats(x):
    i = 0
    k = 0
    avgimg_offset = 0
    while (k < len(x)):
        for e in os.walk(x[k]):
            #print('e = ', e[2])
            print('directory number = ', x[k])
            while i < 60:
                offsetfile = e[2][i]
                #print('offsetfile = ', offsetfile)
                image = np.array(get_data(x[k] + offsetfile), dtype=np.float)
                # np.memmap(filename, dtype='uint16', mode='r').reshape(480, 648)
                # print(image)
                avgimg_offset = image + avgimg_offset
                i = i + 1
        averaged_offset = avgimg_offset / 60
        print(averaged_offset)
        i = 0
        k = k + 1
        avgimg_offset = 0



"""
avgimg_low = avgimg_low / 60.0
print(avgimg_low.shape)
avgimg_lowval = np.average(avgimg_low)
print(avgimg_lowval)
"""

if __name__ == '__main__':
    offset_directories = compute_offsetdirectory()
    compute_offsetmats(offset_directories)
