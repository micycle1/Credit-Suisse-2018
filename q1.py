# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

#import numpy as np
import itertools

# modify this function, and create other functions below as you wish
def question01(portfolios):
    highest = 0
    for x,y in itertools.combinations(portfolios, r=2):
        highest = max(highest, x^y)
    return highest
