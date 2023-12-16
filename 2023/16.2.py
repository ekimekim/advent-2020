
import sys

grid = sys.stdin.read().strip().split("\n")

UP, RIGHT, DOWN, LEFT = range(4)

def solve(sx, sy, sdir):
	queue = [(sx, sy, sdir)]
	done = set()
	while queue:
		x, y, dir = queue.pop()
		if not (
			(0 <= x < len(grid[0]))
			and (0 <= y < len(grid))
		):
			continue
		if (x, y, dir) in done:
			continue
		done.add((x, y, dir))
		c = grid[y][x]
		new_dirs = {
			'.': [dir],
			'/': [[RIGHT, UP, LEFT, DOWN][dir]],
			'\\': [[LEFT, DOWN, RIGHT, UP][dir]],
			'-': [LEFT, RIGHT] if dir in (UP, DOWN) else [dir],
			'|': [UP, DOWN] if dir in (LEFT, RIGHT) else [dir],
		}[c]
		for new_dir in new_dirs:
			dx, dy = [
				(0, -1),
				(1, 0),
				(0, 1),
				(-1, 0),
			][new_dir]
			queue.append((x + dx, y + dy, new_dir))

	return set((x, y) for x, y, dir in done)

width = len(grid[0])
height = len(grid)
print max(
	len(solve(x, y, dir))
	for x, y, dir in (
		[(0, y, RIGHT) for y in range(height)]
		+ [(width - 1, y, LEFT) for y in range(height)]
		+ [(x, 0, DOWN) for x in range(width)]
		+ [(x, height - 1, UP) for y in range(width)]
	)
)
