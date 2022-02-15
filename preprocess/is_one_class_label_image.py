
import cv2
import numpy as np
import os

def isOneClassLabelImage(label_path):
    """
    print if a label image containins only one class
    :param label_path: path to the label image
    :return: True, if the image contains one class, False otherwise
    """

    label = cv2.imread(label_path)

    if label is None:
        print('cannot find label image')
        return False
    else:
        if len(np.unique(label[:,:,0])) == 1 and len(np.unique(label[:,:,1])) == 1 and len(np.unique(label[:,:,2])) == 1:
            return True
        else:
            return False

if __name__ == '__main__':
    from scripts.config import src_pth
    import glob

    # iterate through all files
    label_files = glob.glob(src_pth + '/one_class_images/labels/*.png')

    for label_file in label_files:
        # print labels containing one class
        print(isOneClassLabelImage(label_file))