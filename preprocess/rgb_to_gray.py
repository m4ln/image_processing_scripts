
import cv2

def rgb2gray(path_to_img):
    """
    converts rgb to grayscale image
    :param path_to_img: path to rgb image to be converted to grayscale
    :return: grayscale image
    """

    img_rgb = cv2.imread(path_to_img)
    r, g, b = img_rgb[:, :, 0], img_rgb[:, :, 1], img_rgb[:, :, 2]
    img_gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return img_gray


if __name__ == '__main__':
    from scripts.config import src_pth, trgt_pth

    img_gray = rgb2gray(src_pth + '/mix#1.png')
    cv2.imwrite(trgt_pth + '/img_gray.png', img_gray)
