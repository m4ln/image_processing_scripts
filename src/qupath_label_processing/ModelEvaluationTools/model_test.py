def model_test(
        input_image, model2test,
        im_size = 1024, norm_func = None,
        useCuda = True, visIt = False,
        label2rgb = False
        ):

    #%% set the background
    import torch
    import numpy as np
    import cv2
    import matplotlib.pyplot as plt
    from PIL import Image

    #%% import the images
    if isinstance(input_image, str):

        # %% import the images
        input_image = Image.open(input_image)
        input_image = np.array(input_image)
        input_image = cv2.resize(input_image, dsize=(im_size, im_size), interpolation=cv2.INTER_CUBIC)
        input_image = input_image.astype('float32')/255
        if callable(norm_func):
            input_image = norm_func(input_image)

        # %% adapt it for the model
        data = torch.from_numpy(np.array([input_image.transpose((2, 0, 1))]))
        data = data.float()

    else:
        if callable(norm_func):
            data = norm_func(input_image)
        else:
            data = input_image

    #%% use the model
    if useCuda:
        model2test.cuda()
        data = data.cuda()
    else:
        model2test.cpu()
        data = data.cpu()

    model2test.eval()
    test = model2test(data)

    label_pred = test
    print(str(label_pred.shape))
    _, label_pred = torch.max(test.cpu(), 1)
    label_pred = label_pred.squeeze()

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

    #%% transform to numpy
    input_data = tensor2numpy(data)
    label_pred = tensor2numpy(label_pred)

    #%% transform the output to an rgb-image (if not already)
    if label2rgb:
        label_colours = np.random.randint(255,size=(label_pred.shape[1],3))
        label_pred = np.array([label_colours[c % 100] for c in label_pred])

    #%% show the results
    if visIt:
        from ModelEvaluationTools import vislabel
        plt.figure(1)
        plt.subplot(121)
        plt.title('input')
        plt.imshow(input_data)
        plt.subplot(122)
        if label2rgb:
            plt.imshow(label_pred)
        else:
            n_label = np.max(label_pred) + 1
            vislabel(label_pred, n_label=n_label)
        plt.title('output')
        plt.tight_layout()
        plt.show()

    #%% return
    return input_data, label_pred