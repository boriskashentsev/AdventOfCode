filename = "2020/3.input"

f = open(filename, "r")

inpt = f.read().split("\n")

terrain=[]

for line in inpt:
    terrain.append(line)

#First part

movement = [1,3]
location = [0,0]

answer = 0

while location[0]<len(terrain):
    if (terrain[location[0]][location[1]] == '#'):
        answer = answer + 1
    location[0] = location[0] + movement[0]
    location[1] = (location[1] + movement[1]) % len(terrain[0])


print(answer)

#Second part

movements = [[1,1], [1,3], [1,5], [1,7], [2,1]]
secondAnswer = 1

for movement in movements:
    location = [0,0]
    answer = 0
    while location[0]<len(terrain):
        if (terrain[location[0]][location[1]] == '#'):
            answer = answer + 1
        location[0] = location[0] + movement[0]
        location[1] = (location[1] + movement[1]) % len(terrain[0])
    secondAnswer = secondAnswer * answer


print(secondAnswer)