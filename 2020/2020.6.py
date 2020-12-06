filename = "2020/6.input"

f = open(filename, "r")

inpt = f.read().split("\n")

#first part
""" dictionary = {}
answer = 0
for line in inpt:
    if line == "":
        answer = answer + len(dictionary.keys())
        dictionary = {}
    else:
        for letter in line:
            if letter in dictionary.keys():
                dictionary[letter] = dictionary[letter] + 1
            else:
                dictionary[letter] = 1

answer = answer + len(dictionary.keys())

print(answer) """

#second part

dictionary = {}
answer = 0
peopleInGroup = 0
for line in inpt:
    if line == "":
        for key in dictionary.keys():
            if dictionary[key] == peopleInGroup:
                answer = answer + 1
        dictionary = {}
        peopleInGroup = 0
    else:
        peopleInGroup = peopleInGroup + 1
        for letter in line:
            if letter in dictionary.keys():
                dictionary[letter] = dictionary[letter] + 1
            else:
                dictionary[letter] = 1

for key in dictionary.keys():
    if dictionary[key] == peopleInGroup:
        answer = answer + 1

print(answer)