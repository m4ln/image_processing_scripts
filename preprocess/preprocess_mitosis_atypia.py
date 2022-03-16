import math
import os

import cv2

from preprocess.resize_image import resize_image
from util.ensure_path_exists import ensure_path_exists

if __name__ == '__main__':
    # width and height for image resizing
    new_size_x = 1024
    new_size_y = 1024
    # tile and offset size, if offset size is same as tile size, the tiles
    # are non-overlapping, if smaller, they are overlapping, if bigger,
    # some pixels are skipped
    tile = 256
    offs = 256  # int(tile - tile / 2)
    tile_size = (tile, tile)
    offset = (offs, offs)
    # path to input
    input_dir = "/home/marlen/resizeImages/A"
    # path to output
    output_dir = input_dir + "_tiles_" + str(256) + "_offset_" + str(offs) + "/"
    print(output_dir)
    ensure_path_exists(output_dir)

    # go through each image in directory
    for filename in os.listdir(input_dir):
        # read image
        img = cv2.imread(os.path.join(input_dir, filename))
        # resize image
        img_resized = resize_image(img, new_size_x, new_size_y)
        # extract tiles
        img_shape = img_resized.shape

        for i in range(int(math.ceil(img_shape[0] / (offset[1] * 1.0)))):
            for j in range(int(math.ceil(img_shape[1] / (offset[0] * 1.0)))):
                cropped_img = img[
                              offset[1] * i:min(offset[1] * i + tile_size[1],
                                                img_shape[0]),
                              offset[0] * j:min(offset[0] * j + tile_size[0],
                                                img_shape[1])]
                # Debugging the tiles
                cv2.imwrite(
                    output_dir + filename[:-5] + "tile_" + str(i) + "_" + str(
                        j) + ".tiff", cropped_img)
