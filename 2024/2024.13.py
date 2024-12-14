import sys
from re import findall

sys.path.append("./")
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

# Part 1

machines = input.split("\n\n")

tokens = 0
for machine in machines:
    [x1, y1, x2, y2] = list(map(lambda x: int(x), findall("\\+\\d{1,}", machine)))
    [x0, y0] = list(map(lambda x: int(x[1:]), findall("=\\d{1,}", machine)))

    if (x0 * y2 - x2 * y0) % (x1 * y2 - x2 * y1) == 0 and (x0 * y1 - x1 * y0) % (
        x2 * y1 - x1 * y2
    ) == 0:
        tokens += 3 * (x0 * y2 - x2 * y0) / (x1 * y2 - x2 * y1) + 1 * (
            x0 * y1 - x1 * y0
        ) / (x2 * y1 - x1 * y2)

print("Part 1: ", int(tokens))

# Part 2

machines = input.split("\n\n")

tokens = 0
for machine in machines:
    [x1, y1, x2, y2] = list(map(lambda x: int(x), findall("\\+\\d{1,}", machine)))
    [x0, y0] = list(map(lambda x: int(x[1:]), findall("=\\d{1,}", machine)))

    x0 += 10000000000000
    y0 += 10000000000000

    if (x0 * y2 - x2 * y0) % (x1 * y2 - x2 * y1) == 0 and (x0 * y1 - x1 * y0) % (
        x2 * y1 - x1 * y2
    ) == 0:
        tokens += 3 * (x0 * y2 - x2 * y0) / (x1 * y2 - x2 * y1) + 1 * (
            x0 * y1 - x1 * y0
        ) / (x2 * y1 - x1 * y2)

print("Part 1: ", int(tokens))
