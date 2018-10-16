import sys

def question05(allowedAllocations, totalValue):
    table = [0] #base
    for i in range(totalValue):
        table.append(sys.maxsize)
    for i in range(1, totalValue+1):
        for j in range(len(allowedAllocations)):
            if allowedAllocations[j] <= i:
                sub_res = table[i - allowedAllocations[j]]
                if (sub_res != sys.maxsize and (sub_res + 1) < table[i]):
                    table[i] = sub_res+1
    return table[-1]
