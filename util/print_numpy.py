
import numpy as np


def printNumpy(x, shp=True, val=True):
    """
    Prints the mean, min, max, median, std, and size of a numpy array
    :param x: numpy array
    :param shp: if True prints the shape of the numpy array
    :param val: if True prints the values of the numpy array
    :return:
    """

    x = x.astype(np.float64)
    if shp:
        print('shape =', x.shape)
    if val:
        x = x.flatten()
        print('mean = %3.3f, min = %3.3f, max = %3.3f, median = %3.3f, std=%3.3f' % (
            np.mean(x), np.min(x), np.max(x), np.median(x), np.std(x)))
