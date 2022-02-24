
import cv2
import numpy as np

THRESH_VAL = 0.7

def is_background_image(path_to_image, thresh_value=THRESH_VAL, is_white=True):
    """
    checks if an image is  background image containing either all white or all black pixels
    
    Args:
        path_to_image: path to input image
        thresh_value: threshold value between 0.0 - 1.0 giving the percentage of bg pixels inside the image
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


if __name__ == '__main__':
    from scripts.config import src_pth

    print(is_background_image(src_pth + '/white#1.png'))
    print(is_background_image(src_pth + '/black#1.png'))
    print(is_background_image(src_pth + '/black#1.png', is_white=False))

