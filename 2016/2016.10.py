import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

lines = input.split('\n')

comparingValues = [17, 61]
if len(sys.argv) > 1:
    comparingValues = [3, 5]

bots = {}
output = {}
instructions = {}

botsWithTwoChips = []

for line in lines:
    parts = line.split(' ')
    sign = {}
    if parts[0] == 'bot':
        sign[0] = int(parts[6]) if parts[5] == "bot" else -1*(int(parts[6])+1)
        sign[1] = int(parts[11]) if parts[10] == "bot" else -1*(int(parts[11])+1)
        instructions[int(parts[1])] = [sign[0], sign[1]]
    elif parts[0] == 'value':
        botIndex = int(parts[5])
        if botIndex in bots.keys():
            bots[botIndex] += [int(parts[1])]
            if len(bots[botIndex]) > 2:
                print("NOT ENOUGH HANDS in", botIndex)
            elif len(bots[botIndex]) == 2:
                botsWithTwoChips += [botIndex]
        else:
            bots[botIndex] = [int(parts[1])]
        continue
    else:
        print("We never should get here")

result = -1

while len(botsWithTwoChips) > 0:
    values = sorted(bots[botsWithTwoChips[0]])
    if values == comparingValues:
        result = botsWithTwoChips[0]
    destinations = instructions[botsWithTwoChips[0]]
    for i, index in enumerate(destinations):
        if index < 0:
            output[-1*index] = values[i]
        else:
            if index in bots.keys():
                bots[index] += [values[i]]
                if len(bots[botIndex]) > 2:
                    print("NOT ENOUGH HANDS in", index)
                elif len(bots[index]) == 2:
                    botsWithTwoChips += [index]
            else:
                bots[index] = [values[i]]
    botsWithTwoChips = botsWithTwoChips[1:]

print("Part 1:", result)

print("Part 2:", output[1]*output[2]*output[3])