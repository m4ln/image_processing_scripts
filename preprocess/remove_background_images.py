import glob
import os
import shutil

import cv2
import numpy as np

from util.ensure_path_exists import ensure_path_exists
from util.get_sds_path import get_sds_path

THRESH_VAL = 0.7


def is_background_image(path_to_image, thresh_value=THRESH_VAL, is_white=True):
    """
    checks if an image is  background image containing either all white or all
    black pixels

    Args:
        path_to_image: path to input image
        thresh_value:
            threshold value between 0.0 - 1.0 giving the percentage of bg pixels
            inside the image
        is_white: if True, search for white pixels, otherwise black

    Returns:
        True, if image contains only bg pixels, False otherwise

    """

    img = cv2.imread(path_to_image)

    if (is_white):
        # check for white image
        mask = img > 220
    else:
        # check for black image
        mask = img == 0

    if np.count_nonzero(mask) > thresh_value * mask.size:
        return True
    else:
        return False


def main():
    #############################################
    # set variables

    # use sds if available
    useSds = True
    # folder where the images are stored
    src_pth = '/marlen/scripts/python_image_processing/data'
    # if images should be deleted leave empty
    trgt_pth = '/marlen/scripts/python_image_processing/test'
    # type of image format (e.g .png, .jpg)
    img_type = '.png'
    # thresh value for removing background images
    thresh_val = 0.5
    # background pixels are white (or black otherwise)
    isWhite = True

    #############################################

    # set paths
    if useSds:
        sds_pth = get_sds_path()
    else:
        sds_pth = ''

    src_pth = sds_pth + src_pth
    trgt_pth = sds_pth + trgt_pth

    if not trgt_pth == '':
        # paths to move images if not being deleted
        save_dir = trgt_pth + '/background/'
        ensure_path_exists(save_dir)

    # iterate through all files
    img_files = glob.glob(src_pth + '/*' + img_type)

    for img_file in img_files:
        if is_background_image(img_file, thresh_val, isWhite):
            print('background image detected: ' + img_file)
            if trgt_pth == '':
                os.remove(img_file)
            else:
                shutil.move(img_file, save_dir)


if __name__ == '__main__':
    main()
