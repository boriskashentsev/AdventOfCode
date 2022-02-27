import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

# Part 1

lengths = list(map(lambda x: int(x), input.split(',')))

index = 0
skipSize = 0

myList = list(range(256))
if len(sys.argv) > 1:
    myList = list(range(5))


for length in lengths:
    if length <= len(myList):
        endIndex = index + length
        listToReverse = []
        if endIndex > len(myList):
            listToReverse = list(reversed(myList[index:] + myList[:endIndex-len(myList)]))
            myList = listToReverse[len(myList)-index:] + myList[endIndex-len(myList):index] + listToReverse[:len(myList)-index]
        else:
            listToReverse = list(reversed(myList[index:endIndex]))
            myList = myList[:index] + listToReverse + myList[endIndex:]
        index = (index + length + skipSize) % len(myList)
        skipSize += 1

print("Part 1:",myList[0]*myList[1])

# Part 2

lengths = list(map(lambda x: ord(x), list(input))) + [17, 31, 73, 47, 23]

index = 0
skipSize = 0

myList = list(range(256))

for i in range(64):
    for length in lengths:
        if length <= len(myList):
            endIndex = index + length
            listToReverse = []
            if endIndex > len(myList):
                listToReverse = list(reversed(myList[index:] + myList[:endIndex-len(myList)]))
                myList = listToReverse[len(myList)-index:] + myList[endIndex-len(myList):index] + listToReverse[:len(myList)-index]
            else:
                listToReverse = list(reversed(myList[index:endIndex]))
                myList = myList[:index] + listToReverse + myList[endIndex:]
            index = (index + length + skipSize) % len(myList)
            skipSize += 1

finalHash = ''

for i in range(16):
    result = myList[16*i]
    for j in range(1,16):
        result ^= myList[16*i + j]
    hexResult = hex(result)
    finalHash += '0'*(4-len(hexResult)) + hexResult[2:]

print("Part 2:", finalHash)


