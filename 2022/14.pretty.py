import sys
import itertools

FRAMESKIP = 20

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
sx, sy = None, None

def draw():
	output = "\x1b[H\x1b[2J" + "\n".join(
		"".join(
			"\x1b[31mo" if (x, y) == (sx, sy) else
			"\x1b[34m#" if (x, y) in rocks else
			"\x1b[33mo" if (x, y) in filled else
			"\x1b[31m+" if (x, y) == (500, 0) else
			" "
			for x in range(500 - bottom - 1, 500 + bottom + 2)
		) for y in range(bottom)
	) + "\x1b[m"
	sys.stdout.write(output)
	sys.stdout.flush()

for i in itertools.count():
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
	if i % FRAMESKIP == 0:
		draw()
	filled.add((sx, sy))
	if (sx, sy) == (500, 0):
		break
