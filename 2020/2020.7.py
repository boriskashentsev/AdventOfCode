filename = "2020/7.input"

f = open(filename, "r")

inpt = f.read().split("\n")

bagsConnection = {}

for line in inpt:
    bagConnection = {}
    parts = line.split(" ")

    key = parts[0] + " " + parts[1]
    i = 4
    while i < len(parts):
        if parts[i] != "no":
            bagConnection[parts[i+1]+" "+parts[i+2]] = int(parts[i])
        i = i + 4
    bagsConnection[key] = bagConnection

#first part

neededBags = ["shiny gold"]
bagsContainingNeededBag = []

while len(neededBags) > 0:
    neededBag = neededBags.pop()
    for key in bagsConnection.keys():
        if neededBag in bagsConnection[key].keys():
            if key not in bagsContainingNeededBag:
                neededBags.append(key)
                bagsContainingNeededBag.append(key)

#print(len(bagsContainingNeededBag))

#second part

def goDeeper(tree, bag):
    if len(tree[bag].keys()) == 0:
        return 0
    else:
        answer = 0
        for key in tree[bag].keys():
            answer = answer + tree[bag][key] * (goDeeper(tree, key) + 1)
        return answer


neededBag = "shiny gold"


print(goDeeper(bagsConnection, neededBag))