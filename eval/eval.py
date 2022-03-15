# TODO test these function

import cv2
import numpy as np
from matplotlib import pyplot as plt
# from sklearn.feature_extraction import image
# import matplotlib.image as matlabimg
# from scipy.misc import imread
# from skimage import io, data, img_as_float
# from skimage.measure import compare_ssim as ssim
from skimage.metrics import structural_similarity


def create_histogram(path_to_image, target_path=''):
    """
    creates a histogram of a given image and either shows or saves a plot

    Args:
        path_to_image: path to the image
        target_path: if given, saves a plot, otherwise (if empty) shows the plot

    Returns:
        the histogram plot
    """

    image = cv2.imread(path_to_image)

    depth = image.shape[2]
    for z in range(depth):
        im = image[:, :, z]
        mi = im.min()
        ma = im.max()
        if mi < 0 or ma > 255:
            print("range error: min=" + str(mi) + " max=" + ma)
            exit()

        # V1
        # plt.hist(im.ravel(), 256, [0, 256])

        # V2
        # calculate mean value from RGB channels and flatten to 1D array
        vals = im.flatten()
        # plot histogram with 255 bins
        # b, bins, patches = plt.hist(vals, 255, stacked=True, density=True)

        counts, bins = np.histogram(vals, 255)
        counts = (counts - min(counts)) / (max(counts) - min(counts))
        plt.hist(bins[:-1], bins, weights=counts)

        plt.xlim([0, 255])
        # plt.show()
        #
    plt.title(path_to_image)
    plt.xlabel('pixel value')
    plt.ylabel('count')

    if target_path == '':
        plt.show()
    else:
        plt.savefig(target_path + 'histo')

    plt.clf()

    return plt


def calculate_mse(path_to_image_1, path_to_image_2):
    """
    computes the 'Mean Squared Error' (MSE) between two images as the sum of
    the squared difference between them NOTE: the two images must have the
    same dimension

    Args:
        path_to_image_1: path to the first image
        path_to_image_2: path to the second image

    Returns:
        the MSE, the lower the error, the more "similar" the two images are
    """

    image_1 = cv2.imread(path_to_image_1)
    image_2 = cv2.imread(path_to_image_2)

    mse = np.sum((image_1.astype("float") - image_2.astype("float")) ** 2)
    mse /= float(image_1.shape[0] * image_1.shape[1])

    return mse


def calculate_ssim(path_to_image_1, path_to_image_2):
    """
    computes the 'Structural Similarity Index' (SSIM) between two images

    Args:
        path_to_image_1: path to the first image
        path_to_image_2: path to the second image

    Returns:
        the SSIM value

    """
    image_1 = cv2.imread(path_to_image_1)
    image_2 = cv2.imread(path_to_image_2)

    ssim = structural_similarity(image_1, image_2, gradient=False,
                                 channel_axis=2)

    return ssim


if __name__ == "__main__":
    from scripts.config import source_path, target_path

    path_to_image_1 = source_path + '/mix#1.png'
    path_to_image_2 = source_path + '/mix#2.png'

    # save histogram
    create_histogram(path_to_image_1, target_path)

    # calculate MSE and print
    mse = calculate_mse(path_to_image_1, path_to_image_2)
    print(mse)

    # calculate SSIM and print
    ssim = calculate_ssim(path_to_image_1, path_to_image_2)
    print(ssim)
