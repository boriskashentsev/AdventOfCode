import sys
sys.path.append('./')
from utils.filename import calculateFileName
from utils.string import stringInsert
from functools import reduce

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

lines = input.split('\n')

# Part 1

def printScreen(screen):
    for line in screen:
        print(''.join(map(lambda x: ' ' if x=='.' else x, line)))

screenSize = [50,6]
screen = ['.'*screenSize[0]]*screenSize[1]

for line in lines:
    parts = line.split(' ')
    if parts[0] == 'rect':
        size = list(map(lambda x: int(x), parts[1].split('x')))
        for i in range(size[1]):
            screen[i] = stringInsert(screen[i], '#'*size[0], 0)
    elif parts[0] == 'rotate':
        if parts [1] == 'row':
            rowNumber = int(parts[2][2:])
            byNumber = int(parts[4])
            screen[rowNumber] = screen[rowNumber][screenSize[0]-(byNumber % screenSize[0]):] + screen[rowNumber][:screenSize[0]-(byNumber % screenSize[0])]
        elif parts[1] == 'column':
            columnNumber = int(parts[2][2:])
            byNumber = int(parts[4])
            for i in range(byNumber % screenSize[1]):
                lastElement = screen[screenSize[1]-1][columnNumber]
                for j in reversed(range(screenSize[1]-1)):
                    screen[j+1] = stringInsert(screen[j+1], screen[j][columnNumber],columnNumber)
                screen[0] = stringInsert(screen[0], lastElement, columnNumber)

result = reduce(lambda a,b: a+b, map(lambda line: reduce(lambda a,b: a+b,map(lambda x: 0 if x=='.' else 1, line)), screen))
print(result)

# Part 2
printScreen(screen)