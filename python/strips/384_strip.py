import os
import numpy as np

from read_pgm_file import *

def strip_384():
    image = get_data('./imglib_inputdump_51.pgm')
    print(image)
    print(image.shape)
    np.savetxt('converted.pgm', image, fmt="%i")

if __name__ == '__main__':
    print('hello')
    strip_384()