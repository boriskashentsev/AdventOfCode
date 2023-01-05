import sys
sys.path.append('./')

from utils.filename import calculateFileName
from math import cos, acos, sqrt, pi

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

def gcd(a:int,b:int) -> int:
  minValue = min([abs(a),abs(b)])
  maxValue = max([abs(a),abs(b)])
  if minValue == 0:
    return abs(maxValue)
  for i in reversed(range(1,minValue+1)):
    if a%i == 0 and b%i == 0:
      return i

class Asteroid:
  def __init__(self, x: int, y: int) -> None:
    self.position = {'x': x, 'y':y}
    self.visibleDirections = {}
  
  def checkVisibility(self, location: dict) -> None:
    dx = location['x'] - self.position['x']
    dy = location['y'] - self.position['y']
    gcdValue = gcd(dx, dy)
    key = ' '.join(str(x) for x in [dx // gcdValue, dy // gcdValue])
    if not(key in self.visibleDirections.keys()):
      self.visibleDirections[key] = [[dx, dy]]
    else:
      self.visibleDirections[key].append([dx,dy])
      self.visibleDirections[key] = sorted(self.visibleDirections[key], key = lambda x: x[0]*x[0]+x[1]*x[1])

  
  def getPosition(self) -> dict:
    return self.position
  
  def getVisibilityDirections(self) -> dict:
    return self.visibleDirections

  def getVisibilityLen(self) -> int:
    return len(self.visibleDirections.keys())

  def isAnythingToDestroy(self, key) -> bool:
    return len(self.visibleDirections[key]) > 0

  def destroyAsteroid(self, key) -> list:
    return self.visibleDirections[key].pop(0)

# Part 1

asteroids: list = []

for y, line in enumerate(input.split('\n')):
  for x, position in enumerate(list(line)):
    if position == '#':
      newAsteroid = Asteroid(x, y)
      for oldAsteroid in asteroids:
        newAsteroid.checkVisibility(oldAsteroid.getPosition())
        oldAsteroid.checkVisibility(newAsteroid.getPosition())
      asteroids.append(newAsteroid)

maxVisibilityLen = 0
spaceStation : Asteroid = None

for asteroid in asteroids:
  if asteroid.getVisibilityLen() > maxVisibilityLen:
    maxVisibilityLen = asteroid.getVisibilityLen()
    spaceStation = asteroid


print("Part 1: ", maxVisibilityLen)

# Part 2

# print(spaceStation.getPosition())
keys = []
for key in spaceStation.getVisibilityDirections().keys():
  x0 = 0
  y0 = -1
  [x1, y1] = map(lambda x: int(x),key.split(' '))
  angle = acos((x0*x1 + y0*y1)/sqrt((x0*x0+y0*y0)*(x1*x1+y1*y1)))*180/pi
  if x1 < 0:
    angle = 360 - angle
  keys.append([key, angle])
  
keys = sorted(keys, key = lambda x: x[1])

# print(keys)
index = 0

# print(spaceStation.getVisibilityDirections())

asteroidsToDestroy = 200

for i in range(asteroidsToDestroy):
  while(not spaceStation.isAnythingToDestroy(keys[index][0])):
    index = (index + 1) % len(keys)
  station = spaceStation.destroyAsteroid(keys[index][0])
  index = (index + 1) % len(keys)

print("Part 2: ", (station[0] + spaceStation.getPosition()['x'])*100 + station[1] + spaceStation.getPosition()['y'])


