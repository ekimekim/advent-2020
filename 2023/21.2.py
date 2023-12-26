
import sys

grid = sys.stdin.read().strip().split("\n")

for y, line in enumerate(grid):
	for x, c in enumerate(line):
		if c == "S":
			sx = x
			sy = y

width = len(grid[0])
height = len(grid)

def sum(a, b):
	return tuple(ax + bx for ax, bx in zip(a, b))

def mul(a, k):
	return tuple(ax * k for ax in a)

def rev(a):
	return a[::-1]

def even(x):
	return x % 2 == 0

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

STEPS = 26501365

center = get_counts(sx, sy)

right_start = width - sx
right_counts = get_counts(0, sy)
if not even(right_start):
	right_counts = rev(right_counts)
# count number of complete cycles (2 widths)
full_rights, remaining = divmod((STEPS - right_start), 2 * width)
# total counts are number of complete cycles * (counts from one width + opposite counts from one width)
full_counts = mul(full_rights, add(right_counts, rev(right_counts)))
# add in first half of last complete cycle, which may be partial
full_counts = add(full_counts, get_counts(0, sy, remaining))
# and reversed second half of last complete cycle, if non-zero
if remaining - width >= 0:
	full_counts = add(full_counts, get_counts(0, sy, remaining - width))
