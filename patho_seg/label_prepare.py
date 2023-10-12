# %% function to load and prepare the palette
# simple table adaption

import os
import random
import shutil

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
from numpy import loadtxt
from numpy import savetxt


def loadandprepare(legendPath="LabelLegend.xls", name_palette="palette"):
    # %% load and adapt it
    lookuptable = pd.read_excel(legendPath)
    rgbvalues = np.array([lookuptable.iloc[:, 4], lookuptable.iloc[:, 5],
                          lookuptable.iloc[:, 6]])
    palette = np.transpose(rgbvalues)

    # %% save it
    savetxt(name_palette + '.csv', palette, delimiter=',')

    return palette, lookuptable


# %% function to create a palette on basis of an image set
# cave: does not work properly

def createpalette(img_list, stop_iteration):
    # %% get the look up table
    lookuptable = pd.read_excel("LabelLegend.xls")
    rgbvalues = np.array([lookuptable.iloc[:, 5], lookuptable.iloc[:, 4],
                          lookuptable.iloc[:, 3]])
    rgbvalues = np.transpose(rgbvalues)

    # %%
    img_list = random.sample(img_list, len(img_list))
    if (stop_iteration != float('Inf')):
        img_list = img_list[0:stop_iteration]

    for i in range(len(img_list)):

        imgLink = Image.open(img_list[i])
        img = np.array(imgLink)

        # case for labeled image (the issue is, that qupath
        if len(img.shape) == 2:
            # get the used palette and reshape it
            t_palette = np.unique(im2.reshape(-1, im2.shape[2]), axis=0)

            palette_vector = imgLink.getpalette()
            t_palette = np.reshape(palette_vector, (-1, 3))

            idx = np.unique(img)
            t_palette = t_palette[idx]

        elif len(img.shape) == 3:
            img = np.reshape(img, (-1, 3))
            t_palette = np.unique(img, axis=0)

        # print(t_palette)
        if i == 0:
            palette = t_palette
        else:
            palette = np.concatenate((palette, t_palette), axis=0)

        print('label #', i + 1, ' added')

    # Perform lex sort and get sorted data
    sorted_idx = np.lexsort(palette.T)
    sorted_data = palette[sorted_idx, :]

    # Get unique row mask
    row_mask = np.append([True], np.any(np.diff(sorted_data, axis=0), 1))

    # Get unique rows
    palette = sorted_data[row_mask]
    palette = palette[palette[:, 0].argsort()]

    # %%
    savetxt('palette.csv', palette, delimiter=',')

    return palette


# %% function to convert the rgb-images on basis of a palette to a label-image
# simple loop that compares rgb-values to a table

def rgb2index(label_path, palette, vis=False):
    # %% load the label image
    label_img = Image.open(label_path)

    # %% load the palette
    if type(palette) == str:
        palette = loadtxt('palette.csv', delimiter=',')

    # %% iterate over the palette
    label_rgb = np.asarray(label_img.convert('RGB'))
    x = int(label_rgb.shape[0] / 1)
    y = int(label_rgb.shape[1] / 1)

    label_mask = np.uint8(np.zeros((x, y)))
    output = np.uint8(np.zeros((x, y)))

    nlabel = 1
    for i in range(palette.shape[0]):
        label = palette[i]
        BooleanArr = np.all(label_rgb == label, axis=2, out=output)
        # label_mask = label_mask + (i+1) * BooleanArr
        label_mask[BooleanArr == 1] = i + 1

    # %% plot it (if vis == True)
    x = label_rgb.shape[0]
    y = label_rgb.shape[1]
    label_img = np.array(label_img)

    if vis:
        from model_training.ModelEvaluationTools import vislabel

        plt.figure(1)
        plt.subplot(121)
        plt.imshow(label_rgb)
        plt.title('input image')
        plt.subplot(122)
        vislabel(label_mask, n_label=20)
        plt.title('output image')
        plt.show()
        plt.pause(0.5)

    # %% output-section
    return (label_mask)


# %% old function -> ignore it
def only_rgb2index(list_images, list_labels, path_data):
    # %% create the folders
    path_input = path_data + '/input'
    if os.path.exists(path_input):
        shutil.rmtree(path_input)
    os.makedirs(path_input)
    path_output = path_data + '/output'
    if os.path.exists(path_output):
        shutil.rmtree(path_output)
    os.makedirs(path_output)

    # %% load the palette
    palette = loadtxt('palette.csv', delimiter=',')
    palette = palette.astype('int32')
    n_label = list(range(0, palette.shape[0]))

    # %% iterate over all images
    i_image = 0
    n_iterations = len(list_images) - 1

    for idx in range(0, len(list_images)):

        # %% load and save the image and the label
        lab = rgb2index(list_labels[idx], palette, True)

        if idx == 0:
            label_values = np.unique(lab)
        else:
            label_values = np.concatenate((label_values, np.unique(lab)), 0)

        # lab = Image.fromarray(lab, mode='L')
        # lab.save(path_output + '/label#' + str(i_image) + '.jpg', mode='L')
        cv2.imwrite(path_output + '/label#' + str(i_image) + '.png', lab)
        im = Image.open(list_images[idx])
        im.save(path_input + '/tile#' + str(i_image) + '.jpg')

        print('iteration #' + str(i_image) + ' from n=' + str(n_iterations))
        i_image += 1

    print("These labels where created: ")
    print(np.unique(label_values))

    return
