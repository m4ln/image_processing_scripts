import numpy as np


def print_numpy(array, shape=True, val=True):
    """
    Prints the mean, min, max, median, std, and size of a numpy array

    Args:
        array: numpy array
        shape: if True prints the shape of the numpy array
        val: if True prints the values of the numpy array

    Returns:

    """

    array = array.astype(np.float64)

    if shape:
        print('shape =', array.shape)
    if val:
        array = array.flatten()
        print(
            'mean = %3.3f, min = %3.3f, max = %3.3f, median = %3.3f, std=%3.3f' % (
                np.mean(array), np.min(array), np.max(array), np.median(array),
                np.std(array)))
