
from PIL import Image

def isCorruptedImage(img_path):
    """
    checks if an image is corrupted/not readable
    :param img_path: path to the image
    :return: True, if image is corrupted, False otherwise
    """
    try:
        img = Image.open(img_path)  # open the image file
        img.verify()  # verify that it is, in fact an image
        return False
    except (IOError, SyntaxError):
        return True

if __name__ == '__main__':
    from scripts.config import src_pth

    print(isCorruptedImage(src_pth + '/white#1.png'))
