from operator import contains
import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
containers = list(map(lambda x: int(x), input.split('\n')))

eggnogAmount = 150

def listSum(list):
    result = 0
    for element in list:
        result += element
    return result

def findNextContainer(containers, index, usedContainers, count):
    containerSum = listSum(usedContainers)
    if(containerSum == eggnogAmount):
        if len(usedContainers) in count.keys():
            count[len(usedContainers)] += 1
        else:
            count[len(usedContainers)] = 1
    elif (containerSum < eggnogAmount):
        for i in range(index, len(containers)):
            usedContainers.append(containers[i])
            count = findNextContainer(containers, i+1, usedContainers, count)
            usedContainers.pop()
    return count

result = findNextContainer(containers, 0, [], {})

# Part 1
part1result = 0
for key in result.keys():
    part1result += result[key]
print(part1result)

# Part 2
print(result[min(list(result.keys()))])