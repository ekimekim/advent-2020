import sys

x, y = 0, 0
aim = 0

for line in sys.stdin:
	cmd, n = line.strip().split()
	n = int(n)
	dx, dy, da = {
		'forward': (n, aim * n, 0),
		'down': (0, 0, n),
		'up': (0, 0, -n),
	}[cmd]
	x += dx
	y += dy
	aim += da

print x * y
