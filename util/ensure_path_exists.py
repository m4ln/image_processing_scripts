
import os
import shutil

def ensurePathExists(path, overwrite=True):
    """
    creates a new folder and/or clears existing folder
    :param path: path to the new folder
    :param overwrite: if True, overwrites content if folder already exists, otherwise keeps it
    :return:
    """
    if os.path.exists(path) and overwrite == True:
        print('folder cleared')
        shutil.rmtree(path)
    if not os.path.exists(path):
        print('folder created')
        os.makedirs(path)
