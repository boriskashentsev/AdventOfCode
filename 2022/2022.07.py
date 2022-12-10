import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

class Folder:

  def __init__(self, name='', upFolder=None):
    self.name: str = name
    self.files: list = []
    self.folders: list = []
    self.upFolder: Folder = upFolder

  def __repr__(self):
    line = self.name + '\n'
    for folder in self.folders:
      line += '**' + folder.name + '\n'
    for file in self.files:
      line += '..' + file.getName() + ' - ' + str(file.getSize()) + '\n'
    return line
  
  def addName(self, name: str):
    self.name = name
  
  def getName(self):
    return self.name

  def addFile(self, file: 'File'):
    self.files.append(file)
  
  def addFolder(self, folder: 'Folder'):
    self.folders.append(folder)
  
  def getFolders(self):
    return self.folders
  
  def setUpFolder(self, folder: 'Folder'):
    self.upFolder = folder

  def getUpFolder(self):
    return self.upFolder

  def sizeOfFolder(self):
    size = 0
    for file in self.files:
      size += file.getSize()
    for folder in self.folders:
      size += folder.sizeOfFolder()
    return size

class File:
  def __init__(self, name, size):
    self.name = name
    self.size = size
  
  def __repr__(self):
    return 'File '+ self.name + ' with size ' + self.size
  
  def getName(self):
    return self.name

  def getSize(self):
    return self.size

def findFolders(folder: Folder, folders: list, folderSize: int, smallerOfBigger: str = 'smaller'):
  if folder.sizeOfFolder() == folderSize:
    print("We got exact number")
  if smallerOfBigger == 'smaller':
    if folder.sizeOfFolder() < folderSize:
      folders.append(folder)
  else:
      if folder.sizeOfFolder() >= folderSize:
        folders.append(folder)
  for subfolder in folder.getFolders():
    folders = findFolders(subfolder, folders, folderSize, smallerOfBigger)
  return folders

# Part 1

mainFolder = Folder()
currentFolder = None
lineNumber = 0

while lineNumber < len(lines):
  parts = lines[lineNumber].split(' ')
  if parts[0] == '$':
    if parts[1] == 'cd':
      if parts[2] == '/':
        mainFolder.addName(parts[2])
        currentFolder = mainFolder
      elif parts[2] == '..':
        currentFolder = currentFolder.getUpFolder()
      else:
        for folder in currentFolder.getFolders():
          if folder.getName() == parts[2]:
            currentFolder = folder
            break
      lineNumber += 1
    elif parts[1] == 'ls':
      stillFolderList = True
      lineNumber +=1
      while stillFolderList and lineNumber < len(lines):
        parts = lines[lineNumber].split(' ')
        if parts[0] == 'dir':
          currentFolder.addFolder(Folder(parts[1], currentFolder))
        elif parts[0] == '$':
          stillFolderList = False
          lineNumber -= 1
        else:
          currentFolder.addFile(File(parts[1], int(parts[0])))
        lineNumber +=1
  else:
    print(">>> How did we get here??")

smallFolders = findFolders(mainFolder, [], 100000)

accumulatedSize = 0
for folder in smallFolders:
  accumulatedSize += folder.sizeOfFolder()

print("Part 1: ", accumulatedSize)

# Part 2

fullDiskSize = 70000000
neededSpace = 30000000

freeSpace = fullDiskSize - mainFolder.sizeOfFolder()

if freeSpace < neededSpace:
  folders = findFolders(mainFolder, [], neededSpace-freeSpace, 'bigger')
  minFolderSize = folders[0].sizeOfFolder()
  for folder in folders:
    if minFolderSize > folder.sizeOfFolder():
      minFolderSize = folder.sizeOfFolder()
  print("Part 2: ", minFolderSize)
else:
  print("Part 2: we already have enough space for the update")
