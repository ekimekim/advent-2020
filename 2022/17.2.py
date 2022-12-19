
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

TARGET = 1000000000000
first_state = None
i = 0
skipped_y = None
while i < TARGET:
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

	y = height()
	if all((x, y) in filled for x in range(7)):
		if first_state is None:
			first_state = i, y
		else:
			prev_i, prev_y = first_state
			di = i - prev_i
			dy = y - prev_y
			# we now know we can advance by di steps, and it adds dy to the pile and leaves
			# us back in an identical state.
			remaining = TARGET - i
			skips = int(remaining / di)
			i = i + di * skips # last such state before TARGET
			assert skipped_y is None, "deja vu?"
			skipped_y = skips * dy
	i += 1

print height() + skipped_y
