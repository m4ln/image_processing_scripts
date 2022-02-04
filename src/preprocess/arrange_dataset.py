#%% set all packages
import os
from sys import platform
import shutil
from PIL import Image
import numpy as np
import glob
import random


if __name__ == '__main__':
    
    # --- EDIT THESE VARIABLES ---
    # source directory
    src_dir = '/home/mr38/sds_hd/sd18a006/Marlen/datasets/stainNormalization/tumorLymphnode/patches/tumor/H.21.6011_2.3_HE.vmic/165/'
    #output directory
    out_dir =  '/home/mr38/sds_hd/sd18a006/Marlen/datasets/stainNormalization/tumorLymphnode/train/tumor/'
    # number of images to copy
    num_images = 900
    # list of all files 
    allFileNames = glob.glob(src_dir + '/*.png')
    # --- END OF EDIT ---

    # prepare output directory
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    
    if len(allFileNames) > num_images:
        # randomize the list of files
        allFileNames = random.sample(allFileNames, num_images)
        
    # Copy-pasting images
    for file in allFileNames:
        shutil.copy(file, out_dir)

    print('Done copying '+ str(len(allFileNames)) + ' images')
