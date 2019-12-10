class node:
    parent = False
    name = ""
    depth = 0
    children = []
    def introduction(self):
        return "Name: " + self.name + "\n  Depth: " + str(self.depth) + "\n  Parent: " + str(self.parent) + "\n  # of children: " + str(len(self.children))

def calucateDepth(element, dictionary, depth):
    if element.parent != False :
        element.depth = dictionary[element.parent].depth + 1
        depth += element.depth
    
    for child in element.children:
        depth = calucateDepth(child, dictionary, depth)
    return depth

#filename = "2019/2019.6.test1.input"
filename = "2019/2019.6.input"

f = open(filename, "r")

inpt = f.read().split("\n")

dictionary = {}

for line in inpt:
    parts = line.split(")")
    if parts[1] not in dictionary:
        newNode = node()
        newNode.name = parts[1]
        newNode.parent = parts[0]
        newNode.children = []
        dictionary[parts[1]] = newNode
    else:
        dictionary[parts[1]].parent = parts[0]

    if parts[0] not in dictionary:
        newNode = node()
        newNode.name = parts[0]
        newNode.children = []
        dictionary[parts[0]] = newNode
    dictionary[parts[0]].children.append(dictionary[parts[1]])

root = False

for value in dictionary.values():
    if not value.parent:
        root = value
        
# print root.introduction()
# depth = 0
# depth = calucateDepth(root, dictionary, depth)
# print depth

you = dictionary["YOU"]
san = dictionary["SAN"]

routeYou = []
routeSan = []

while (you.parent):
    routeYou.insert(0, you.name)
    you = dictionary[you.parent]

while (san.parent):
    routeSan.insert(0, san.name)
    san = dictionary[san.parent]

print routeYou
print routeSan

i = 0
while (routeSan[i] == routeYou[i]):
    i += 1

print len(routeYou) + len(routeSan) - 2*i - 2