import numpy as np


def make_prediction(input):
    # Currently just going to return a random Number
    return np.random.random() # random number between 0 and 1


def predict_all(inputs):
    predictions = [make_prediction(x) for x in inputs]
    return predictions

def apply_prediction(dataframe):
    dataframe['pred'] = dataframe['id'].apply(lambda x: make_prediction(x))
    sample_submission.to_csv('test.csv',index=False)
    return(dataframe)
