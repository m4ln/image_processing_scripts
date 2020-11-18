
#%% set all packages
import os
from sys import platform
import shutil
from PIL import Image
import numpy as np
import glob
import random


if __name__ == '__main__':
    # create dataset with non-neoplastic lung
    data_dir = '/home/mr38/sds_hd/sd18a006/Marlen/datasets/HE_H.18.4262/H.18.4262_only-H.vmic/512/'
    allFileNames = glob.glob(data_dir + '/*.tif')
    allFileNames = random.sample(allFileNames, len(allFileNames))

    #%% Creating Train / Val / Test folders (One time use)
    val_ratio = 0
    test_ratio = 0.2


    #% prepare the directories
    # train folder
    trainFolder = data_dir +'/train'
    if os.path.exists(trainFolder):
        shutil.rmtree(trainFolder)
    os.makedirs(trainFolder)
    # validation folder
    #valFolder = data_dir +'/val'
    #if os.path.exists(valFolder):
    #    shutil.rmtree(valFolder)
    #os.makedirs(data_dir +'/val')
    # test folder
    testFolder = data_dir +'/test'
    if os.path.exists(testFolder):
        shutil.rmtree(testFolder)
    os.makedirs(data_dir +'/test')

    #% prepare the data
    # Creating partitions of the data after shuffeling
    allFileNames = glob.glob(data_dir + '/*.tif')
    np.random.shuffle(allFileNames)
    #train_FileNames, val_FileNames, test_FileNames = np.split(np.array(allFileNames),
    #                                                            [int(len(allFileNames) * (1 - val_ratio + test_ratio)),
    #                                                            int(len(allFileNames) * (1 - test_ratio))])

    train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames) * (1 - test_ratio))])
    
    train_FileNames = [name for name in train_FileNames.tolist()]
    #val_FileNames = [name for name in val_FileNames.tolist()]
    test_FileNames = [name for name in test_FileNames.tolist()]

    print('Total images: ', len(allFileNames))
    print('Training: ', len(train_FileNames))
    #print('Validation: ', len(val_FileNames))
    print('Testing: ', len(test_FileNames))

    #% Copy-pasting images
    for name in train_FileNames:
        shutil.copy(name, data_dir + '/train')

    #for name in val_FileNames:
    #    shutil.copy(name, data_dir + '/val')

    for name in test_FileNames:
        shutil.copy(name, data_dir + '/test')

    #% counter section
    print('Done!')
