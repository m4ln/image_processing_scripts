import cv2

import config


def rgb2gray(path_to_image):
    """
    converts rgb to grayscale image

    Args:
        path_to_image: path to rgb image to be converted to grayscale

    Returns:
        grayscale image
    """

    img_rgb = cv2.imread(path_to_image)
    r, g, b = img_rgb[:, :, 0], img_rgb[:, :, 1], img_rgb[:, :, 2]
    img_gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return img_gray


def main():
    img_gray = rgb2gray(config.source_path + '/mix#1.png')
    cv2.imwrite(config.target_path + '/img_gray.png', img_gray)


if __name__ == '__main__':
    main()
