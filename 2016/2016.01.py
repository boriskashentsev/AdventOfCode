def beautyPrint(field):
    for line in field:
        print(''.join(line))

filename = "2016/01.input"
f = open(filename, "r")
input = f.read()

directives = input.split(", ")

# Part 1

coordinates = [0,0]

direction = 0
move = [[0,1],[1,0],[0,-1],[-1,0]]

minMaxesOfAxes=[[0,0],[0,0]]

for directive in directives:
    if directive[0] == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    for i in range(len(coordinates)):
        coordinates[i] += move[direction][i]*int(directive[1:])
        if coordinates[i] < minMaxesOfAxes[0][i]:
            minMaxesOfAxes[0][i] = coordinates[i]
        elif coordinates[i] > minMaxesOfAxes[1][i]:
            minMaxesOfAxes[1][i] = coordinates[i]

print(abs(coordinates[0])+abs(coordinates[1]))

# Part 2

field = []

for i in range(minMaxesOfAxes[1][1]-minMaxesOfAxes[0][1]+2):
    line = ['.']*(minMaxesOfAxes[1][0]-minMaxesOfAxes[0][0]+2)
    field.append(line)

coordinates = [0-minMaxesOfAxes[0][0], 0-minMaxesOfAxes[0][1]]

field[coordinates[1]][coordinates[0]]='x'

isLocationFound = False

for directive in directives:
    if directive[0] == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    for i in range(int(directive[1:])):
        for j in range(len(coordinates)):
            coordinates[j] += move[direction][j]
        if field[coordinates[1]][coordinates[0]] != '.':
            isLocationFound = True
            break
        else:
            field[coordinates[1]][coordinates[0]]='*'
    if isLocationFound:
        break
beautyPrint(field)

print(abs(coordinates[0] + minMaxesOfAxes[0][0])+abs(coordinates[1] + minMaxesOfAxes[0][1]))