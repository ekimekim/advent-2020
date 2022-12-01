import sys

x, y = 0, 0

for line in sys.stdin:
	cmd, n = line.strip().split()
	n = int(n)
	dx, dy = {
		'forward': (n, 0),
		'down': (0, n),
		'up': (0, -n),
	}[cmd]
	x += dx
	y += dy

print x * y
