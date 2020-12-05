def converTicket2Id(code):
    number = 0
    for bit in code:
        if bit == "B" or bit == "R":
            number = number * 2 + 1
        elif bit == "F" or bit == "L":
            number = number * 2
        else:
            print("Which bit is that", bit)
    return number



filename = "2020/5.input"

f = open(filename, "r")

inpt = f.read().split("\n")

#first part

""" maxId = 0
for line in inpt:
    number = converTicket2Id(line)
    if number > maxId:
        maxId = number

print ("Max", maxId) """

#second part
maxId = 0
minId = 1024
idSum = 0
for line in inpt:
    number = converTicket2Id(line)
    if number > maxId:
        maxId = number
    if number < minId:
        minId = number
    idSum = idSum + number
    

fullSum = 0
for i in range(minId, maxId+1):
    fullSum = fullSum + i
print ("missing id", fullSum - idSum)