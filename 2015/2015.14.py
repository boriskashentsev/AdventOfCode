filename = "2015/14.input"

f = open(filename, "r")

input = f.read().split("\n")

runners={}

for line in input:
    parts = line.split(' ')
    name = parts[0]
    speed = int(parts[3])
    runTime = int(parts[6])
    restTime = int(parts[13])
    runners[name] = {'speed': speed,
                     'run'  : runTime,
                     'rest' : restTime}

#time = 1000
time = 2503

# Part 1

def calculateDistance(runner, time):
    distance = (time // (runner['run'] + runner['rest'])) * runner['speed'] * runner['run']
    if  time % (runner['run'] + runner['rest']) >= runner['run']:
        distance += runner['run']*runner['speed']
    else :
        distance += (time % (runner['run'] + runner['rest'])) * runner['speed']
    return distance

maxDistance = -1

for runner in runners.keys():
    distance = calculateDistance(runners[runner], time)
    if distance > maxDistance:
        maxDistance = distance

print(maxDistance)

# Part 2

for runner in runners.keys():
    runners[runner]['distance'] = 0
    runners[runner]['points'] = 0

for second in range(1,time+1):
    maxDistance = -1
    for runner in runners.keys():
        distance = calculateDistance(runners[runner], second)
        runners[runner]['distance'] = distance
        if maxDistance < distance:
            maxDistance = distance
    for runner in runners.keys():
        if maxDistance == runners[runner]['distance']:
            runners[runner]['points'] += 1

maxPoints = -1
for runner in runners.keys():
    if maxPoints < runners[runner]['points']:
        maxPoints = runners[runner]['points']

print(maxPoints)