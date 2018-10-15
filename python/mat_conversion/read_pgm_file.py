import os
import numpy


def read_pgm(filename):
    if not os.path.exists(filename):
        print('file %s does not exist...' % filename)
        exit(-1)

    file = open(filename, 'r')
    assert file.readline() == 'P2\n'

    width, height = [int(i) for i in file.readline().split()]
    depth = int(file.readline())

    # if you'd like to downscale the depth for better visualization
    # data = [256.0*float(x)/depth for x in file.readline().split()]
    # depth = 256.0

    data = [float(x) for x in file.readline().split()]
    data = numpy.array(data).reshape(height, width)
    return data, width, height, depth


def get_data(filename):
    '''
    columns_to_read; usually 3,645 when you don't want temp columns
    '''
    data, _, _, _ = read_pgm(filename)
    # return data from column 3 till column 644
    return data[:, 0:323]


# TODO add temp columns as variables
def get_temperature_columns(filename):
    data, _, _, _ = read_pgm(filename)
    return data[:, -3:]
