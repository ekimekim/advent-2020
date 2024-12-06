import sys

UP, RIGHT, DOWN, LEFT = range(4)
DIRS = {
	UP: (-1, 0),
	RIGHT: (0, 1),
	DOWN: (1, 0),
	LEFT: (0, -1),
}

grid = [list(line) for line in sys.stdin.read().strip().split("\n")]
gy, gx, gd = None, None, UP
for y, line in enumerate(grid):
	for x, c in enumerate(line):
		if c == '^':
			assert gx is None
			gy = y
			gx = x
			grid[y][x] = "." # replace guard with empty space
assert gx is not None

visited = set()
while True:
	visited.add((gy, gx))
	dy, dx = DIRS[gd]
	ny = gy + dy
	nx = gx + dx
	if not ((0 <= ny < len(grid)) and (0 <= nx < len(grid[ny]))):
		# left grid
		break
	elif grid[ny][nx] == "#":
		# obstacle, turn right
		gd = (gd + 1) % 4
	else:
		# move forward
		gy, gx = ny, nx

print(len(visited))
