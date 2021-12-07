import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

lines = input.split('\n')

# Part 1

numberOfPossibleTriangles = 0

for line in lines:
    numbers = list(map(lambda x: int(x), line.split()))
    numbers.sort()
    if numbers[0]+numbers[1] > numbers[2]:
        numberOfPossibleTriangles += 1

print(numberOfPossibleTriangles)

# Part 2

numberOfPossibleTriangles = 0
i = 0

while i < len(lines):
    numbers = []
    for j in range(3):
        numbers += list(map(lambda x: int(x), lines[i+j].split()))
    
    for j in range(3):
        triangle = []
        for k in range(3):
            triangle += [numbers[j+3*k]]
        triangle.sort()
        if triangle[0]+triangle[1] > triangle[2]:
            numberOfPossibleTriangles += 1
    i += 3


print(numberOfPossibleTriangles)