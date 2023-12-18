
import sys

lines = sys.stdin.read().strip().split("\n")
outline = {} # (x, y): color
x = 0
y = 0
for line in lines:
	dir, steps, color = line.split()
	dx, dy = {
		"U": (0, -1),
		"D": (0, 1),
		"L": (-1, 0),
		"R": (1, 0),
	}[dir]
	for _ in range(int(steps)):
		x += dx
		y += dy
		outline[x, y] = color

assert x == 0 and y == 0

min_x = min(x for x, y in outline)
max_x = max(x for x, y in outline)
min_y = min(y for x, y in outline)
max_y = max(y for x, y in outline)

inside = set()
outside = set()
for x in range(min_x, max_x + 1):
	for y in range(min_y, max_y + 1):
		current = set()
		queue = [(x, y)]
		is_outside = False
		while queue:
			x, y = queue.pop()
			if (x, y) in outside:
				is_outside = True
				continue
			if x < min_x or x > max_x or y < min_y or y > max_y:
				is_outside = True
				continue
			if (x, y) in inside or (x, y) in current or (x, y) in outline:
				continue
			current.add((x, y))
			for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
				queue.append((x + dx, y + dy))
		if is_outside:
			outside |= current
		else:
			inside |= current

DEBUG_X = -100
for y in range(min_y, max_y + 1):
	print "".join(
		("\x1b[31m" if x == DEBUG_X else "")
		+ (
			"o" if (x, y) in outline else
			"i" if (x, y) in inside else
			"."
		) + "\x1b[m"
		for x in range(min_x, max_x + 1)
	)

running = 0
for x in range(min_x, max_x + 1):
	count = len([1 for ix, iy in inside if ix == x])
	running += count
	print "x = {}: {} (total {})".format(x, count, running)

print "inside", len(inside)
print "outline", len(outline)
print len(inside) + len(outline)
