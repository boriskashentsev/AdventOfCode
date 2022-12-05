import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

# Part 1
###
# Current solution is rather slow
###

values = []
for line in lines:
  values.append(int(line.split(' ')[-1]))

factors = [16807, 48271]
module = pow(2,16)


numberOfCompares = 40000000 
result = 0
for i in range(numberOfCompares):
  # if i% 1000000 == 0:
  #   print("... round ", i)
  for j in range(2):
    values[j] = values[j]*factors[j] % 2147483647
  if values[0]%module == values[1]%module:
    result += 1

# print("Part 1: ", result)

# Part 2
###
# Current solution is less slow, but might be improved somehow
###

multiples = [4, 8]

numberOfCompares = 5000000
result = 0
for i in range(numberOfCompares):
  # if i% 500000 == 0:
  #   print("... round ", i)
  for j in range(2):
    number = values[j]*factors[j] % 2147483647
    while number % multiples[j] != 0:
      number = number * factors[j] % 2147483647
    values[j] = number
  if values[0]%module == values[1]%module:
    result += 1

print("Part 1: ", result)