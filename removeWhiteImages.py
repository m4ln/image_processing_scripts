
def rgb2gray(rgb):
    rgb = np.array(rgb)
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray

def check4white(gray, tresh_value = 0.5):
    mask = gray > 220
    if sum(sum(mask)) > tresh_value * len(mask) * len(mask):
        all_white = True
    else:
        all_white = False

    return (all_white)

import os
import glob
from PIL import Image
import numpy as np

if __name__ == '__main__':
    # ubuntu
    # src = '/home/mr38/sds_hd/sd18a006/Marlen/datasets/beauty-and-beast/train_test_sets/test_FID/H.18.4262_only-E.vmic/size512_overlap256/'
    # win
    src = 'Z:/Marlen/datasets/beauty-and-beast/train_test_sets/test_FID/H.18.4262_only-H.vmic/size512_overlap256'
    allFileNames = glob.glob(src + '/*.tif')

    for ifile in allFileNames:
        if os.path.isfile(ifile) == False:
            continue
        try: # bad style, I know
            img = Image.open(ifile)
            img = img.resize([500,500])
        except:
            print('error override')
            continue

        all_white = check4white(rgb2gray(img), 0.8)

        if all_white:
            print('removing: ' + ifile)
            os.remove(ifile) 

    print('Done')
