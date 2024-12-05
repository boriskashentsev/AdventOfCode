# Part 1

input = 356

buffer = [0]
steps = 2017
index = 0

for i in range(steps):
  index = (index + input) % len(buffer) + 1
  buffer = buffer[:index]+[i+1]+buffer[index:]

print("Part 1: ", buffer[index + 1])

# Part 2

steps = 50000000
index = 0
afterZero = 0

for i in range(steps):
  index = (index + input) % (i+1) + 1
  if index == 1:
    afterZero = i+1

print("Part 2: ", afterZero)