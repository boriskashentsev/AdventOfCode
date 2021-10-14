def esclength(line):
    ind = 1
    length = 0
    while ind < len(line) - 1:
        length += 1
        if line[ind] == "\\":
            if line[ind+1] =="x":
                ind += 4
            else:
                ind += 2
        else:
            ind += 1
    return length

def encode(line):
    result = "\""
    for char in line:
        if char =="\"":
            result += "\\\""
        elif char == "\\":
            result += "\\\\"
        else :
            result += char
    result += "\""
    #print(result)
    return result

filename = "2015/8.input"

f = open(filename, "r")

inpt = f.read().split("\n")

# Part 1

result = 0
for line in inpt:
    #print(line)
    result += len(line) - esclength(line)

print(result)

# Part 2

result = 0
for line in inpt:
    result += len(encode(line)) - len(line)

print (result)
