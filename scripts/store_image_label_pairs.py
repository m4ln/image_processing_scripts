""" Script to store a specific number of image label pairs in a specified directory
To use this script change the variables starting from line 12
"""

import shutil
import glob
from util.ensure_path_exists import ensure_path_exists
import os


# SET VARIABLES
image_path = 'C:/Users/mr38/projects/masterproject_valentin_barth/data/classes_12/Input/train/'
label_path = 'C:/Users/mr38/projects/masterproject_valentin_barth/data/classes_12/Output/train/'
image_type = '.png'
target_path_images = 'C:/Users/mr38/projects/masterproject_valentin_barth/data/classes_12/Input/small/'
target_path_labels = 'C:/Users/mr38/projects/masterproject_valentin_barth/data/classes_12/Output/small/'
label_suffix = '-labelsIDX2classes'
number_of_files_to_copy = 200


if __name__ == '__main__':

    # create target paths if none exist or overwrite them
    ensure_path_exists(target_path_images)
    ensure_path_exists(target_path_labels)

    # iterate through all files
    img_files = glob.glob(image_path + '/*' + image_type)
    if(number_of_files_to_copy < len(img_files)):
        img_files = img_files[:number_of_files_to_copy]

    for img_file in img_files:
        img = os.path.basename(img_file)
        label_file = label_path + img[:-4] + label_suffix + img[-4:]

        if os.path.isfile(label_file):
            shutil.copy(img_file, target_path_images)
            shutil.copy(label_file, target_path_labels)