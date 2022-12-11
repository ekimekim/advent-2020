
import sys

def sign(x):
	return cmp(x, 0)

hx = hy = tx = ty = 0
visited = {(0, 0)}
for line in sys.stdin.read().strip().split("\n"):
	dir, steps = line.split()
	hdx, hdy = {
		'U': (0, 1),
		'D': (0, -1),
		'R': (1, 0),
		'L': (-1, 0),
	}[dir]
	steps = int(steps)
	for step in range(steps):
		hx += hdx
		hy += hdy
		dx = hx - tx
		dy = hy - ty
		if abs(dx) > 1 or abs(dy) > 1:
			tx += sign(dx)
			ty += sign(dy)
			visited.add((tx, ty))

print len(visited)
