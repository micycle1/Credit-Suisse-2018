# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

#import numpy as np

# return minimum difference between a subset from each param
def question02(cashFlowIn, cashFlowOut):

  table = []

  result = min(min(cashFlowIn),min(cashFlowOut))

  for i in cashFlowIn:
    sums = []
    for o in cashFlowOut:
      sums.append(i-o)
      result = min(result,i-o)
    table.append(sums)
    
##  for row in table:
##    #print row
##    pass

  return result
    

##  table2 = []
##  for i, row in enumerate(table):
##    for rowIndex in range(len(row)):
##      if not rowIndex == i:
##        table2.append(i+o)
##  print table2

"""
cin = [66, 293, 215, 188, 147, 326, 449, 162, 46, 350]
cout = [170, 153, 305, 290, 187]

cin2 = [189, 28,99]
cout2 = [43, 267, 112, 166]
"""
