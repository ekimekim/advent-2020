import sys

grid = {
	(x, y): c
	for y, line in enumerate(sys.stdin.read().strip().split("\n"))
	for x, c in enumerate(line)
}

start, = [coord for coord, c in grid.items() if c == 'S']
end, = [coord for coord, c in grid.items() if c == 'E']
grid[start] = 'a'
grid[end] = 'z'

def candidates((cx, cy)):
	for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
		x = cx + dx
		y = cy + dy
		if (x, y) not in grid:
			continue
		if ord(grid[x, y]) - ord(grid[cx, cy]) > 1:
			continue
		yield x, y

to_visit = [(start, 0)]
seen = set()
while True:
	current, steps = to_visit.pop(0)
	if current in seen:
		continue
	seen.add(current)
	if current == end:
		print steps
		break
	for candidate in candidates(current):
		to_visit.append((candidate, steps + 1))
