import sys

grid = sys.stdin.read().strip().split("\n")

word = "XMAS"
found = 0
for y, line in enumerate(grid):
	for x, _ in enumerate(line):
		for dy in (-1, 0, 1):
			for dx in (-1, 0, 1):
				for n, c in enumerate(word):
					cx = x + n * dx
					cy = y + n * dy
					if (0 <= cy < len(grid)) and (0 <= cx < len(grid[cy])) and grid[cy][cx] == c:
						continue
					break
				else:
					found += 1

print(found)
