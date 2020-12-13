filename = "2020/13.input"

f = open(filename, "r")

inpt = f.read().split("\n")

arrival = int(inpt[0])
allIds = inpt[1].split(',')

busIds = {}
index = 0
for busId in allIds:
    if busId != 'x':
        busIds[int(busId)] = index
    index = index + 1

# first part
result = 0
minWait = max (busIds.keys())

for busId in busIds.keys():
    waitTime = (busId - arrival % busId) % busId
    if minWait > waitTime :
        minWait = waitTime
        result = minWait * busId

print(minWait, result / minWait)
print(result)

# second part (good attempt, but works too slow)

'''itterator = max(busIds.keys())
print(itterator)
result = -itterator

isEnd = False
printMax = 10000
printId = 0
while not isEnd:
    isEnd = True
    result = result + itterator
    for busId in busIds.keys():
        if (result - busIds[itterator] + busIds[busId]) % busId != 0:
            isEnd = False
    if printId % printMax == 0:
        print(result)
        printId == 0
    printId = printId + 1

print(result - busIds[itterator])'''

# second part (using https://www.reddit.com/r/adventofcode/comments/kc60ri/2020_day_13_can_anyone_give_me_a_hint_for_part_2/gfnnfm3?utm_source=share&utm_medium=web2x&context=3)

iterator = 1
value = 1

for key in busIds.keys():
    while (value + busIds[key]) % key != 0:
        value = value + iterator
    iterator = iterator*key
    print (value, iterator)

print (value)