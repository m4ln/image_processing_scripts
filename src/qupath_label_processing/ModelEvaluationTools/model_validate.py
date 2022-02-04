def model_validate(
        input_image, label_exp, model2test,
        im_size = 1024, norm_func = None,
        useCuda = True, metric = None, vis_it = True
        ):

    #%% set the background
    import torch
    import numpy as np
    import cv2
    import matplotlib.pyplot as plt
    from PIL import Image

    #%% analyse the input image
    from . import model_test
    input_data, label_pred = model_test(input_image, model2test,
                                        im_size=im_size, useCuda=useCuda,
                                         norm_func = norm_func)

    #%% import the label
    if isinstance(label_exp, str):

        # %% import the images
        label_exp = Image.open(label_exp)
        label_exp = np.array(label_exp)

    label_exp = cv2.resize(label_exp, dsize=(im_size, im_size), interpolation=cv2.INTER_NEAREST)
    label_exp = np.int64(label_exp)

    #%% calculate the error
    from ModelEvaluationTools import model_metrics

    if metric is not None:
        assesment_segmentation =  model_metrics(label_exp = label_exp,
                                                label_pred = label_pred,
                                                metric = metric)
    else:
        assesment_segmentation = None

    #%% define transformation function
    def tensor2numpy(tensor_array):

        tensor_array = tensor_array.cpu()
        numpy_array = tensor_array.numpy()

        # all cases with batch-size > 1
        if (not (numpy_array.shape[0] == 1)) and (not (len(numpy_array.shape) == 2)):

            if len(numpy_array.shape) == 3:
                numpy_array = np.transpose(numpy_array, (1,2,0))
                numpy_array = [numpy_array[:, :, c] for c in range(numpy_array.shape[2])]
            else:
                numpy_array = np.transpose(numpy_array, (2, 3, 1, 0))
                numpy_array = [numpy_array[:, :, :, c] for c in range(numpy_array.shape[3])]

            numpy_array = np.concatenate(numpy_array,1)
        # batch-size == 1
        else:
            numpy_array = np.squeeze(numpy_array)
            if len(numpy_array.shape) > 2:
                numpy_array =np.transpose(numpy_array, (1, 2, 0))

        return numpy_array

    #%% print the results
    print('classes in the truth label')
    print(str(np.unique(label_exp)))
    print('classes in the predicted label')
    print(str(np.unique(label_pred)))

    #%% plot it
    if vis_it:
        from ModelEvaluationTools import vislabel
        plt.figure(1)
        plt.subplot(131)
        plt.title('input')
        plt.imshow(input_data)
        plt.subplot(132)
        vislabel(label_exp)
        plt.title('target')
        plt.subplot(133)
        vislabel(label_pred)
        plt.title('prediction')
        plt.tight_layout()
        plt.show()

    #%% return
    return label_exp, label_pred, assesment_segmentation