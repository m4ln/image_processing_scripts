import glob

import numpy as np
from PIL import Image

from util.ensure_path_exists import ensure_path_exists


def image_to_npy(image_path):
    """convert image to numpy array.

    Args:
        image_path: path to the image

    Returns:
        a numpy array of the image
    """

    image = Image.open(image_path)
    return np.array(image)


def save_npy(npy_array, target_file_name):
    """save numpy array to a file.

    Args:
        npy_array: numpy array to save
        target_file_name: file to save the numpy array

    Returns
        None
    """
    np.save(target_file_name, npy_array)


def save_images_to_npy(path_to_images, image_type='.png'):
    """copy images which contain only one class label.

    Args:
        path_to_images: path to the images
        path_to_labels: path to the labels
        target_path: path to store the images/labels
        image_type: type of the images/labels (e.g. .jpg, .png)
        label_suffix: the suffix of the label names

    Returns:
        None
    """

    # iterate through all files
    img_files = glob.glob(path_to_images + '/*' + image_type)

    target_path = path_to_images + '/npy'

    ensure_path_exists(target_path)

    for image_file in img_files:
        image_npy = image_to_npy(image_file)
        save_npy(image_npy, image_file.replace(image_type, '.npy'))


if __name__ == '__main__':
    save_images_to_npy('../data/one_class_images/labels', '.png')
