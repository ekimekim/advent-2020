
import sys
import itertools

grid = sys.stdin.read().strip().split("\n")

DIRS = [
	(0, -1),
	(1, 0),
	(0, 1),
	(-1, 0),
]

UP, RIGHT, DOWN, LEFT = DIRS

def next(x, y, dir):
	c = grid[y][x]
	rev_dir = -dir[0], -dir[1]
	dirs_by_char = {
		"|": (UP, DOWN),
		"-": (LEFT, RIGHT),
		"L": (UP, RIGHT),
		"J": (UP, LEFT),
		"7": (DOWN, LEFT),
		"F": (DOWN, RIGHT),
		".": (),
		"S": (UP, DOWN, LEFT, RIGHT),
	}
	dirs = [d for d in dirs_by_char[c] if d != rev_dir]
	print x, y, dir, c, dirs
	if len(dirs) != 1:
		return None
	new_dir = dirs[0]
	dx, dy = new_dir
	print x, y, dir, c, "->", x + dx, y + dy, new_dir
	return x + dx, y + dy, new_dir

for y, line in enumerate(grid):
	if "S" in line:
		sx = line.index("S")
		sy = y
		break

for dir in DIRS:
	dx, dy = dir
	x = sx + dx
	y = sy + dy
	if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
		continue
	# for each direction, make sure it makes sense to come from start to that square
	result = next(sx + dx, sy + dy, dir)
	if result is not None:
		sdir = dir
		break

x = sx + sdir[0]
y = sy + sdir[1]
dir = sdir
for step in itertools.count():
	if grid[y][x] == "S":
		break
	x, y, dir = next(x, y, dir)

print (step + 1)/2
