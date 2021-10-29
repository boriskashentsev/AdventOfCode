def dealWithAPerson(person, people):
    '''Add person to the disctionary if s/he doesn't exist already'''
    if person not in people.keys():
        people[person] = len(people.keys())

def dealWithHappiness (person1Index, person2Index, gainOrLose, number, happiness):
    '''Add happiness value between two people to the matrix'''
    maxIndex = max(person1Index, person2Index)
    if maxIndex >= len(happiness):
        for i in range(len(happiness)):
            happiness[i].append(0)
        happiness.append([0]*len(happiness[0]))
    happiness[person1Index][person2Index] = int(number) if gainOrLose == "gain" else -1 * int(number)

def printMatrix(matrix):
    '''Helpful matrix printer function'''
    for i in range(len(matrix)):
        print(matrix[i])

def calculateHappiness(order, happiness):
    '''Calculate cummulative happiness around the table'''
    joy = 0
    trueOrder = [0] + order
    for i in range(len(trueOrder)):
        joy += happiness[trueOrder[i]][trueOrder[(i+1)%len(trueOrder)]] + happiness[trueOrder[i]][trueOrder[(i-1)%len(trueOrder)]]
    return joy

def generateNewOrderAndCountHappiness(leftover, result, happiness, maxValue):
    if len(leftover) == 0:
        joy = calculateHappiness(result, happiness)
        maxReturn = joy if (maxValue < 0 or maxValue < joy) else maxValue
        return maxReturn
    
    for i in range(len(leftover)):
        value = leftover.pop(i)
        result.append(value)
        maxValue = generateNewOrderAndCountHappiness(leftover, result, happiness, maxValue)
        leftover.insert(i, value)
        result.pop()
    return maxValue

def findMaxHappiness(happiness):
    indexes = list(range(1, len(happiness)))
    result = generateNewOrderAndCountHappiness(indexes, [], happiness, -1)
    return result

filename = "2015/13.input"

f = open(filename, "r")

input = f.read().split("\n")

# Part 1

people = {}
happiness  = [[0]]

for line in input:
    parts = line.split(" ")
    dealWithAPerson(parts[0],people)
    dealWithAPerson(parts[10][0:len(parts[10])-1], people)
    dealWithHappiness(people[parts[0]], people[parts[10][0:len(parts[10])-1]], parts[2] , parts[3], happiness)

maxvalue = findMaxHappiness(happiness)

print(maxvalue)

# Part 2

you = 'You'

def dealWithYou(people):
    '''Adding you to the table'''
    dealWithAPerson(you, people)

def dealWithYourHappiness(people, happiness):
    '''Adding your joy values to the matrix'''
    for i in range(len(people)):
        dealWithHappiness(people[you], i, 'gain', '0', happiness)
        dealWithHappiness(i, people[you], 'gain', '0', happiness)
    return

dealWithYou(people)
dealWithYourHappiness(people, happiness)

maxvalue = findMaxHappiness(happiness)
print(maxvalue)