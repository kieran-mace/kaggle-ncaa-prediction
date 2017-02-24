# This is the scoring function
import numpy as np

def get_score(guess, actual):
    diff = actual - guess
    return diff


# get_score(1,1) should return 0
# get_score(0,0) should return 0
# get_score(1,0) should return Inf
# get_score(0.5,1) should return 0.6931472
