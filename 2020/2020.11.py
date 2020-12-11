import copy

def printSeats(plan):
    for rows in plan:
        print("".join(rows))
    print(" ")

filename = "2020/11.input"

f = open(filename, "r")

inpt = f.read().split("\n")

plan = []

size = 0

for line in inpt:
    if len(plan) == 0:
        size = len(line)
        plan.append('.' * (size+2))
    plan.append('.' + line + '.')
plan.append('.' * (size+2))

# first part
rounds = [[]]
for i in range(len(plan)):
    rounds[0].append(list(plan[i]))

stepX = [-1, -1, 0, 1, 1, 1, 0, -1]
stepY = [0, 1, 1, 1, 0, -1, -1, -1]

#printSeats(rounds[0])

changed = True
while changed :
    changed = False

    rounds.append(copy.deepcopy(rounds[0]))

    for i in range(1, len(rounds[0])-1):
        for j in range(1, len(rounds[0][0])-1):
            numOccupied = 0
            if rounds[0][i][j] in 'L#':
                numOccupied = 0

                for k in range(len(stepX)):
                    if rounds[0][i+stepY[k]][j+stepX[k]] == '#':
                        numOccupied = numOccupied + 1

                if rounds[0][i][j] == 'L' and numOccupied == 0:
                    rounds[1][i][j] = '#'
                elif rounds[0][i][j] == '#' and numOccupied >= 4:
                    rounds[1][i][j] = 'L'

                if rounds[0][i][j] != rounds[1][i][j]:
                    changed = True
    rounds.pop(0)
    #printSeats(rounds[0])

numOccupied = 0
for i in range(1, len(rounds[0])-1):
    for j in range(1, len(rounds[0][0])-1):
        if rounds[0][i][j] == '#':
            numOccupied = numOccupied + 1

print(numOccupied)

# second part

def part2neighbours(plan, i, j):
    stepX = [-1, -1, 0, 1, 1, 1, 0, -1]
    stepY = [0, 1, 1, 1, 0, -1, -1, -1]
    numOfNeighbours = 0

    for k in range(len(stepX)):
        newY = i + stepY[k]
        newX = j + stepX[k]
        noNeighbour = True
        while newY >=0 and newY < len(plan) and newX >= 0 and newX < len(plan[0]):
            if plan[newY][newX] == 'L':
                break
            elif plan[newY][newX] == '#':
                noNeighbour = False
            newY = newY + stepY[k]
            newX = newX + stepX[k]
        if not noNeighbour:
            numOfNeighbours = numOfNeighbours + 1
    
    return numOfNeighbours

rounds = [[]]
for i in range(len(plan)):
    rounds[0].append(list(plan[i]))

changed = True
while changed :
    changed = False

    rounds.append(copy.deepcopy(rounds[0]))

    for i in range(1, len(rounds[0])-1):
        for j in range(1, len(rounds[0][0])-1):
            numOccupied = 0
            if rounds[0][i][j] in 'L#':
                numOccupied = part2neighbours(rounds[0], i, j)

                if rounds[0][i][j] == 'L' and numOccupied == 0:
                    rounds[1][i][j] = '#'
                elif rounds[0][i][j] == '#' and numOccupied >= 5:
                    rounds[1][i][j] = 'L'

                if rounds[0][i][j] != rounds[1][i][j]:
                    changed = True

    rounds.pop(0)

numOccupied = 0
for i in range(1, len(rounds[0])-1):
    for j in range(1, len(rounds[0][0])-1):
        if rounds[0][i][j] == '#':
            numOccupied = numOccupied + 1

print(numOccupied)