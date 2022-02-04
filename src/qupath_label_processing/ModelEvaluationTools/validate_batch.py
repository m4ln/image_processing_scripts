
def validate_batch(img_list, label_list, model2test,
                norm_func = None, metric = "all",
                useCuda = True, visIt = False):

    #%% import-section
    from ModelEvaluationTools import model_validate
    import pandas as pd
    from ModelEvaluationTools import get_file_name

    #%% iterate over all images
    file_names = get_file_name(img_list)

    for idx in range(0, len(img_list)):

        #%% validate the model
        _, _, df_t = model_validate(input_image=img_list[idx], label_exp=label_list[1],
                                    model2test=model2test,
                                    im_size=1024, norm_func=norm_func,
                                    useCuda=True, metric=metric, vis_it=visIt)

        #%% mount the results in a pandas dataframe
        if idx == 0:
            df = df_t.transpose()
        else:
            df = df.append(df_t['Value'])

    #%% finalize the dataframe
    df = df.rename(columns=df.iloc[0])
    df = df.drop(df.index[0])
    df['file_names'] = file_names

    #%%
    return df