# This is the scoring function
import numpy as np

def get_score(guess, actual):
    diff = actual - guess
    return diff


# get_score(1.0,1.0) should return 0.0
# get_score(0.0,0.0) should return 0.0
# get_score(1.0,0.0) should return Inf
# get_score(0.5,1.0) should return 0.6931472


def score_predictions(truth, predicitons):
    scores = list()
    for i in range(0,len(truth)-1)
        scores[i] = get_score[predicitons[i], truth[i]]
    return np.mean(scores)
    
