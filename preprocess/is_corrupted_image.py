from PIL import Image


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


if __name__ == '__main__':
    from scripts.config import source_path

    print(is_corrupted_image(source_path + '/white#1.png'))
