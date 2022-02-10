
import cv2
import numpy as np

THRESH_VAL = 0.7

def isBackgroundImage(img_path, thresh_value=THRESH_VAL, isWhite=True):
    """
    checks if an image is  background image containing either all white or all black pixels
    :param img_path: path to input image
    :param thresh_value: threshold value between 0.0 - 1.0 giving the percentage of bg pixels inside the image
    :param isWhite: if True, search for white pixels, otherwise black
    :return: True, if image contains only bg pixels, False otherwise
    """

    img = cv2.imread(img_path)

    if (isWhite):
        # check for white image
        mask = img > 220
    else:
        # check for black image
        mask = img == 0

    if np.count_nonzero(mask) > thresh_value * mask.size:
        return True
    else:
        return False


if __name__ == '__main__':
    from scripts.config import src_pth

    print(isBackgroundImage(src_pth + '/white#1.png'))
    print(isBackgroundImage(src_pth + '/black#1.png'))
    print(isBackgroundImage(src_pth + '/black#1.png', isWhite=False))

