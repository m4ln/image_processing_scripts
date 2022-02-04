import os
import glob
from PIL import Image
import numpy as np
from sys import platform
from util.util import assure_path_exists
from util.util import isBackgroundImage
import shutil
from pathlib import Path

if __name__ == '__main__':

    # =====================================================
    # set variables

    # relative input path on sds
    path = "/marlen/datasets/tatar/HE.vmic/2048/"
    # relative path (or absolute)
    rel_path = True
    # remove files (or seperate them)
    remove_files = False

    # =====================================================

    if rel_path:
        if platform == "linux":
            sds_path = '/home/mr38/sds_hd/sd18a006/'
        elif platform == "win32":
            sds_path = 'Z:/'
        path = sds_path + path

    # create subfolder if images should bee moved instead of being deleted
    if not (remove_files):
        path_corrupted = path + '/corrupted/'
        assure_path_exists(path_corrupted)

    # convert to path
    path = Path(path)
    path_corrupted = Path(path_corrupted)
    print(path)

    # list of all files
    image_files_list = [f for f in path.glob('*.png')]

    for image_file in image_files_list:
        image_file = str(image_file)
        try:
            image = Image.open(image_file)
            image.verify()  # verify that it is, in fact an image
        except:
            print('Bad file:', image_file)  # print out the names of corrupt files
            image.close()
            if (remove_files):
                os.remove(image_file)
            else:
                shutil.move(image_file, path_corrupted)

        # check if image is all white or black
        try:
            image = Image.open(image_file)
            if isBackgroundImage(image, 0.999):
                print('background image:', image_file)  # print out the names of corrupt files
                image.close()
                if (remove_files):
                    os.remove(image_file)
                else:
                    shutil.move(image_file, path_corrupted)
        except:
            continue

    print('Done')
