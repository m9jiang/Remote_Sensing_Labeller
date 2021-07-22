import numpy as np


def read_bil_hdr(bil_path):
    bil_path_no_ext = bil_path[:bil_path.rindex('.')]
    hdr_path = bil_path_no_ext + '.hdr'
    f = open(hdr_path,'r')
    lines = f.readlines()
    for lines in lines:
        if "lines = " in lines:
            row = int(lines[lines.rindex(' = ')+3:])
            print('row = {}'.format(row))
        elif "samples = " in lines:
            col = int(lines[lines.rindex(' = ')+3:])
            print('col = {}'.format(col))
    
    return row, col


def read_IRGS_bil(bil_path, bil_rows, bil_cols):
    '''This function is a simple way to read bil file from MAGIC
    Data type of IRGS results is int32, while autopolygon is int8'''

    bil_array = np.fromfile(bil_path, dtype=np.int32)
    bil_array = bil_array.reshape(bil_rows, bil_cols)

    return bil_array