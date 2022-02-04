"""This module contains simple helper functions """
import numpy as np
from PIL import Image
import os
import sys
import pathlib

def rgb2gray(pil_image):
    img_array = np.array(pil_image)
    r, g, b = img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray


def isBackgroundImage(pil_img, tresh_value=0.6):
    # img_gray = rgb2gray(pil_img)
    img_gray = np.array(pil_img)

    # for color in range(0,250):
    # mask = (img_gray >= float(color)) * (img_gray < float(color) + 50)
    # mask_black = img_gray < float(color) + 10

    # # white
    mask = img_gray > 220
    # # black
    # mask_black = img_gray < 70

    # mask = mask_black + mask_white

    if np.count_nonzero(mask) > tresh_value * mask.size:
        is_background = True
        # break
    else:
        is_background = False

    return (is_background)


def isWhiteImage(gray, tresh_value = 0.5):
    mask = gray > 220
    if sum(sum(mask)) > tresh_value * (len(mask) * len(mask)):
        all_white = True
    else:
        all_white = False

    return (all_white)


def save_image(image_numpy, image_path, aspect_ratio=1.0):
    """Save a numpy image to the disk

    Parameters:
        image_numpy (numpy array) -- input numpy array
        image_path (str)          -- the path of the image
    """

    image_pil = Image.fromarray(image_numpy)
    h, w, _ = image_numpy.shape

    if aspect_ratio > 1.0:
        image_pil = image_pil.resize((h, int(w * aspect_ratio)), Image.BICUBIC)
    if aspect_ratio < 1.0:
        image_pil = image_pil.resize((int(h / aspect_ratio), w), Image.BICUBIC)
    image_pil.save(image_path)


def print_numpy(x, val=True, shp=False):
    """Print the mean, min, max, median, std, and size of a numpy array

    Parameters:
        val (bool) -- if print the values of the numpy array
        shp (bool) -- if print the shape of the numpy array
    """
    x = x.astype(np.float64)
    if shp:
        print('shape,', x.shape)
    if val:
        x = x.flatten()
        print('mean = %3.3f, min = %3.3f, max = %3.3f, median = %3.3f, std=%3.3f' % (
            np.mean(x), np.min(x), np.max(x), np.median(x), np.std(x)))


def mkdirs(paths):
    """create empty directories if they don't exist

    Parameters:
        paths (str list) -- a list of directory paths
    """
    if isinstance(paths, list) and not isinstance(paths, str):
        for path in paths:
            mkdir(path)
    else:
        mkdir(paths)


def mkdir(path):
    """create a single empty directory if it didn't exist

    Parameters:
        path (str) -- a single directory path
    """
    if not os.path.exists(path):
        os.makedirs(path)


# retrieve correct path depending on os and sds
def check_os(sds=False):
    path = ''
    if sys.platform == "linux":
        if sds:
            path = '/sds_hd/sd18a006/'
        path1 = '/home/marlen/'
        path2 = '/home/mr38/'
        if pathlib.Path('/home/marlen/').exists():
            return path1 + path
        elif pathlib.Path('/home/mr38/').exists():
            return path2 + path
        else:
            print('error: sds path cannot be defined! Abort')
            return 1
    elif sys.platform == "win32":
        path = ''
        if sds:
            path = '//lsdf02.urz.uni-heidelberg.de/sd18A006/'
        else:
            path = 'C:/Users/mr38/'
        if pathlib.Path(path).exists():
            return path
        else:
            print('error: sds path cannot be defined! Abort')
            return 1
    else:
        print('error: sds path cannot be defined! Abort')
        return 1

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
