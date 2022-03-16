from PIL import Image

import config


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


def main():
    print(is_corrupted_image(config.source_path + '/white#1.png'))


if __name__ == '__main__':
    main()
