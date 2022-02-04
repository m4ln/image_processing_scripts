
#%% set all packages
import os
from sys import platform
import shutil
from PIL import Image
import numpy as np
import glob
import random


#%% get the sds-path
if platform == "linux":
    input_dir = '/home/mr38/sds_hd/sd18a006/Marlen/datasets/HE_H.18.4262/
elif platform == "win32":
    input_dir = 'Z:/Marlen/project_data/pytorch-cycleGan-stain-normalization/camelyon16classification/trainImages/trainA'


#%% create dataset with non-neoplastic lung
allFileNames = glob.glob(input_dir + '/*.png')
# allFileNames = random.sample(allFileNames, len(allFileNames))

root_dir = sds_path + '/trainingSet'
lung_folder = root_dir + '/tissue'
if os.path.exists(lung_folder):
    shutil.rmtree(lung_folder)
os.makedirs(lung_folder)

# now iterate over the images
n_lung, n_ws = 1,1
for ifile in allFileNames:

    if os.path.isfile(ifile) == False:
        continue
    try: # bad style, I know
        img = Image.open(ifile)
        img = img.resize([500,500])
    except:
        print('error override')
        continue

    all_white = isWhiteImage(rgb2gray(img), 0.8)

    if !all_white:
        #if n_lung > n_max_tiles_per_class :
        #    continue
        img.save(lung_folder + '/tile#' + str(n_lung) + '.tif')
        print('tile #' + str(n_lung) + ' added in folder "Lung"')
        n_lung += 1
    # else:
    #     #if n_ws > n_max_tiles_per_class:
    #     #   continue
    #     img.save(ws_folder + '/tile#' + str(n_ws) + '.tif')
    #     print('tile #' + str(n_ws) + ' added in folder "WS"')
    #     n_ws += 1

    #if n_lung > n_max_tiles_per_class  and n_ws > n_max_tiles_per_class:
    #    break

print('Finally n = ' + str(n_lung-1) + ' lung images and n = ' + str(n_ws-1) + ' white space images are added')
"""
#%% create dataset with other tissues than lung (liver, thymus)
src = sds_path + '/DataAdenoCarcinomaLung/Scans_NSCLC_Vollschnitte/Segmetierung/exported_tiles_otherTissue'
allFileNames = glob.glob(src + '/*.tif')
allFileNames = random.sample(allFileNames, len(allFileNames))

root_dir = sds_path + '/DataBase'
ot_folder = root_dir + '/OT'
if os.path.exists(ot_folder):
    shutil.rmtree(ot_folder)
os.makedirs(ot_folder)

# now iterate over the images
n_ot = 1
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

    if all_white == False:
        if n_ot > n_max_tiles_per_class:
            continue
        img.save(ot_folder + '/tile#' + str(n_ot) + '.tif')
        print('tile #' + str(n_ot) + ' added in folder "OT"')
        n_ot += 1

    if n_ot > n_max_tiles_per_class:
        break

print('Finally n = ' + str(n_ot-1) + ' other tissue images are added')
"""
#%% Creating Train / Val / Test folders (One time use)
classes_dir = ['tissue',
               '/whiteSpace']
val_ratio = 0.15
test_ratio = 0.05

#%% iterate over it
for cls in classes_dir:

    #% counter section
    print('folder ' + cls + ' started')

    #% prepare the directories
    # train folder
    trainFolder = root_dir +'/train' + cls
    if os.path.exists(trainFolder):
        shutil.rmtree(trainFolder)
    os.makedirs(trainFolder)
    # validation folder
    valFolder = root_dir +'/val' + cls
    if os.path.exists(valFolder):
        shutil.rmtree(valFolder)
    os.makedirs(root_dir +'/val' + cls)
    # test folder
    testFolder = root_dir +'/test' + cls
    if os.path.exists(testFolder):
        shutil.rmtree(testFolder)
    os.makedirs(root_dir +'/test' + cls)

    #% prepare the data
    # Creating partitions of the data after shuffeling
    input_dir = root_dir + cls  # Folder to copy images from

    allFileNames = glob.glob(input_dir + '/*.tif')
    np.random.shuffle(allFileNames)
    train_FileNames, val_FileNames, test_FileNames = np.split(np.array(allFileNames),
                                                              [int(len(allFileNames) * (1 - val_ratio + test_ratio)),
                                                               int(len(allFileNames) * (1 - test_ratio))])

    train_FileNames = [name for name in train_FileNames.tolist()]
    val_FileNames = [name for name in val_FileNames.tolist()]
    test_FileNames = [name for name in test_FileNames.tolist()]

    print('Total images: ', len(allFileNames))
    print('Training: ', len(train_FileNames))
    print('Validation: ', len(val_FileNames))
    print('Testing: ', len(test_FileNames))

    #% Copy-pasting images
    for name in train_FileNames:
        shutil.copy(name, root_dir + '/train' + cls)

    for name in val_FileNames:
        shutil.copy(name, root_dir + '/val' + cls)

    for name in test_FileNames:
        shutil.copy(name, root_dir + '/test' + cls)

    #% counter section
    print('folder ' + cls + ' finished')
