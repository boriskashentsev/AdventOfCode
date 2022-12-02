import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

# Part 1

cross = {"A": {"X": 3, "Y": 6, "Z":0},
         "B": {"X": 0, "Y": 3, "Z":6},
         "C": {"X": 6, "Y": 0, "Z":3}}

choice = {"X": 1, "Y": 2, "Z":3}

scores = 0

for line in lines:
  enemy = line[0]
  hero = line[2]
  scores += cross[enemy][hero] + choice[hero]

print("Part 1: ", scores)

# Part 2

cross = {"A": {"X": "Z", "Y": "X", "Z":"Y"},
         "B": {"X": "X", "Y": "Y", "Z":"Z"},
         "C": {"X": "Y", "Y": "Z", "Z":"X"}}

choice = {"X": 1, "Y": 2, "Z":3}
score = {"X": 0, "Y": 3, "Z":6}

scores = 0

for line in lines:
  enemy = line[0]
  outcome = line[2]
  scores += score[outcome] + choice[cross[enemy][outcome]]

print("Part 2: ", scores)