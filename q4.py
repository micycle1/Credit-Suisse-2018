def question04(rows, numberMachines):

  if not any(isinstance(i, list) for i in rows):
    rows = [rows]

  sequences = []
  for i, row in enumerate(rows):
    temp = []
    for k, symbol in enumerate(row):
      if symbol != 'X':
        temp.append(symbol)
      else:
        if len(temp) >= numberMachines:
          sequences.append(temp)
          temp = []
    if temp and len(temp) >= numberMachines:
      sequences.append(temp) #still append if no 'x' found
      temp = []

  if not sequences: # empty
    return 0

  max_sum = 2**32
  for sequence in sequences:
    #sequence = list(itertools.combinations(sorted(sequence), numberMachines))
    sequence = sorted(sequence)
    sequenceSum = sum(sequence[i] for i in range(numberMachines))
    max_sum = min(max_sum, sequenceSum)
##    for subsequence in sequence:
##      max_sum = min(max_sum, sum(subsequence))
  return max_sum

"""
test = ([11,12, 12, 3, 'X', 3],
        [23, 'X', 'X', 'X', 3],
        [33, 21, 'X', 'X', 'X'],
        [9, 12, 3, 'X', 'X'],
        ['X', 'X', 'X', 4, 5])

test2 = (['X', 'X', 2], [2, 3, 'X'], ['X', 3, 2])

test3 = ([2, 3, 'X', 2], [4, 'X', 'X', 4], [3, 2, 'X', 'X'], ['X', 'X', 'X', 5])


test4 = ([11,12, 12, 3, 'X', 3],[23, 'X', 'X', 'X', 3],[23, 'X', 'X', 'X', 3],
        [23, 'X', 'X', 'X', 3, 33, 21, 'X', 'X', 'X', 21, 'X', 'X', 7, 9, 2],
        [33, 21, 'X', 'X', 'X'],[9, 12, 3, 'X', 'X','X', 4, 5, 423,4,3,3,5,6],['X', 'X', 'X', 4, 5],['X', 'X', 'X', 4, 5],[9, 12, 3, 'X', 'X','X', 4, 5,423,4,3,3,5,6],['X', 'X', 'X', 4, 5],['X', 'X', 'X', 4, 5],
        [9, 12, 3, 'X', 'X','X', 4, 5,423,4,3,3,5,6],['X', 'X', 'X', 4, 5],['X', 'X', 'X', 4, 5],
        ['X', 'X', 'X', 4, 5])
"""
