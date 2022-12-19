
import itertools
import sys

SHAPES = [
	[(0, 0), (1, 0), (2, 0), (3, 0)],
	[(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
	[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
	[(0, 0), (0, 1), (0, 2), (0, 3)],
	[(0, 0), (0, 1), (1, 0), (1, 1)],
]

jets = itertools.cycle(sys.stdin.read().strip())

filled = set()
def height():
	return max(y for x, y in filled) if filled else 0

def check_collision(rock, rx, ry):
	for dx, dy in rock:
		x = rx + dx
		y = ry + dy
		if not (0 <= x < 7):
			return True
		if (x, y) in filled:
			return True
		if y <= 0:
			return True
	return False

def draw(rock, rx, ry):
	rockparts = [(rx + dx, ry + dy) for dx, dy in rock]
	print "\n".join(
		"".join(
			"@" if (x, y) in rockparts else
			"#" if (x, y) in filled else
			" "
			for x in range(7)
		) for y in range(height() + 5, 0, -1)
	)
	print "======="

for i in range(2022):
	rock = SHAPES[i % len(SHAPES)]
	rx = 2
	ry = height() + 4
	for jet in jets:
		#draw(rock, rx, ry)
		dx = -1 if jet == '<' else 1
		if not check_collision(rock, rx + dx, ry):
			rx += dx
		#draw(rock, rx, ry)
		if check_collision(rock, rx, ry - 1):
			break
		else:
			ry -= 1
	#draw(rock, rx, ry)
	for dx, dy in rock:
		filled.add((rx + dx, ry + dy))

print height()
