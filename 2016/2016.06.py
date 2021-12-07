import sys
sys.path.append('./')
from utils.filename import calculateFileName
from functools import cmp_to_key

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

lines = input.split('\n')

histograms = []

for line in lines:
    for i in range(len(line)):
        letter = line[i]
        histogram = []
        if len(histograms) > i :
            histogram = histograms[i]
        isLetterFound = False
        j = 0
        while j < len(histogram) and not isLetterFound:
            if histogram[j][0] == letter:
                histogram[j][1] += 1
                isLetterFound = True
            j += 1
        if not isLetterFound:
            histogram += [[letter, 1]]
        if len(histograms) > i:
            histograms[i] = histogram
        else :
            histograms += [histogram]

def compare(item1, item2):
    if item1[1] < item2[1]:
        return 1
    elif item1[1] == item2[1] and item1[0] > item2[0]:
        return 1
    return -1

# Part 1 and Part 2

phrasePart1 = ''
phrasePart2 = ''
for histogram in histograms:
    histogram.sort(key = cmp_to_key(compare))
    phrasePart1 += histogram[0][0]
    phrasePart2 += histogram[-1][0]

print(phrasePart1)
print(phrasePart2)