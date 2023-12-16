
import sys

grid = sys.stdin.read().strip().split("\n")

UP, RIGHT, DOWN, LEFT = range(4)

queue = [(0, 0, RIGHT)]
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

energized = set((x, y) for x, y, dir in done)
print len(energized)
