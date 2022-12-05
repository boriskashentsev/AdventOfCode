import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

alphabet = 'abcdefghijklmnopqrstuvqxyz'

moves = input.split(',')

numberOfPrograms = 16

programs = list(alphabet)[:numberOfPrograms]
# Part 1

def doTheDance(programs, moves):
  for move in moves:
    if move[0] == 's':
      programs = programs[-int(move[1:]):]+programs[:len(programs)-int(move[1:])]
    elif move[0] == 'x':
      indices = list(map(lambda x: int(x), move[1:].split('/')))
      buffer = programs[indices[1]]
      programs[indices[1]] = programs[indices[0]]
      programs[indices[0]] = buffer
    elif move[0] == 'p':
      string = ''.join(programs)
      programsToFind = move[1:].split('/')
      indices=[]
      for element in programsToFind:
        indices.append(string.find(element))
      buffer = programs[indices[1]]
      programs[indices[1]] = programs[indices[0]]
      programs[indices[0]] = buffer
  return programs

programs = doTheDance(programs, moves)

print("Part 1: ", ''.join(programs))

# Part 2

###
# Observing first 1000 dances, I noticed that there is a pattern, that repeats every 48 dances
###

programs = list(alphabet)[:numberOfPrograms]
for i in range(1000000000%48):
  newPrograms = doTheDance(programs, moves)
  programs = newPrograms

print("Part 2: ", ''.join(programs))