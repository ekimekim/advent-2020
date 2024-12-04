import sys

grid = sys.stdin.read().strip().split("\n")

found = 0
for y, line in enumerate(grid):
	for x, _ in enumerate(line):
		if grid[y][x] != "A":
			continue
		a, b = [
			"".join(
				grid[y + dy][x + dx] for dx, dy in ds
				if (0 <= y + dy < len(grid)) and (0 <= x + dx < len(grid[y]))
			) for ds in [[(-1, -1), (1, 1)], [(-1, 1), (1, -1)]]
		]
		if a in ("MS", "SM") and b in ("MS", "SM"):
			found += 1

print(found)
