import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

def velocityFormula(first, second) -> int:
  if second-first == 0:
    return 0
  return int((second-first)/(abs(second-first)))

class Planet:
  def __init__(self, xyz) -> None:
    self.coordinates = xyz
    self.velocity = [0, 0, 0]
  
  def adjustVelocity(self, anotherPosition) -> None:
    self.velocity = [self.velocity[i] + velocityFormula(value, anotherPosition[i]) for i,value in enumerate(self.coordinates)]

  def step(self) -> None:
    self.coordinates = [value + self.velocity[i] for i,value in enumerate(self.coordinates)]

  def energy(self) -> int:
    resultCoordinates = 0
    resultVelocity = 0
    for i in range(len(self.coordinates)):
      resultCoordinates += abs(self.coordinates[i])
      resultVelocity += abs(self.velocity[i])
    return resultCoordinates*resultVelocity
  
  def print(self) -> None:
    print('Coordinates: ', self.coordinates)
    print('Velocity:    ', self.velocity)

planets = []
for line in lines:
  coordinates = [int(part.split('=')[1]) for part in line[1:len(line)-1].split(',')]
  planets.append(Planet(coordinates))

steps = 0

while True:
  for i in range (len(planets) - 1):
    for j in range(i+1, len(planets)):
      planets[i].adjustVelocity(planets[j].coordinates)
      planets[j].adjustVelocity(planets[i].coordinates)
  
  for planet in planets:
    planet.step()

  totalEnergy = 0
  for planet in planets:
    totalEnergy += planet.energy()
  
  if totalEnergy == 0:
    break

  steps += 1
  if steps % 1000000 == 0: 
    print(steps, totalEnergy)
  
print('Part 2: ', (steps+1)*2)