# this function reads all numpy files in a directory and prints the occurring
# classes with the percentage in each numpy into a text file and stores it in
# the same folder as the numpy files are stored in
import glob

import numpy as np


def get_unique_label_in_array(numpy_array):
    classdict = {
        0: "Tumor",  # blue
        1: "Bladder Wall",  # green
        2: "Perivascular Fat",  # yellow
        3: "Background",
        255: "Background",
        86: "",  # random vaule if less classes in one image than expected
        85: ""  # random vaule if less classes in one image than expected

    }

    # get number of pixels
    pixel_count = numpy_array.shape[0] * numpy_array.shape[1]

    # get unique labels
    unique, counts = np.unique(numpy_array, return_counts=True)

    # finds the percentages of each class
    background_percent = counts[unique == 255]
    if background_percent.size == 0:
        background_percent = 0.0
    elif background_percent.size > 0:
        background_percent = background_percent[0]
    background_percent = np.around(background_percent / pixel_count, decimals=1)

    tumor_percent = counts[unique == 0]
    if tumor_percent.size == 0:
        tumor_percent = 0.0
    elif tumor_percent.size > 0:
        tumor_percent = tumor_percent[0]
    tumor_percent = np.around(tumor_percent / pixel_count, decimals=1)

    bladderwall_percent = counts[unique == 1]
    if bladderwall_percent.size == 0:
        bladderwall_percent = 0.0
    elif bladderwall_percent.size > 0:
        bladderwall_percent = bladderwall_percent[0]
    bladderwall_percent = np.around(bladderwall_percent / pixel_count,
                                    decimals=1)

    fat_percent = counts[unique == 2]
    if fat_percent.size == 0:
        fat_percent = 0.0
    elif fat_percent.size > 0:
        fat_percent = fat_percent[0]
    fat_percent = np.around(fat_percent / pixel_count, decimals=1)

    return background_percent, tumor_percent, \
           bladderwall_percent, fat_percent


def count_classes(path_to_numpy_files):
    # iterate through all files
    numpy_files = glob.glob(path_to_numpy_files + '/*.npy')

    header = ['file', 'background', 'tumor', 'bladder_wall', 'perivascular_fat']

    # open csv file
    with open(path_to_numpy_files + '/count_classes.csv', 'w') as f:
        f.write(';'.join(header) + '\n')

        for numpy_file in numpy_files:
            # read numpy file
            numpy_array = np.load(numpy_file)

            # get unique labels
            background_percent, tumor_percent, bladderwall_percent, \
            fat_percent = get_unique_label_in_array(numpy_array)

            data = [numpy_file, background_percent, tumor_percent, bladderwall_percent, fat_percent]

            # write to csv file
            f.write(';'.join(str(x) for x in data) + '\n')


if __name__ == '__main__':
    count_classes('D:/projects/masterproject_valentin_barth/data'
                       '/classes_123/Output/val')
