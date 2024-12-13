import sys

sys.path.append("./")
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

# Part 1

blinks = 25
stones = input.split(" ")
for i in range(blinks):
    newStones = []
    for stone in stones:
        if stone == "0":
            newStones.append("1")
        elif len(stone) % 2 == 0:
            newStones.append(stone[: int(len(stone) / 2)])
            newStones.append(str(int(stone[int(len(stone) / 2) :])))
        else:
            newStones.append(str(2024 * int(stone)))
    stones = newStones

print("Part 1: ", len(stones))

# Part 2


def goDeeper(stone: str, depth: int, maxDepth: int, stats: dict) -> int:
    if depth < maxDepth:
        if stone in stats.keys() and (maxDepth - depth) in stats[stone].keys():
            return stats[stone][maxDepth - depth]
        if stone not in stats.keys():
            stats[stone] = {}
        if stone == "0":
            value = goDeeper("1", depth + 1, maxDepth, stats)
            stats[stone][maxDepth - depth] = value
            return value
        elif len(stone) % 2 == 0:
            leftTree = goDeeper(
                stone[: int(len(stone) / 2)], depth + 1, maxDepth, stats
            )
            rightTree = goDeeper(
                str(int(stone[int(len(stone) / 2) :])), depth + 1, maxDepth, stats
            )
            stats[stone][maxDepth - depth] = leftTree + rightTree
            return leftTree + rightTree
        else:
            value = goDeeper(str(2024 * int(stone)), depth + 1, maxDepth, stats)
            stats[stone][maxDepth - depth] = value
            return value
    else:
        return 1


newBlinks = 75
stones = input.split(" ")
result = 0
statistics = {}
for i in range(len(stones)):
    result += goDeeper(stones[i], 0, newBlinks, statistics)
print()
print("Part 2: ", result)
