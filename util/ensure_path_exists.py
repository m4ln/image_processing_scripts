import os
import shutil


def ensure_path_exists(path, overwrite=True):
    """
    creates a new folder and/or clears existing folder

    Args:
        path: path to the new folder
        overwrite: if True, overwrites content if folder already exists

    Returns:
        None
    """

    if os.path.exists(path) and overwrite:
        print('folder cleared')
        shutil.rmtree(path)
    if not os.path.exists(path):
        print('folder created')
        os.makedirs(path)
