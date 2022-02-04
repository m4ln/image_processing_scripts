def testmodel(input_image, label_exp, model2test, args):

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
        input_image = cv2.resize(input_image, dsize=(args.imSize, args.imSize), interpolation=cv2.INTER_CUBIC)
        input_image = input_image.astype('float32')/255
        input_image = (input_image - [0.485, 0.456, 0.406]) / [0.229, 0.224, 0.225]

        label_exp = Image.open(label_exp)
        label_exp = np.int64(np.array(label_exp))
        label_exp = cv2.resize(label_exp, dsize=(args.imSize, args.imSize), interpolation=cv2.INTER_NEAREST)
        label_exp = torch.from_numpy(np.array(label_exp)).type(torch.long)  # torch.from_numpy .type(torch.long)

        # %% adapt it for the model
        data = torch.from_numpy(np.array([input_image.transpose((2, 0, 1))]))
        data = data.float()

    else:
        data = input_image

    #%% use the model
    if args.useCuda:
        model2test.cuda()
        data = data.cuda()
    else:
        model2test.cpu()
        data = data.cpu()

    model2test.eval()
    if args.model2use == 'UNet' or args.model2use == 'Kanezaki':
        test = model2test(data)
    else:
        test = model2test(data)['out']

    label_pred = test
    print(str(label_pred.shape))
    _, label_pred = torch.max(test.cpu(), 1)
    label_pred = label_pred.squeeze()

    #%% calculate the error
    from segmentation_metrics import dice
    dice_error = dice.dice_coef(label_exp, label_pred)
    print('dice coefficient = ' + str(dice_error))

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
    label_exp = tensor2numpy(label_exp)

    #%% print the results
    print('classes in the truth label')
    print(str(np.unique(label_exp)))
    print('classes in the predicted label')
    print(str(np.unique(label_pred)))

    #%% plot it
    if data.shape[0] == 1:
        plt.figure(1)
        plt.subplot(131)
        plt.title('input')
        plt.imshow(input_data)
        plt.subplot(132)
        plt.imshow(label_exp)
        plt.title('target')
        plt.subplot(133)
        plt.imshow(label_pred)
        plt.title('prediction')
    else:
        plt.figure(1)
        plt.subplot(311)
        plt.title('input')
        plt.imshow(input_data)
        plt.subplot(312)
        plt.imshow(label_exp)
        plt.title('target')
        plt.subplot(313)
        plt.imshow(label_pred)
        plt.title('prediction')

    plt.show()

    #%% return
    return label_exp, label_pred