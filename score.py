# This is the scoring function
import numpy as np

def get_logloss(guess, actual):
    logloss = -np.mean(actual * np.log(guess)) + (1.0 - actual) * np.log((1.0 - guess))
    return logloss

# get_score(1,1) should return 0
# get_score(0,0) should return 0
# get_score(1,0) should return Inf
# get_score(0.5,1) should return 0.6931472
