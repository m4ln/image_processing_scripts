"""This module contains simple helper functions """
from sys import platform
import os
import shutil
import cv2
import numpy as np

def getSdsPath():
    """
    get the sds path based on the operating system
    :return: sds path if os is win or linux, otherwise error
    """
    if platform == "linux":
        sds_path = '/sds_hd/sd18a006/'
    elif platform == "win32":
        sds_path = "//lsdf02.urz.uni-heidelberg.de/sd18A006/"
    else:
        print('error: sds path cannot be defined! Abort')
        return 1

    return sds_path

def ensurePathExists(path, overwrite=True):
    """
    creates a new folder and/or clears existing folder
    :param path: path to the new folder
    :param overwrite: if True, overwrites content if folder already exists, otherwise keeps it
    :return:
    """
    if os.path.exists(path) and overwrite == True:
        print('folder cleared')
        shutil.rmtree(path)
    if not os.path.exists(path):
        print('folder created')
        os.makedirs(path)

def rgb2gray(img_rgb):
    """
    converts rgb to grayscale image
    :param img_rgb: rgb image to be converted to grayscale
    :return: grayscale image
    """
    r, g, b = img_rgb[:, :, 0], img_rgb[:, :, 1], img_rgb[:, :, 2]
    img_gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return img_gray

def isBackgroundImage(img, tresh_value = 0.5, isWhite=True):
    """
    checks if an image is  background image containing either all white or all black pixels
    :param img: input image
    :param tresh_value: threshold value between 0.0 - 1.0 giving the percentage of bg pixels inside the image
    :param isWhite: if True, search for white pixels, otherwise black
    :return: True, if image contains only bg pixels, False otherwise
    """

    if (isWhite):
        # check for white image
        mask = img > 220
    else:
        # check for black image
        mask = img == 0

    if np.count_nonzero(mask) > tresh_value * mask.size:
        is_bg = True
    else:
        is_bg = False

    return (is_bg)

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

if __name__ == '__main__':
    test_path = '../../test/'
    # 1
    print(getSdsPath())
    # 2
    ensurePathExists(test_path + 'ensure_path/', True)
    # 3
    img_rgb = cv2.imread('../../data/mix#1.png')
    cv2.imwrite(test_path + 'img_rgb.png', img_rgb)
    img_gray = rgb2gray(img_rgb)
    cv2.imwrite(test_path + 'img_gray.png', img_gray)
    # 4
    img_white = cv2.imread('../../data/white#1.png')
    img_black = cv2.imread('../../data/black#1.png')
    print(isBackgroundImage(img_white))
    print(isBackgroundImage(img_black))
    print(isBackgroundImage(img_black, isWhite=False))
    # 6
    printNumpy(img_rgb)
