import sys
sys.path.append('./')
from utils.filename import calculateFileName
from copy import deepcopy

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

def prepareBins(neededSum, bins, leftover, minElements, minEntanglement, toZeroDepth):
    if len(bins) == sum(list(map(lambda x: 1 if sum(x) == neededSum else 0, bins))):
        if minElements < 0 or len(bins[0]) < minElements:
            minElements = len(bins[0])
            entanglement = 1
            for element in bins[0]:
                entanglement *= element
            minEntanglement = entanglement
            #print(minElements, minEntanglement)
        elif len(bins[0]) == minElements:
            entanglement = 1
            for element in bins[0]:
                entanglement *= element
            if minEntanglement > entanglement or minEntanglement < 0:
                minEntanglement = entanglement
                #print(minElements, minEntanglement)
        toZeroDepth = True # Found combination. Time to go to the first bin for the new combination.

    else:
        index = 0
        for i in range(len(bins)-1):
            if sum(bins[i]) == neededSum:
                index = i+1
            else:
                break

        for i in reversed(range(len(leftover))):
            if sum(bins[index]) + leftover[i] <= neededSum:
                toContinue = True
                if  len(bins[index])>0:
                    if bins[index][-1] < leftover[i]:
                        toContinue = False
                if toContinue:
                    bins[index].append(leftover[i])
                    newLeftover = []
                    for j in range(len(leftover)):
                        if j != i:
                            newLeftover.append(leftover[j])
                    if minElements < 0 or len(bins[0]) <= minElements:
                        result = prepareBins(neededSum, bins, newLeftover, minElements, minEntanglement, toZeroDepth)
                        minElements = result[0]
                        minEntanglement = result[1]
                        toZeroDepth = result[2]
                    bins[index].pop()
                    if toZeroDepth:
                        if index > 0:
                            return [minElements, minEntanglement, toZeroDepth]
                        else:
                            toZeroDepth = False

    return [minElements, minEntanglement, toZeroDepth]

numbers = list(map(lambda x: int(x),input.split('\n')))

# Part 1

bins = [[],[]]
compartments = len(bins) + 1
neededSum = sum(numbers) // compartments

result = prepareBins(neededSum, bins, numbers, -1, -1, False)
entanglement = result[1]
print(entanglement)

# Part 2

bins = [[], [], []]
compartments = len(bins) + 1
neededSum = sum(numbers) // compartments

result = prepareBins(neededSum, bins, numbers, -1, -1, False)
entanglement = result[1]
print(entanglement)