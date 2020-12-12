filename = "2020/12.input"

f = open(filename, "r")

inpt = f.read().split("\n")

steps=[]

for line in inpt:
    steps.append([line[0], int(line[1:])])

# first part

direction = 90
location = [0, 0]

for step in steps:
    if step[0] == "N" or (step[0] == "F" and direction == 0):
        location[1] = location[1] + step[1]
    elif step[0] == "S" or (step[0] == "F" and direction == 180):
        location[1] = location[1] - step[1]
    elif step[0] == "E" or (step[0] == "F" and direction == 90):
        location[0] = location[0] + step[1]
    elif step[0] == "W" or (step[0] == "F" and direction == 270):
        location[0] = location[0] - step[1]
    elif step[0] == "L":
        direction = (direction - step[1]) % 360
    elif step[0] == "R":
        direction = (direction + step[1]) % 360
    else:
        print("Where are we going?")

print (abs(location[0])+abs(location[1]))

# second part

waypoint = [10, 1]

location = [0, 0]

for step in steps :
    if step[0] == "N":
        waypoint[1] = waypoint[1] + step[1]
    elif step[0] == "S":
        waypoint[1] = waypoint[1] - step[1]
    elif step[0] == "E":
        waypoint[0] = waypoint[0] + step[1]
    elif step[0] == "W":
        waypoint[0] = waypoint[0] - step[1]
    elif step[0] == "L":
        angle = step[1]
        while angle > 0:
            temp = waypoint[0]
            waypoint[0] = -waypoint[1]
            waypoint[1] = temp
            angle = angle - 90
    elif step[0] == "R":
        angle = step[1]
        while angle > 0:
            temp = waypoint[0]
            waypoint[0] = waypoint[1]
            waypoint[1] = -temp
            angle = angle - 90
    elif step[0] == "F":
        location[0] = location[0] + step[1] * waypoint[0]
        location[1] = location[1] + step[1] * waypoint[1]

print (abs(location[0])+abs(location[1]))