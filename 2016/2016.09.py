import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

# Part 1

index = 0
result = ''

while index < len(input):
    if input[index] == '(':
        marker=''
        i=1
        while input[index+i] != ')':
            marker += input[index + i]
            i += 1
        parts = list(map(lambda x: int(x),marker.split('x')))
        if parts[1] > 0:
            repeatingPart = input[index + i + 1 : index + i + parts[0] + 1]
            for j in range(parts[1]):
                result += repeatingPart
            index += i + parts[0] + 1
        else:
            index += i + 1
    else:
        result += input[index]
        index += 1

print("Part 1:",len(result))

# Part 2

def recursiveCount(line):
    length = 0
    index = 0
    while index < len(line):
        if line[index] == '(':
            marker=''
            i=1
            while line[index+i] != ')':
                marker += line[index + i]
                i += 1
            parts = list(map(lambda x: int(x),marker.split('x')))
            if parts[1] > 0:
                repeatingPart = line[index + i + 1 : index + i + parts[0] + 1]
                length += recursiveCount(repeatingPart)*parts[1]
                index += i + parts[0] + 1
            else:
                index += i + 1
        else:
            length += 1
            index += 1
    return length

result = recursiveCount(input)
print("Part 2:", result)