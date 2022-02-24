import os
import shutil
import glob
from util.get_sds_path import get_sds_path
from util.ensure_path_exists import ensure_path_exists
from preprocess.is_background_image import is_background_image

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


if __name__ == '__main__':

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



