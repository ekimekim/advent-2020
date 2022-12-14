import sys

lines = sys.stdin.read().strip().split("\n")
rocks = set()
for line in lines:
	parts = line.split(" -> ")
	for a, b in zip(parts, parts[1:]):
		ax, ay = map(int, a.split(","))
		bx, by = map(int, b.split(","))
		if ax == bx:
			ay, by = sorted([ay, by])
			for y in range(ay, by + 1):
				rocks.add((ax, y))
		else:
			assert ay == by
			ax, bx = sorted([ax, bx])
			for x in range(ax, bx + 1):
				rocks.add((x, ay))

bottom = max(y for x, y in rocks) + 2
filled = set(rocks)
while True:
	sx, sy = 500, 0
	while sy < bottom:
		sy += 1
		if (sx, sy) not in filled:
			pass
		elif (sx - 1, sy) not in filled:
			sx -= 1
		elif (sx + 1, sy) not in filled:
			sx += 1
		else:
			# come to rest at prev position
			sy -= 1
			break
	else:
		# came to rest on bottom, at prev position
		sy -= 1
	filled.add((sx, sy))
	if (sx, sy) == (500, 0):
		break

print len(filled) - len(rocks)
