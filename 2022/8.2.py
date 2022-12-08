import sys
import itertools

grid = [
	map(int, line)
	for line in sys.stdin.read().strip().split("\n")
]

width = len(grid[0])
height = len(grid)

def walk(x, y, dx, dy):
	target = grid[y][x]
	count = 0
	x += dx
	y += dy
	while 0 <= x < width and 0 <= y < height:
		here = grid[y][x]
		count += 1
		if target <= here:
			break
		x += dx
		y += dy
	return count

def score((x, y)):
	left = walk(x, y, 1, 0)
	right = walk(x, y, -1, 0)
	up = walk(x, y, 0, 1)
	down = walk(x, y, 0, -1)
	return left * right * up * down

print max(map(score, itertools.product(range(width), range(height))))
