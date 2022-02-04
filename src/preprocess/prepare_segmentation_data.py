import glob
import shutil
from PIL import Image
from util.util import assure_path_exists
import os

dir = 'Z:/Marlen/datasets/segmentation/urothel/classes_123/TCGA-BT-A20W-01Z-00-DX1.26F73765-704B-4D81-923D-F20860A3EFFC/512/'
input_dir = dir + '*-labels.png'
output_images_dir = dir + 'trainA/'
output_labels_dir = dir + 'trainB/'
assure_path_exists(output_images_dir)
assure_path_exists(output_labels_dir)

remove_corrupted = True

if __name__ == '__main__':
    for label_file in glob.glob(input_dir):
         try:
           label = Image.open(label_file) # open the label file
           image_file = label_file[:-11] + ".png"
           image = Image.open(image_file) # open the image file
           label.verify() # verify that it is, in fact an image
           image.verify() # verify that it is, in fact an image
           shutil.move(image_file, output_images_dir)
           shutil.move(label_file, output_labels_dir)
         except (IOError, SyntaxError) as e:
           print('Bad file:', label_file) # print out the names of corrupt files
           if remove_corrupted:
               print('removing...')
               try:
                   os.remove(label_file)
                   os.remove(image_file)
               except Exception:
                   continue




