import sys

sys.path.append("./")
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

# Part 1

memory = input

i = 0
j = len(memory) - 1 if len(memory) % 2 == 1 else len(memory) - 2
index = -1

result = 0
isRunning = True
while isRunning:
    if i % 2 == 0:
        for k in range(int(memory[i])):
            index += 1
            result += int(i / 2) * index
    else:
        toCover = int(memory[i])
        coverable = int(memory[j])
        while toCover > 0:
            coverable = int(memory[j])
            while toCover > 0 and coverable > 0:
                index += 1
                result += int(j / 2) * index
                toCover -= 1
                coverable -= 1
            memory = memory[:j] + str(coverable) + memory[j + 1 :]
            if toCover > 0:
                memory = memory[:j] + str(coverable) + memory[j + 1 :]
                j -= 2
            if j < i:
                isRunning = False
                break
    i += 1
    if i > len(memory) or j < i:
        isRunning = False

print("Part 1: ", result)

# Part 2


def findIndex(memory: list, file: int, length: int = 0) -> int:
    if file >= 0:
        for i in range(1, len(memory) + 1):
            memoryFile = memory[len(memory) - i]
            if memoryFile[0] == file:
                return len(memory) - i
    else:
        for i, memoryFile in enumerate(memory):
            if memoryFile[0] == -1 and memoryFile[1] >= length:
                return i
        return -1


def findFreeMemory(memory: list, index: int, side: int) -> int:
    if index + side in range(len(memory)):
        if memory[index + side][0] > 0:
            return 0
        else:
            return memory[index + side][1]
    else:
        return 0


def printMemory(memory: list) -> None:
    memoryString = ""
    for element in memory:
        memoryString += (
            str(element[0]) * element[1] if element[0] >= 0 else "." * element[1]
        )
    print(memoryString)


memory = []

for i in range(len(input)):
    if int(input[i]) > 0:
        if i % 2 == 0:
            memory.append([int(i / 2), int(input[i])])
            file = int(i / 2)
        else:
            if memory[len(memory) - 1][0] == -1:
                memory[len(memory) - 1][1] += int(input[i])
            else:
                memory.append([-1, int(input[i])])

while file > 0:
    fileIndex = findIndex(memory, file)
    freeMemoryIndex = findIndex(memory, -1, memory[fileIndex][1])
    if freeMemoryIndex > 0 and freeMemoryIndex < fileIndex:
        fileData = [*memory[fileIndex]]
        combinedFreeSpace = [
            -1,
            fileData[1]
            + findFreeMemory(memory, fileIndex, -1)
            + findFreeMemory(memory, fileIndex, 1),
        ]

        leftIndex = fileIndex - 1 if (memory[fileIndex - 1][0]) < 0 else fileIndex
        rightIndex = (
            fileIndex + 1
            if (fileIndex + 1 < len(memory) and memory[fileIndex + 1][0] < 0)
            else fileIndex
        )
        memory = memory[:leftIndex] + [combinedFreeSpace] + memory[rightIndex + 1 :]

        leftOverFreeMemory = memory[freeMemoryIndex][1] - fileData[1]
        memory = (
            (
                memory[:freeMemoryIndex]
                + [fileData]
                + [[-1, leftOverFreeMemory]]
                + memory[freeMemoryIndex + 1 :]
            )
            if leftOverFreeMemory > 0
            else memory[:freeMemoryIndex] + [fileData] + memory[freeMemoryIndex + 1 :]
        )
    file -= 1

index = 0
result = 0
for element in memory:
    if element[0] > 0:
        for i in range(element[1]):
            result += element[0] * index
            index += 1
    else:
        index += element[1]

print("Part 2: ", result)
