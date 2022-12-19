
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

# bounding box with 1 padding on all sides
min_x = min(x for x, y, z in cubes) - 1
min_y = min(y for x, y, z in cubes) - 1
min_z = min(z for x, y, z in cubes) - 1
max_x = max(x for x, y, z in cubes) + 1
max_y = max(y for x, y, z in cubes) + 1
max_z = max(z for x, y, z in cubes) + 1
# start in top corner, BFS to fill
start = min_x, min_y, min_z
outside = set([start])
to_fill = [start]
while to_fill:
	x, y, z = to_fill.pop(0)
	for dx, dy, dz in SIDES:
		nx = x + dx
		ny = y + dy
		nz = z + dz
		if not all([
			min_x <= nx <= max_x,
			min_y <= ny <= max_y,
			min_z <= nz <= max_z,
		]):
			continue
		t = (nx, ny, nz)
		if t in cubes:
			continue
		if t in outside:
			continue
		outside.add(t)
		to_fill.append(t)

# now count edges that are in the outside set
count = 0
for x, y, z in cubes:
	for dx, dy, dz in SIDES:
		if (x + dx, y + dy, z + dz) in outside:
			count += 1

print count
