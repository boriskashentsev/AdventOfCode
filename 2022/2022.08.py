import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

# Part 1

treeGrid = []
for line in lines:
  treeGrid.append([int(x) for x in line])

def isVisible(grid, y, x):
  notVisible = 0
  # Visible from North
  for i in range(y):
    if grid[i][x] >= grid[y][x]:
      notVisible += 1
      break
  # Visible from West
  for i in range(x):
    if grid[y][i] >= grid[y][x]:
      notVisible += 1
      break
  # Visible from South
  for i in range(y+1, len(grid)):
    if grid[i][x] >= grid[y][x]:
      notVisible += 1
      break
  # Visible from East
  for i in range(x+1, len(grid[y])):
    if grid[y][i] >= grid[y][x]:
      notVisible += 1
      break
  if notVisible == 4:
    return False
  return True
  

visibleTrees = len(treeGrid) * 2 + (len(treeGrid[0])-2) * 2
print(visibleTrees)

for i in range(1, len(treeGrid)-1):
  for j in range(1, len(treeGrid[i])-1):
    if isVisible(treeGrid, i, j):
      visibleTrees += 1

print("Part 1: ", visibleTrees)

# Part 2

def scenicScore(grid, y, x):
  result = 1
  # Look to the North
  canSee = 0
  for i in range(y):
    canSee += 1
    if grid[y-i-1][x] >= grid[y][x]:
      break
  result *= canSee
  # Look to the West
  canSee = 0
  for i in range(x):
    canSee += 1
    if grid[y][x-i-1] >= grid[y][x]:
      break
  result *= canSee
  # Look to the South
  canSee = 0
  for i in range(y+1, len(grid)):
    canSee += 1
    if grid[i][x] >= grid[y][x]:
      break
  result *= canSee
  # Look to the East
  canSee = 0
  for i in range(x+1, len(grid[y])):
    canSee += 1
    if grid[y][i] >= grid[y][x]:
      break
  result *= canSee
  return result

maxScenicScore = 0
for i in range(1, len(treeGrid)-1):
  for j in range(1, len(treeGrid[i])-1):
    currentScenicScore = scenicScore(treeGrid, i, j)
    if maxScenicScore < currentScenicScore:
      maxScenicScore = currentScenicScore

print("Part 2: ", maxScenicScore)
