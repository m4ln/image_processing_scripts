
#%% get the images
import glob
input_path = "/home/cw9/sds_hd/sd19g003/databaseSegmentation/AnnotatedNiklas"
img_list = sorted(glob.glob(input_path + '/*.jpg'))
label_list = sorted(glob.glob(input_path + '/*.png'))

#%% load a model
import torch
save_path = "/home/cw9/sds_hd/sd19g003/TrainedModels"
model2test = torch.load(save_path + '/UNet_pretrained.pt')

#%%
norm_func = lambda im : (im - [0.485, 0.456, 0.406]) / [0.229, 0.224, 0.225]

from ModelEvaluationTools import model_test
model_test(model2test = model2test, input_image = img_list[1], visIt = True, norm_func = norm_func)

from ModelEvaluationTools import model_validate
_,_, df = model_validate(input_image = img_list[1], label_exp = label_list[1], model2test = model2test,
                im_size = 1024, norm_func = norm_func,
                useCuda = True, metric = "all", vis_it = True)

#%% iterate over several models
model_list = ["UNet_pretrained.pt",
              "UNet_unpretrained.pt"]

from ModelEvaluationTools import validate_batch
import torch
import pandas as pd

for i_model in range(0, len(model_list)):

    #%% load the model
    model2test = torch.load(save_path + '/' + model_list[i_model])

    #%% do it
    df_t = validate_batch(img_list, label_list, model2test,
                        norm_func = None, metric = "all",
                        useCuda = True, visIt = False)

    #%% mount it
    df_t['model'] = model_list[i_model]
    if i_model ==0:
        df = df_t
    else:
        df = pd.concat((df, df_t), axis = 0)