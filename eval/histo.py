import matplotlib.pyplot as plt
import cv2
import numpy as np

def createHistogram(img_path, target_path=''):
    """
    creates a histogram of a given image and either shows or saves a plot
    :param img_path: path to the image
    :param target_path: if given, saves a plot, otherwise (if empty) shows the plot
    :return: histogram plot
    """
    img = cv2.imread(img_path)

    depth = img.shape[2]
    for z in range(depth):
        im = img[:,:,z]
        mi = im.min()
        ma = im.max()
        if mi < 0 or ma > 255:
            print("range error: min=" + str(mi) + " max=" + ma )
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
    plt.title(img_path)
    plt.xlabel('pixel value')
    plt.ylabel('count')

    if target_path == '':
        plt.show()
    else:
        plt.savefig(target_path + 'histo')

    plt.clf()

    return plt

if __name__ == '__main__':
    from scripts.config import src_pth, trgt_pth
    createHistogram(src_pth + '/mix#1.png', trgt_pth)