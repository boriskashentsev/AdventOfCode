def dealWithACity(city, cities):
    '''Add city to the disctionary if it doesn't exist already'''
    if city not in cities.keys():
        cities[city] = len(cities.keys())

def dealWithADistance (city1Index, city2Index, distance, distances):
    '''Add distance between the cities to the matrix'''
    maxIndex = max(city1Index, city2Index)
    if maxIndex >= len(distances):
        for i in range(len(distances)):
            distances[i].append(0)
        distances.append([0]*len(distances[0]))
    distances[city1Index][city2Index] = distance
    distances[city2Index][city1Index] = distance

def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def calculateDistance(order, distances):
    '''Calculate distance from visit order and distances between cities'''
    distance = 0
    for i in range(len(order)-1):
        distance += distances[order[i]][order[i+1]]
    return distance


def generateNewOrderAndCountDistance(leftover, result, distances, minValue, maxValue):
    '''Recursive generation of the visit orders'''
    if len(leftover) == 0:
        distance = calculateDistance(result, distances)
        minReturn = minValue
        maxReturn = maxValue
        if minValue < 0 or minValue > distance:
            minReturn = distance
        if maxReturn < 0 or maxValue < distance:
            maxReturn = distance
        return minReturn, maxReturn
    
    for i in range(len(leftover)):
        value = leftover.pop(i)
        result.append(value)
        minValue, maxValue = generateNewOrderAndCountDistance(leftover, result, distances, minValue, maxValue)
        leftover.insert(i, value)
        result.pop()
    return minValue, maxValue

def minAndMaxDistances(distances):
    indexes = list(range(len(distances)))
    results = generateNewOrderAndCountDistance(indexes, [], distances, -1, -1)
    return results

filename = "2015/9.input"

f = open(filename, "r")

input = f.read().split("\n")

cities = {}
distances  = [[0]]

for line in input:
    line_split = line.split(" ")
    dealWithACity(line_split[0], cities)
    dealWithACity(line_split[2], cities)
    dealWithADistance(cities[line_split[0]], cities[line_split[2]], int(line_split[4]), distances)

print(cities)
printMatrix(distances)

# Part 1 & 2

minResult, maxResult = minAndMaxDistances(distances)
print (minResult, ' and ', maxResult)