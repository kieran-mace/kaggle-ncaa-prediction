# This is the scoring function
import numpy as np

def get_score(guess, actual):
    diff = actual - guess
    return diff
