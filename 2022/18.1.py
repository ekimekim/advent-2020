
import sys

cubes = set(
	tuple(map(int, line.split(",")))
	for line in sys.stdin.read().strip().split("\n")
)

SIDES = [
	(0, 0, -1),
	(0, 0, 1),
	(0, -1, 0),
	(0, 1, 0),
	(-1, 0, 0),
	(1, 0, 0),
]

count = 0
for x, y, z in cubes:
	for dx, dy, dz in SIDES:
		if (x + dx, y + dy, z + dz) not in cubes:
			count += 1

print count
