filename = "2021/07.input"
f = open(filename, "r")
input = f.read()

positions = list(map(lambda x: int(x),input.split(",")))

minPosition = min(positions)
maxPosition = max(positions)

# Part 1

minFuel = -1

for i in range(minPosition, maxPosition + 1):
    fuel = 0
    for position in positions:
        fuel += abs(i-position)
    if fuel < minFuel or minFuel < 0:
        minFuel = fuel

print(minFuel)

# Part 2

minFuel = -1
fuelSpent = [0]
for i in range(1, maxPosition - minPosition +1 ):
    fuelSpent += [fuelSpent[-1]+i]

for i in range(minPosition, maxPosition + 1):
    fuel = 0
    for position in positions:
        fuel += fuelSpent[abs(i-position)]
    if fuel < minFuel or minFuel < 0:
        minFuel = fuel

print(minFuel)
