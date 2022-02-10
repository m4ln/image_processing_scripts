
from sys import platform

def getSdsPath():
    """
    get the sds path based on the operating system
    :return: sds path if os is win or linux, otherwise error
    """
    if platform == "linux":
        sds_path = '/sds_hd/sd18a006/'
    elif platform == "win32":
        sds_path = "//lsdf02.urz.uni-heidelberg.de/sd18A006/"
    else:
        print('error: sds path cannot be defined!')
        sds_path = ""

    return sds_path