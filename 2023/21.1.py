
import sys

grid = sys.stdin.read().strip().split("\n")

for y, line in enumerate(grid):
	for x, c in enumerate(line):
		if c == "S":
			sx = x
			sy = y

width = len(grid[0])
height = len(grid)

queue = [(0, sx, sy)]
seen = set()
result = 0
while queue:
	steps, x, y = queue.pop(0)
	if (x, y) in seen:
		continue
	seen.add((x, y))
	if steps % 2 == 0:
		result += 1
	if steps == 64:
		continue
	for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
		nx = x + dx
		ny = y + dy
		if nx < 0 or ny < 0 or nx >= width or ny >= height or grid[ny][nx] == "#":
			continue
		queue.append((steps + 1, nx, ny))

print result
