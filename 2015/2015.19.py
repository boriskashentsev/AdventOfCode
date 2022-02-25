from dataclasses import replace
import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

replacement = {}

for line in lines:
    parts = line.split(' => ')
    if len(parts) > 1:
        if parts[0] in replacement.keys():
            replacement[parts[0]].append(parts[1])
        else:
            replacement[parts[0]] = [parts[1]]
    elif len(line) > 0:
        startMolecule = line

# Part 1

molecules = set()

maxKeyLen = max(list(map(lambda x: len(x), list(replacement.keys()))))
for i in range(len(startMolecule)):
    for j in range(1,maxKeyLen+1):
        possibleKey = startMolecule[i:min([i+j, len(startMolecule)])]
        if len(possibleKey) == j:
            if possibleKey in replacement.keys():
                for element in replacement[possibleKey]:
                    newMolecule = startMolecule[:i] + element + startMolecule[i+j:]
                    molecules.add(newMolecule)

print(len(molecules))

# Part 2

### Direct attempt to solve it. But it takes too much time.
#def newStep(molecule, step, minStep):
#    #print(molecule)
#    if molecule == startMolecule:
#        minStep = step if minStep == -1 or minStep > step else minStep
#    elif len(molecule) <= len(startMolecule):
#        for i in range(len(molecule)):
#            for j in range(1,maxKeyLen + 1):
#                possibleKey = molecule[i:min([i+j, len(molecule)])]
#                if len(possibleKey) == j:
#                    if possibleKey in replacement.keys():
#                        for element in replacement[possibleKey]:
#                            newMolecule = molecule[:i] + element + molecule[i+j:]
#                            if minStep < 0 or (minStep > 0 and step + 1 < minStep):
#                                minStep = newStep(newMolecule, step +1, minStep)
#    else:
#        print(molecule)
#    return minStep
#
#molecule = 'e'
#
#result = newStep(molecule, 0, -1)
#
#print(result)

# Part 2 second try
# If building it take too much time, let's break it down instead.

backReplacement = {}

for line in lines:
    parts = line.split(' => ')
    if len(parts) > 1:
        if parts[1] in backReplacement.keys():
            backReplacement[parts[1]].append(parts[0])
        else:
            backReplacement[parts[1]] = [parts[0]]

finalMolecule = 'e'

maxKeyLen = max(list(map(lambda x: len(x), list(backReplacement.keys()))))

allMolecules = set()

def newStep(molecule, step, minStep):
    if molecule == finalMolecule:
        minStep = step if minStep == -1 or minStep > step else minStep
    elif finalMolecule not in molecule:
        # After waiting algorithm to finish for a long time, I had to check some ideas for a solution
        # 1. Getting rid of longer sequences helped
        # 2. Going over the initial molecule from the end also helped
        # Link to the helpful comment: https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4qca2/?utm_source=share&utm_medium=web2x&context=3
        for i in reversed(range(len(molecule))):
            for j in reversed(range(1,maxKeyLen + 1)):
                possibleKey = molecule[i:min([i+j, len(molecule)])]
                if len(possibleKey) == j:
                    if possibleKey in backReplacement.keys():
                        for element in backReplacement[possibleKey]:
                            newMolecule = molecule[:i] + element + molecule[i+j:]
                            if newMolecule not in allMolecules:
                                allMolecules.add(newMolecule)
                                if minStep > 0:
                                    # 3. Adding this print reveales result before the program was finished
                                    print(minStep, newMolecule, step)
                                else:
                                    print(newMolecule, step)
                                if minStep < 0 or (minStep > 0 and step + 1 < minStep):
                                    minStep = newStep(newMolecule, step +1, minStep)
    return minStep

result = newStep(startMolecule, 0, -1)

print(result)
