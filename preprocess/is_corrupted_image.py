from PIL import Image

#import config


def is_corrupted_image(path_to_image):
    """
    checks if an image is corrupted/not readable

    Args:
        path_to_image: path to the image

    Returns:
        True, if image is corrupted, False otherwise
    """

    try:
        img = Image.open(path_to_image)  # open the image file
        img.verify()  # verify that it is, in fact an image
        return False
    except (IOError, SyntaxError):
        return True


def main(path_to_images):
    """
    checks if all images in a folder are corrupted/not readable and deletes them

    Args:
        path_to_images: path to the folder containing the images

    Returns:
        None
    """

    import os
    import glob

    print('number of images: ' + str(len(os.listdir(path_to_images))))

    for filename in glob.glob(os.path.join(path_to_images, '*.png')):
        if is_corrupted_image(filename):
            print('corrupted image: ' + filename)
            os.remove(filename)


if __name__ == '__main__':
    path_to_images = '/home/mr38/sds_hd/sd18a006/marlen/histoNorm/urothel/data/trainB/'
    main(path_to_images)
