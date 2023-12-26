
import sys

grid = sys.stdin.read().strip().split("\n")

for y, line in enumerate(grid):
	for x, c in enumerate(line):
		if c == "S":
			sx = x
			sy = y

width = len(grid[0])
height = len(grid)

def add(*values):
	return tuple(sum(parts) for parts in zip(*values))

def mul(k, a):
	return tuple(ax * k for ax in a)

def rev(a):
	return a[::-1]

def even(x):
	return x % 2 == 0

# width and height are odd, start is in center
# width and height are equal.
assert not even(width)
assert not even(height)
assert 2 * sx + 1 == width
assert 2 * sy + 1 == height
assert width == height
SIZE = width
HALF_SIZE = (width + 1) / 2
assert even(HALF_SIZE)

# We observe that the grid always has open sides - there are no rocks in the top/bottom rows
# or left/right columns.
# It also has an open row/column in line with start.
# Also, the grid is an odd size in both axes, and is square. The size is 131.
#
# This means that starting from the bottom-left corner of one copy of the grid,
# you know that you can each the bottom-left corner of the copies up or right of yours
# in exactly 131 steps, and that this is the fastest path there.
# So once you know how many steps it is to reach the first bottom-left corner,
# and how many points in the grid are even/odd from there, then you know how many grids
# you can go before hitting step limits.
# This can be similarly repeated for each of the 4 diagonals.
#
# For grids in-line with the start, we can act similarly except our starting point is in line with
# start and on the near edge (eg. center-left when going right).

def get_counts(sx, sy, limit=None):
	if limit < 0:
		return (0, 0)
	queue = [(0, sx, sy)]
	seen = set()
	even = 0
	odd = 0
	while queue:
		steps, x, y = queue.pop(0)
		if (x, y) in seen:
			continue
		seen.add((x, y))
		if steps % 2 == 0:
			even += 1
		else:
			odd += 1
		if limit is not None and steps >= limit:
			continue
		for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
			nx = x + dx
			ny = y + dy
			if nx < 0 or ny < 0 or nx >= width or ny >= height or grid[ny][nx] == "#":
				continue
			queue.append((steps + 1, nx, ny))
	return even, odd

STEPS = int(sys.argv[1]) if len(sys.argv) > 1 else 26501365

def cardinal_counts(sx, sy):
	counts = get_counts(sx, sy)
	# count number of complete cycles (2 widths)
	full, remaining = divmod(STEPS - HALF_SIZE, 2 * SIZE)
	# step backwards once so we know full always covers complete cycles.
	full -= 1
	remaining += 2 * SIZE
	# total counts are number of complete cycles * (counts from one width + opposite counts from one width)
	full_counts = mul(full, add(counts, rev(counts)))
	odd = False
	while remaining >= 0:
		counts = get_counts(sx, sy, remaining)
		if odd:
			counts = rev(counts)
		full_counts = add(full_counts, counts)
		odd = not odd
		remaining -= SIZE
	return full_counts

def diagonal_counts(sx, sy):
	counts = get_counts(sx, sy)
	# count number of complete cycles (2 widths) in one direction
	full, remaining = divmod(STEPS - 2 * HALF_SIZE, 2 * SIZE)
	# step backwards so we know full always covers complete cycles
	full -= 1
	remaining += 2 * SIZE
	# We can go FULL steps in one direction, or (FULL - 1) steps then 1 in the other,
	# or (FULL - 2) and 2 in the other, etc. The total area is a triangular number.
	full_area = full * (full + 1) / 2
	# Note one full area contains 2 lots of counts and reversed counts.
	full_counts = mul(2 * full_area, add(counts, rev(counts)))

	# The remainder is a 2 * 2 area that is repeated FULL + 1 times (one more than the
	# last diagonal full line), then another 2x2 area that is repeated FULL + 2 times
	# (one more than that line).
	# m
	# mm
	# MMm
	# MMmm
	# FFMMm
	# FFMMmm
	major_remainder = add(
		get_counts(sx, sy, remaining),
		mul(2, rev(get_counts(sx, sy, remaining - SIZE))),
		get_counts(sx, sy, remaining - 2 * SIZE)
	)
	minor_remainder = add(
		get_counts(sx, sy, remaining - 2 * SIZE),
		mul(2, rev(get_counts(sx, sy, remaining - 3 * SIZE))),
		# since remaining < 4 * SIZE, the final corner is impossible
	)

	return add(
		full_counts,
		mul(full + 1, major_remainder),
		mul(full + 2, minor_remainder),
	)

center = get_counts(sx, sy)
left = cardinal_counts(width - 1, sy)
right = cardinal_counts(0, sy)
up = cardinal_counts(sx, height - 1)
down = cardinal_counts(sx, 0)
up_left = diagonal_counts(width - 1, height - 1)
up_right = diagonal_counts(0, height - 1)
down_left = diagonal_counts(width - 1, 0)
down_right = diagonal_counts(0, 0)

all_counts = add(
	center,
	left,
	right,
	up,
	down,
	up_left,
	up_right,
	down_left,
	down_right,
)

if not even(STEPS):
	all_counts = rev(all_counts)

print all_counts[0]
