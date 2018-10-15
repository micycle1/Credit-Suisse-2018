# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

#import numpy as np
import itertools

#compute all combinations for two portfolios
def question04(rows, numberMachines):

  def generate():
    sequences = []
    for i, row in enumerate(rows):
      temp = []
      for k, symbol in enumerate(row):
        if symbol != 'X':
          temp.append(symbol)
        else:
          if len(temp) >= numberMachines:
            sequences.append(temp)
            #yield temp
            temp = []
    return sequences

  out = generate()
  if not out: # empty
    return 0

  max_sum = 2**64
  for sequence in out:
    sequence = list(itertools.combinations(sequence, numberMachines))
    for subsequence in sequence:
      max_sum = min(max_sum, sum(subsequence))
  return max_sum

"""
test = ([11,12, 12, 3, 'X', 3],
        [23, 'X', 'X', 'X', 3],
        [33, 21, 'X', 'X', 'X'],
        [9, 12, 3, 'X', 'X'],
        ['X', 'X', 'X', 4, 5])

test2 = (['X', 'X', 2], [2, 3, 'X'], ['X', 3, 2])

test3 = ([2, 3, 'X', 2], [4, 'X', 'X', 4], [3, 2, 'X', 'X'], ['X', 'X', 'X', 5])
"""
