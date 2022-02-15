
import shutil
import glob
from preprocess.is_one_class_label_image import isOneClassLabelImage
from util.ensure_path_exists import ensurePathExists
import os

def copyOneClassImagesLabels(imgs_path, labels_path, target_path, img_type='.png', label_suffix='-labels'):

    # iterate through all files
    img_files = glob.glob(imgs_path + '/*' + img_type)

    target_path += '/one_class_images_labels/'
    one_class_img_dir =  target_path + '/images/'
    one_class_label_dir =  target_path + '/labels/'

    ensurePathExists(one_class_img_dir)
    ensurePathExists(one_class_label_dir)

    for img_file in img_files:
        img = os.path.basename(img_file)
        label_file = labels_path + img[:-4] + label_suffix + img[-4:]
        if isOneClassLabelImage(label_file):
            shutil.copy(img_file, one_class_img_dir)
            shutil.copy(label_file, one_class_label_dir)


if __name__ == '__main__':
    from scripts.config import src_pth, trgt_pth

    # iterate through all files
    img_files = src_pth + '/one_class_images/images/'
    label_files = src_pth + '/one_class_images/labels/'

    copyOneClassImagesLabels(img_files, label_files, trgt_pth, label_suffix='')