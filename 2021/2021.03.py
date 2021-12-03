filename = "2021/03.input"

f = open(filename, "r")

input = f.read().split("\n")

# Part 1
histogram = []
for i in range(len(input[0])):
    histogram = histogram + [[0,0]]

for line in input:
    for i in range(len(line)):
        histogram[i][int(line[i])] += 1

gamma = 0
epsilon = 0

for position in histogram:
    if position[0] > position[1]:
        gamma = gamma * 2
        epsilon = epsilon * 2 + 1
    else:
        gamma = gamma * 2 + 1
        epsilon = epsilon * 2

print(gamma*epsilon)

# Part 2

oxStr = ""
co2Str = ""
for position in range(len(input[0])):
    histogramO = [0,0]
    histogramCO2 = [0,0]
    for line in input:
        if line.startswith(oxStr):
            histogramO[int(line[position])] += 1
        if line.startswith(co2Str):
            histogramCO2[int(line[position])] += 1
    
    if histogramO[0] > histogramO[1]:
        oxStr += "0"
    else:
        oxStr += "1"
    
    if ((histogramCO2[1] < histogramCO2[0] and histogramCO2[1] > 0) or (histogramCO2[1]>0 and histogramCO2[0]==0)):
        co2Str += "1"
    else:
        co2Str += "0"

print(oxStr, co2Str)
ox = 0
co2 = 0
for i in range(len(oxStr)):
    ox = ox*2 + int(oxStr[i])
    co2 = co2*2 + int(co2Str[i])

print(ox*co2)