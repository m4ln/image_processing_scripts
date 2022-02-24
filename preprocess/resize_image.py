
import cv2

def resize_image(path_to_image, new_width, new_height):
    """
    resizes an image

    Args:
        path_to_image: path to the image
        new_width: new width of the image
        new_height: new height of the image

    Returns:
        resized image
    """

    img_resized = cv2.imread(path_to_image)
    img_resized = cv2.resize(img_resized, dsize=(new_width, new_height))

    return img_resized

if __name__ == '__main__':
    from scripts.config import src_pth, trgt_pth

    img_resized = resize_image(src_pth + '/mix#1.png', 64, 64)
    cv2.imwrite(trgt_pth + '/img_resized.png', img_resized)
