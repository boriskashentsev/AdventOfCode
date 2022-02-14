import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

lines = input.split('\n')

# Part 1

def containsABBA(line):
    for i in range(len(line)-3):
        if line[i]==line[i+3] and line[i+1]==line[i+2] and line[i]!=line[i+1]:
            return True
    return False

result = 0

for line in lines:
    hasABBA = False
    hasABBAinHS = False
    parts = line.split('[')
    for part in parts:
        if ']' in part:
            smallerParts = part.split(']')
            hasABBA = hasABBA or containsABBA(smallerParts[1])
            hasABBAinHS = hasABBAinHS or containsABBA(smallerParts[0])
        else:
            hasABBA = hasABBA or containsABBA(part)
    if hasABBA and not hasABBAinHS:
        result += 1

print("Part 1:", result)

# Part 2

def splitToSequences(line):
    supernetSQNC = ""
    hypernetSQNC = ""
    isHypernet = False
    for i in range(len(line)):
        if line[i] == '[':
            isHypernet = True
            supernetSQNC += "  "
        elif line[i] == ']':
            isHypernet = False
            hypernetSQNC += "  "
        elif isHypernet:
            hypernetSQNC += line[i]
        else:
            supernetSQNC += line[i]
    return [supernetSQNC, hypernetSQNC]

result = 0

for line in lines:
    supportsABA = False
    [super, hyper] = splitToSequences(line)
    for i in range(len(super)-2):
        if super[i] == super[i+2]:
            string = super[i+1]+super[i]+super[i+1]
            if string in hyper:
                supportsABA = True
                break
    if supportsABA:
        result+=1

print("Part 2", result)

