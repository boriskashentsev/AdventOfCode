import sys
sys.path.append('./')
from utils.filename import calculateFileName
from functools import cmp_to_key

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

lines = input.split('\n')

class Node:

    def __init__(self, name, weight, trash):
        self.name = name
        self.weight = weight
        self.children = []
        self.trash = trash

    def __repr__(self):
        return self.name + ' (' + str(self.weight) + ') -> ' + str(self.children) 
    
    def weightWithChildren(self):
        result = self.weight
        for child in self.children:
            result += child.weightWithChildren()
        return result

    def isBalanced(self):
        weights = []
        for child in self.children:
            weights.append(child.weightWithChildren())
        for i in range(len(weights)-1):
            if weights[i+1] != weights[i]:
                return False
        return True

    def findUnbalancedChild(self):
        if len(self.children) == 2:
            print("Well FUCK")
            return [-1, -1]
        weights = []
        for child in self.children:
            weights.append(child.weightWithChildren())
            #print(child.weightWithChildren())
        histogram = []
        for weight in weights:
            isWeightFound = False
            j = 0
            while j < len(histogram) and not isWeightFound:
                if histogram[j][0] == weight:
                    histogram[j][1] += 1
                    isWeightFound = True
                j += 1
            if not isWeightFound:
                histogram += [[weight, 1]]
        uniqueWeight = -1
        nonUniqueWeight = -1
        for element in histogram:
            if element[1] == 1:
                uniqueWeight = element[0]
            else:
                nonUniqueWeight = element[0]
        for i in range(len(weights)):
            if weights[i] == uniqueWeight:
                return [i, nonUniqueWeight]
    
    def balance(self, correctWeight):
        if not self.isBalanced():
            [index, correctWeight] = self.findUnbalancedChild()
            if index >= 0:
                return self.children[index].balance(correctWeight)
            else:
                print("I don't know what to do yet")
        else:
            childrenWeight = 0
            for child in self.children:
                childrenWeight += child.weightWithChildren()
            return correctWeight - childrenWeight



class LinkedTree:
    def __init__(self):
        self.head = None
        self.branches = []
    
    def __repr__(self):
        return str(self.head)

    def buildTree(self):
        for branch in self.branches:
            if branch[0].trash != None:
                for element in branch[0].trash:
                    child = None
                    for branchChild in self.branches:
                        if branchChild[0].name == element:
                            child = branchChild[0]
                            branchChild[1] = True
                            break
                    branch[0].children.append(child)
                    branch[0].trash = None
        for branch in self.branches:
            if not branch[1]:
                self.head = branch[0]
        self.branches = []

    def balanceTree(self):
        return self.head.balance(0)



tree = LinkedTree()

for line in lines:
    parts = line.split(' -> ')
    nameAndWeight = parts[0].split(' (')
    trash = None
    if (len(parts) == 2):
        trash = parts[1].split(', ')
    name = nameAndWeight[0]
    weight = int(nameAndWeight[1][:-1])
    branch = Node(name, weight, trash)
    tree.branches.append([branch, False]) # information about the Node and if parent has been found

tree.buildTree()

print(tree.head.name)

print(tree.balanceTree())