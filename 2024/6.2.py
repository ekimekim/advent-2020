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
assert gx is not None

def get_visited(gy, gx, gd, oy=None, ox=None):
	visited = set()
	while (gy, gx, gd) not in visited:
		visited.add((gy, gx, gd))
		dy, dx = DIRS[gd]
		ny = gy + dy
		nx = gx + dx
		if not ((0 <= ny < len(grid)) and (0 <= nx < len(grid[ny]))):
			# left grid, return visited
			return set((y, x) for y, x, d in visited)
		elif (ny, nx) == (oy, ox) or grid[ny][nx] == "#":
			# obstacle, turn right
			gd = (gd + 1) % 4
		else:
			# move forward
			gy, gx = ny, nx
	# found loop
	return None

candidates = get_visited(gy, gx, gd) - {(gy, gx)}
print(len([1 for oy, ox in candidates if get_visited(gy, gx, gd, oy, ox) is None]))
