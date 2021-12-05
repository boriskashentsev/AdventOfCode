filename = "2021/05.input"
f = open(filename, "r")
input = f.read().split("\n")

maxX = 0
maxY = 0

vents = []

for line in input:
    parts = line.split(" ")
    start = list(map(lambda x: int(x),parts[0].split(",")))
    end = list(map(lambda x: int(x),parts[2].split(",")))
    if maxX < max(start[0], end[0]):
        maxX = max(start[0], end[0])
    if maxY < max(start[1], end[1]):
        maxY = max(start[1], end[1])
    vent = [start,end]
    vents.insert(len(vents),vent)

print(maxX, maxY)

# Part 1

field = []
for i in range(maxY+1):
    field.insert(len(field),[0]*(maxX+1))

part1Result = 0

for vent in vents:
    if vent[0][0] == vent[1][0]:
        minValue = min(vent[0][1],vent[1][1])
        maxValue = max(vent[0][1],vent[1][1])
        for i in range(minValue, maxValue + 1):
            field[i][vent[0][0]] += 1
            if field[i][vent[0][0]] == 2:
                part1Result += 1
    
    if vent[0][1] == vent[1][1]:
        minValue = min(vent[0][0],vent[1][0])
        maxValue = max(vent[0][0],vent[1][0])
        for i in range(minValue, maxValue + 1):
            field[vent[0][1]][i] += 1
            if field[vent[0][1]][i] == 2:
                part1Result += 1

print("Part 1 result:", part1Result)

# Fancy printing
#for line in field:
#    print("".join(map(lambda x: str(x) if x != 0 else ".",line)))

# Part 2

field = []
for i in range(maxY+1):
    field.insert(len(field),[0]*(maxX+1))

part2Result = 0

for vent in vents:
    if vent[0][0] == vent[1][0]:
        minValue = min(vent[0][1],vent[1][1])
        maxValue = max(vent[0][1],vent[1][1])
        for i in range(minValue, maxValue + 1):
            field[i][vent[0][0]] += 1
            if field[i][vent[0][0]] == 2:
                part2Result += 1
    
    if vent[0][1] == vent[1][1]:
        minValue = min(vent[0][0],vent[1][0])
        maxValue = max(vent[0][0],vent[1][0])
        for i in range(minValue, maxValue + 1):
            field[vent[0][1]][i] += 1
            if field[vent[0][1]][i] == 2:
                part2Result += 1
    
    if abs(vent[0][0]-vent[1][0]) == abs(vent[0][1] - vent[1][1]):
        directionX = 1 if vent[0][0] < vent[1][0] else -1
        directionY = 1 if vent[0][1] < vent[1][1] else -1
        for i in range(abs(vent[0][0]-vent[1][0])+1):
            field[vent[0][1]+i*directionY][vent[0][0]+i*directionX] += 1
            if field[vent[0][1]+i*directionY][vent[0][0]+i*directionX] == 2:
                part2Result += 1

# Fancy printing
#for line in field:
#    print("".join(map(lambda x: str(x) if x != 0 else ".",line)))

print("Part 2 result:",part2Result)