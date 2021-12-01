filename = "2021/01.input"

f = open(filename, "r")

input = f.read().split("\n")
depths = list(map(lambda x: int(x), input))

# First part

result = 0
for i in range(len(depths)-1):
    if(depths[i+1]>depths[i]):
        result += 1
print(result)

# Second part

newDepths = list(map(lambda x,y,z: x+y+z, depths[:len(depths)-2], depths[1:len(depths)-1], depths[2:]))

result = 0
for i in range(len(newDepths)-1):
    if(newDepths[i+1]>newDepths[i]):
        result += 1
print(result)