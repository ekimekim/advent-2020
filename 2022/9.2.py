
import sys

def sign(x):
	return cmp(x, 0)

rope = [[0, 0] for _ in range(10)]
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
		rope[0][0] += hdx
		rope[0][1] += hdy
		for prev, here in zip(rope, rope[1:]):
			dx = prev[0] - here[0]
			dy = prev[1] - here[1]
			if abs(dx) > 1 or abs(dy) > 1:
				here[0] += sign(dx)
				here[1] += sign(dy)
		visited.add(tuple(rope[-1]))

print len(visited)
