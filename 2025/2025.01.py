import sys

sys.path.append("./")
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

# Part 1
lines = input.split("\n")

dial = 50
count = 0

for line in lines:
    char = line[0]
    number = int(line[1:])
    dial = (dial + number) % 100 if char == "R" else (dial - number) % 100
    if dial == 0:
        count += 1

print("Part 1:", count)

# Part 2

dial = 50
count = 0

for line in lines:
    char = line[0]
    number = int(line[1:])
    for _ in range(number):
        dial = (dial + 1) if char == "R" else (dial - 1)
        if (dial % 100) == 0:
            count += 1


print("Part 2:", count)
