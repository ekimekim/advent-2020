import sys

grid = [list(line) for line in sys.stdin.read().strip().split("\n")]

for y, line in enumerate(grid):
	for x, c in enumerate(line):
		if c != 'O':
			continue
		empty = y
		while empty > 0 and grid[empty - 1][x] == ".":
			empty -= 1
		grid[y][x] = '.'
		grid[empty][x] = 'O'

print "\n".join("".join(line) for line in grid)

print sum(
	len(grid) - y
	for y, line in enumerate(grid)
	for c in line
	if c == 'O'
)
