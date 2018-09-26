"""
import numpy as np

filename = "14.yuv"
a = np.memmap(filename, dtype='uint16', mode='r').reshape(480, 648)
np.transpose(a)

print a.shape
print a.data[-3:, :]


import os
directory = 'the/directory/you/want/to/use'

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        f = open(filename)
        lines = f.read()
        print (lines[10])
        continue
    else:
    continue
"""

import os
import numpy

from read_pgm_file import get_data
directory = './datasets/'

def main():
  #  if do_adb_actions(wait_for_dumps=5) == -1:
   #     exit(-1)
   # fname = '14.yuv'
  #  pull_files(file = fname)
  #  print('swap.c being called')
   # os.system('gcc -o swap swap.c')
   # os.system('./swap imglib_inputdump_ 5 5')
   # data = get_data(fname.split('.')[0] + '.pgm')

	for filename in os.listdir(directory):


    		data = get_data(fname.split('.')[0] + '.pgm')
    
    	print 'Average:', numpy.average(data)
    	print '2nd percentile:', numpy.percentile(data, 2)
    	print '98th percentile:', numpy.percentile(data, 98)




if __name__ == '__main__':
    
    main()


def scan_folder(parent):
    # iterate over all the files in directory 'parent'
    for file_name in os.listdir(parent):
        if file_name.endswith(".txt"):
            # if it's a txt file, print its name (or do whatever you want)
            print(file_name)
        else:
            current_path = "".join((parent, "/", file_name))
            if os.path.isdir(current_path):
                # if we're checking a sub-directory, recall this method
                scan_folder(current_path)

scan_folder("/example/path")