filename = "2021/06.input"
f = open(filename, "r")
input = f.read()

ages = list(map(lambda x: int(x),input.split(",")))

# Part 1 (too slow for Part 2)

numberOfDays = 80

for i in range(numberOfDays):
    newFishes = ages.count(0)
    ages = list(map(lambda x: 6 if x == 0 else x - 1, ages))
    ages = ages + [8]*newFishes

print("Part 1", len(ages))

# Part 2

numberOfDifferentAges = 9
ages = list(map(lambda x: int(x),input.split(",")))

numberOfDays = 256

daysOfExperiment = [[1]*numberOfDifferentAges]

for i in range(numberOfDays):
    currentDay = []
    for j in range(numberOfDifferentAges):
        if j == 0:
            currentDay += [daysOfExperiment[i][6]+daysOfExperiment[i][8]]
        else:
            currentDay += [daysOfExperiment[i][j-1]]
    daysOfExperiment.insert(len(daysOfExperiment), currentDay)

result = 0
for age in ages:
    result += daysOfExperiment[-1][age]

print("Part 2", result)


