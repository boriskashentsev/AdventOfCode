def compare(item1, item2):
    if item1[1] < item2[1]:
        return 1
    elif item1[1] == item2[1] and item1[0] > item2[0]:
        return 1
    return -1

import sys
sys.path.append('./')
from utils.filename import calculateFileName
from functools import cmp_to_key

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
resultPart1 = 0

for line in lines:
    parts = line.split('[')
    checksum = parts[1][:-1]
    parts = parts[0].split('-')
    sectorID = int(parts[-1])
    letters = ''.join(parts[:-1])
    histogram = []
    for letter in letters:
        isLetterFound = False
        j = 0
        while j < len(histogram) and not isLetterFound:
            if histogram[j][0] == letter:
                histogram[j][1] += 1
                isLetterFound = True
            j += 1
        if not isLetterFound:
            histogram += [[letter, 1]]
    histogram.sort(key = cmp_to_key(compare))
    isChecksumCorrect = True
    for i in range(len(checksum)):
        if checksum[i] != histogram[i][0]:
            isChecksumCorrect = False
            break
    if isChecksumCorrect:
        resultPart1 += sectorID
        lineSyphered=' '.join(parts[:-1])
        lineDesyphered = ''
        for i in range(len(lineSyphered)):
            if lineSyphered[i] != ' ':
                index = alphabet.index(lineSyphered[i])
                index = (index + sectorID)%len(alphabet)
                lineDesyphered += alphabet[index]
            else:
                lineDesyphered += ' '
        print(lineDesyphered, sectorID) # Search for North Pole related stuff from this massive dump

print(resultPart1)
