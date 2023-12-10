
import sys
import itertools

verbose = True
color = True
FULL_BLOCK = "\xe2\x96\x88"

DIRS = [
	(0, -1),
	(1, 0),
	(0, 1),
	(-1, 0),
]

UP, RIGHT, DOWN, LEFT = DIRS

SUBDIV = {
	"|": {(1, 0), (1, 1), (1, 2)},
	"-": {(0, 1), (1, 1), (2, 1)},
	"L": {(1, 0), (1, 1), (2, 1)},
	"J": {(1, 0), (1, 1), (0, 1)},
	"7": {(0, 1), (1, 1), (1, 2)},
	"F": {(2, 1), (1, 1), (1, 2)},
	".": set(),
	"S": {(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)},
}

lines = sys.stdin.read().strip().split("\n")

def add(t1, t2):
	return tuple(a + b for a, b in zip(t1, t2))

pipes = set()

for y, line in enumerate(lines):
	for x, c in enumerate(line):
		if c == "S":
			sy = 3 * y + 1
			sx = 3 * x + 1
		for delta in SUBDIV[c]:
			pipes.add(add((3 * x, 3 * y), delta))

if verbose:
	for y in range(len(lines) * 3):
		print "".join(
			FULL_BLOCK if (x, y) in pipes else " "
			for x in range(len(lines[0]) * 3)
		)

start_points = set(
	add((sx, sy), delta)
	for delta in SUBDIV["S"]
)

# BFS
queue = [(0, (sx, sy))]
loop = set()
found_loop = False
while queue:
	step, pos = queue.pop()
	for delta in DIRS:
		new_pos = add(pos, delta)
		if new_pos in pipes and new_pos not in loop:
			queue.append((step + 1, new_pos))
			loop.add(new_pos)
		if new_pos in start_points and step > 2 and not found_loop:
			length = step + 1 # include the one step we've taken in the other direction
			length /= 3 # un-expand
			half_length = (length + 1) / 2
			print "part 1:", half_length
			found_loop = True

# flood fill into 2 sets: outside and inside
outside = set()
inside = set()
width = len(lines[0]) * 3
height = len(lines) * 3
for y in range(height):
	for x in range(width):
		# check for already known
		pos = x, y
		if pos in inside or pos in outside or pos in loop:
			continue
		# do a BFS until we know if pos is inside or outside
		current = set()
		queue = [pos]
		is_outside = False
		while queue:
			pos = queue.pop()
			for delta in DIRS:
				new_pos = add(pos, delta)
				if new_pos in loop:
					continue # don't cross the loop
				if new_pos in current:
					continue
				nx, ny = new_pos
				if nx < 0 or ny < 0 or nx >= width or ny >= height:
					is_outside = True
					continue
				current.add(new_pos)
				queue.append(new_pos)
		# if current ever touched outside, it's outside. otherwise it's inside.
		if is_outside:
			outside |= current
		else:
			inside |= current

if color:
	LOOP = "\x1b[31m" + FULL_BLOCK + "\x1b[m"
	INSIDE = "\x1b[33m" + FULL_BLOCK + "\x1b[m"
else:
	LOOP = "O"
	INSIDE = "*"
OUTSIDE = " "

if verbose:
	for y in range(height):
		print "".join(
			LOOP if (x, y) in loop else
			OUTSIDE if (x, y) in outside else
			INSIDE if (x, y) in inside else "?"
			for x in range(width)
		)

# un-expand inside by considering blocks of 3x3
block = list(itertools.product(range(3), repeat=2))
fully_inside = [
	(bx / 3, by / 3)
	for bx in range(0, width, 3)
	for by in range(0, height, 3)
	if all(add((bx, by), delta) in inside for delta in block)
]
print "part 2:", len(fully_inside)

if verbose:
	for y in range(height / 3):
		print "".join(
			LOOP if any(add((3*x, 3*y), delta) in loop for delta in block) else
			INSIDE if (x, y) in fully_inside else
			OUTSIDE
			for x in range(width / 3)
		)
