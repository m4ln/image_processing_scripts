
import shutil
import glob
from preprocess.is_one_class_label_image import is_one_class_label_image
from util.ensure_path_exists import ensure_path_exists
import os

def copy_one_class_images_labels(path_to_images, path_to_labels, target_path, image_type='.png', label_suffix='-labels'):
    """
        copy images which contain only one class label
    Args:
        path_to_images: path to the images
        path_to_labels: path to the labels
        target_path: path to store the images/labels
        image_type: type of the images/labels (e.g. .jpg, .png)
        label_suffix: the suffix of the label names

    Returns:

    """
    # iterate through all files
    img_files = glob.glob(path_to_images + '/*' + image_type)

    target_path += '/one_class_images_labels/'
    one_class_img_dir =  target_path + '/images/'
    one_class_label_dir =  target_path + '/labels/'

    ensure_path_exists(one_class_img_dir)
    ensure_path_exists(one_class_label_dir)

    for img_file in img_files:
        img = os.path.basename(img_file)
        label_file = path_to_labels + img[:-4] + label_suffix + img[-4:]
        if is_one_class_label_image(label_file):
            shutil.copy(img_file, one_class_img_dir)
            shutil.copy(label_file, one_class_label_dir)


if __name__ == '__main__':
    from scripts.config import src_pth, trgt_pth

    # iterate through all files
    img_files = src_pth + '/one_class_images/images/'
    label_files = src_pth + '/one_class_images/labels/'

    copy_one_class_images_labels(img_files, label_files, trgt_pth, label_suffix='')