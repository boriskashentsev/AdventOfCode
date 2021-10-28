def dealWithAPerson(person, people):
    '''Add city to the disctionary if it doesn't exist already'''
    if person not in people.keys():
        people[person] = len(people.keys())

def dealWithHappiness (person1Index, person2Index, gainOrLose, number, happiness):
    '''Add distance between the cities to the matrix'''
    maxIndex = max(person1Index, person2Index)
    if maxIndex >= len(happiness):
        for i in range(len(happiness)):
            happiness[i].append(0)
        happiness.append([0]*len(happiness[0]))
    happiness[person1Index][person2Index] = int(number) if gainOrLose == "gain" else -1 * int(number)

def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

filename = "2015/13.test.input"

f = open(filename, "r")

input = f.read().split("\n")

people = {}
happiness  = [[0]]

for line in input:
    parts = line.split(" ")
    dealWithAPerson(parts[0],people)
    dealWithAPerson(parts[10][0:len(parts[10])-1], people)
    dealWithHappiness(people[parts[0]], people[parts[10][0:len(parts[10])-1]], parts[2] , parts[3], happiness)


printMatrix(happiness)