"""Script to convert label images from rgb to single index.

This script was copied and altered from Erdi Duezel.

"""

# todo finish docu and generalize this script more regarding directories

import glob

import numpy as np
from PIL import Image

from util import ensure_path_exists


def rgb2index(path_to_label_images, path_to_color_palette, target_path):
    """Converts an RGB label image to indexed image.

    An RGB image is converted to indexed image using a given colorpalette.
    The colorpalettte needs to be a comma seperated csv file containing an
    rgb value in each row for each class.

    E.g.
    colorpalette.csv contains the following RGB values
        26, 0, 104
        26, 77, 26
        153, 102, 0

    Then the function sets the index values as follows:
        0
        1
        2

    Args:
        path_to_label_images: path to the input images with the image type at
        the end, e.g /*.png
        path_to_color_palette: path to the color palette file as comma
        seperated csv file
        target_path:

    Returns:

    """
    files = glob.glob(path_to_label_images)

    # what classes we expect to have in the data, here we have only 2 classes
    # but we could add additional classes and/or specify an index from which we
    # would like to ignore
    classes = [0, 1, 2]

    palette = np.loadtxt(path_to_color_palette, delimiter=',')

    ensure_path_exists.ensure_path_exists(target_path, False)

    for file in files:
        image = Image.open(file)
        image_rgb = np.asarray(image.convert('RGB'))
        idx = np.uint8(np.zeros((image.height, image.width)))
        output = np.uint8(np.zeros((image.height, image.width)))
        label = [0, 0, 0]
        idx = idx + 255 * np.all(image_rgb == label, axis=2,
                                 out=output)  # 0 to 255
        # converting indexes so they are equal for one class for the whole
        # dataset
        for i in classes:
            label = palette[i]
            idx = idx + i * np.all(image_rgb == label, axis=2, out=output)
        idx = np.uint8(idx)
        # io = np.repeat(idx[:, :, np.newaxis], 3, axis=2)
        # due to later transformations we need 3 layers
        # interp_method = PIL.Image.NEAREST
        # want to use nearest! otherwise resizing may cause non-existing classes
        # to be produced via interpolation (e.g., ".25")
        # give visual output to controll function
        # image.show()
        aim_mask = Image.fromarray(idx, mode='P')
        aim_mask.putpalette(palette)
        aim_mask.save(file.replace('.png', 'IDX3classes.png'))


def main():
    source_path = 'D:/projects/masterproject_valentin_barth/data/classes_123' \
                  '/Output/orig3/*.png'
    path_color_palette = 'D:/projects/masterproject_valentin_barth/data' \
                         '/palette.csv'
    target_path = 'D:/projects/masterproject_valentin_barth/data/classes_123' \
                  '/Output/orig_rgb2index'
    rgb2index(source_path, path_color_palette, target_path)


if __name__ == '__main__':
    main()
