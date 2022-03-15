import cv2


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


if __name__ == '__main__':
    from scripts.config import source_path, target_path

    img_gray = rgb2gray(source_path + '/mix#1.png')
    cv2.imwrite(target_path + '/img_gray.png', img_gray)
