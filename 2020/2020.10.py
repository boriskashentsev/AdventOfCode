filename = "2020/10.input"

f = open(filename, "r")

inpt = f.read().split("\n")

adapters = [0]

for line in inpt:
    adapters.append(int(line))

# first part

adapters.sort()

adapters.append(adapters[-1]+3)

histogram = {}

for i in range(len(adapters)-1):
    key = adapters[i+1]-adapters[i]
    if key in histogram.keys() :
        histogram[key] = histogram[key] + 1
    else :
        histogram[key] = 1

print(histogram[1]*histogram[3])

# second part

diff = []
for i in range(len(adapters)-1):
    diff.append(adapters[i+1] - adapters[i])

value = 0
result = 1
multiplication= [1,1,2,4,7] # investigated, 4 is the maximum value of ones back to back in diff array
for i in range(len(diff)):
    if diff[i] == 1:
        value = value + 1
    elif diff[i] == 3:
        result = result * multiplication[value]
        value = 0
    else :
        print("What is that?")

print(result)