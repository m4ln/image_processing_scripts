
import cv2

def resizeImage(img_path, new_width, new_height):
    """
    resizes an image
    :param img_path: path to the image
    :param new_width: new width of the image
    :param new_height: new height of the image
    :return: resized image
    """
    img_resized = cv2.imread(img_path)
    img_resized = cv2.resize(img_resized, dsize=(new_width, new_height))

    return img_resized

if __name__ == '__main__':
    from scripts.config import src_pth, trgt_pth

    img_resized = resizeImage(src_pth + '/mix#1.png', 64, 64)
    cv2.imwrite(trgt_pth + '/img_resized.png', img_resized)
