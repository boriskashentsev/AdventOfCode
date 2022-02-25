import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

mfcsam_result = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3,
                'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

sues = []

lines = input.split('\n')
for line in lines:
    parts = line.split(' ')
    memory = {}
    i = 2
    while i < len(parts):
        type = parts[i][:-1]
        number = int(parts[i+1][:-1]) if parts[i+1][-1] == ',' else int(parts[i+1])
        memory[type] = number
        i += 2
    sues.append(memory)

# Part 1

possibleSues = []

for i in range(len(sues)):
    sue = sues[i]
    isCurrentSue = True
    for key in sue.keys():
        if sue[key] != mfcsam_result[key]:
            isCurrentSue = False
            break
    if isCurrentSue:
        possibleSues.append(i+1)

print(possibleSues)

# Part 2

possibleSues = []
greaterKeys = ['cats', 'trees']
fewerKeys = ['pomeranians', 'goldfish']

for i in range(len(sues)):
    sue = sues[i]
    isCurrentSue = True
    for key in sue.keys():
        if key in greaterKeys: 
            if sue[key] <= mfcsam_result[key]:
                isCurrentSue = False
                break
        elif key in fewerKeys: 
            if sue[key] >= mfcsam_result[key]:
                isCurrentSue = False
                break
        elif (sue[key] != mfcsam_result[key]):
            isCurrentSue = False
            break
    if isCurrentSue:
        possibleSues.append(i+1)

print(possibleSues)