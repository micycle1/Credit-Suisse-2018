import sys

def question05(allowedAllocations, totalValue):
    z = 2**32
    table = [z]*(totalValue+1)
    table[0] = 0

    for i in range(1, totalValue+1):
        for j in range(len(allowedAllocations)):
            if allowedAllocations[j] <= i:
                sub_res = table[i - allowedAllocations[j]]
                if (sub_res != z and (sub_res + 1) < table[i]):
                    table[i] = sub_res+1
    return table[-1]
"""
import random
test = random.sample(range(1, 5000), 300)
"""
