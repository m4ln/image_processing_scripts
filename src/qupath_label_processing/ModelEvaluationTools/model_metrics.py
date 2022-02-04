
def model_metrics(label_exp, label_pred, metric):

    #%% import stuff
    from sklearn.metrics import jaccard_score
    from sklearn.metrics import f1_score
    from sklearn.metrics import accuracy_score
    import numpy as np

    #%% prepare the labels
    label_exp_flat = np.ndarray.tolist(np.ndarray.flatten(label_exp))
    label_pred_flat = np.ndarray.tolist(np.ndarray.flatten(label_pred))

    #%% calculate the jaccard value
    results = []
    method = []

    if ("jaccard" in metric) or ("all" in metric):
        r = jaccard_score(label_pred_flat, label_exp_flat, average = "macro")
        results.append(r)
        method.append("jaccard")

    if ("f1" in metric) or ("all" in metric):
        r = f1_score(label_pred_flat, label_exp_flat, average='macro')
        results.append(r)
        method.append("f1")

    if ("accuracy" in metric) or ("all" in metric):
        r = accuracy_score(label_pred_flat, label_exp_flat)
        results.append(r)
        method.append("accuracy")

    # %% create the output
    import pandas as pd
    df = pd.DataFrame(list(zip(method, results,)),
                      columns=['Metric', 'Value'])


    #%% return the favor

    return df