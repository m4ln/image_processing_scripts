""" Script to store a specific number of image label pairs in a specified directory
To use this script change the variables starting from line 12
"""

import glob
import os
import shutil

from util.ensure_path_exists import ensure_path_exists

if __name__ == '__main__':

    # SET VARIABLES
    image_path = 'D:/projects/masterproject_valentin_barth/data/classes_123/Input' \
                 '/orig/'
    label_path = 'D:/projects/masterproject_valentin_barth/data/classes_123' \
                 '/Output/orig/'
    image_type = '.png'
    target_path_images = os.path.join(image_path, '../new/orig')
    target_path_labels = os.path.join(label_path, '../new/orig')
    label_suffix = '-labels'
    number_of_files_to_copy = 20000

    # create target paths if none exist or overwrite them
    ensure_path_exists(target_path_images)
    ensure_path_exists(target_path_labels)

    # iterate through all files
    img_files = glob.glob(image_path + '/*' + image_type)
    if (number_of_files_to_copy < len(img_files)):
        img_files = img_files[:number_of_files_to_copy]

    for img_file in img_files:
        img = os.path.basename(img_file)
        label_file = label_path + img[:-4] + label_suffix + img[-4:]

        if os.path.isfile(label_file):
            shutil.copy(img_file, target_path_images)
            shutil.copy(label_file, target_path_labels)
