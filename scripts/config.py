
# import
from util.get_sds_path import get_sds_path

## paths
# ----------
# relative path (or absolute)
useSds = True
# if data is saved on sds then get path depending on os, otherwise change the paths below to match your needs
sds_pth = get_sds_path()
# folder where the images are stored
src_pth = sds_pth + '/marlen/scripts/python_image_processing/data/'
# folder where the labels are stored
lbl_folder = '/output'
# label name suffix
lbl_sufx = '-labelsIDX2classes'
# path to the images and labels; must have the following structure:
# ./<image_folder>/id.<im_type> ./<label_folder>/id-labels.<im_type>
# src_pth = sds_pth + '/marlen/students/erdi_semiSupervisedSegmentation/datasets/urothelial/classes_12/val/new/'
# path to store the files after sorting
trgt_pth = sds_pth + '/marlen/scripts/python_image_processing/test/'

## images
# ----------
# type of image format (e.g .png, .jpg)
img_type = '.png'
# image size (w, h) for resizing
img_size = 512
# remove files (or seperate them)
removeFiles = False
# thresh value for removing background images
thresh_val = 0.5
# background pixels are white (or black otherwise)
isWhite = True


## training details
# ----------
# split of train and val images in percent (e.g. 1.0: 100% train, 0% val; 0.1: 10% train, 90% val)
train_split = 1.0

