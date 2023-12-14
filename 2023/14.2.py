import sys
import itertools

grid = [list(line) for line in sys.stdin.read().strip().split("\n")]

def roll(dir):
	dx, dy = {
		"N": (0, -1),
		"S": (0, 1),
		"E": (1, 0),
		"W": (-1, 0),
	}[dir]
	order = {
		"N": lambda (x, y): (y, x),
		"S": lambda (x, y): (-y, x),
		"E": lambda (x, y): (-x, y),
		"W": lambda (x, y): (x, y),
	}[dir]
	width = len(grid[0])
	height = len(grid)
	coords = itertools.product(range(width), range(height))
	for x, y in sorted(coords, key=order):
		if grid[y][x] != 'O':
			continue
		nx, ny = (x, y)
		while (
			(0 <= nx + dx < width)
			and (0 <= ny + dy < height)
			and grid[ny + dy][nx + dx] == "."
		):
			nx += dx
			ny += dy
		grid[y][x] = '.'
		grid[ny][nx] = 'O'

states = {} # grid: cycle number
for n in itertools.count():
	grid_copy = tuple(tuple(line) for line in grid)
	if grid_copy in states:
		start = states[grid_copy]
		length = n - start
		break
	states[grid_copy] = n
	roll('N')
	roll('W')
	roll('S')
	roll('E')

target = 1000000000
offset = (1000000000 - start) % length
print "loop of", length, "from", start, "so cycle", target, "is at loop offset", offset, "at state", offset + start
grid = [state for state, n in states.items() if n == offset + start][0]

print sum(
	len(grid) - y
	for y, line in enumerate(grid)
	for c in line
	if c == 'O'
)
