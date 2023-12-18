

"""
idea:
for each y
	inside = false
	for each x where whether we're in outline or not changes (along the line y)
		inside = not inside
		if inside, points += this x - prev x
		keep track of min y for which these points are the same
	ie. for every second interval between outline points, it's inside.
	area += points * y distance for which points are all the same
	y = next spot where points aren't all the same
"""

PART2 = False

from collections import namedtuple
import bisect
import sys

lines = sys.stdin.read().strip().split("\n")
verts = []
horis = []
x = 0
y = 0
for line in lines:
	dir, length, color = line.split()
	if PART2:
		length = int(color[2:7], 16)
		dir = "RDLU"[int(color[7])]
	else:
		length = int(length)
	dx, dy = {
		"U": (0, -1),
		"D": (0, 1),
		"L": (-1, 0),
		"R": (1, 0),
	}[dir]
	end_x = x + length * dx
	end_y = y + length * dy
	sort = lambda *t: tuple(sorted(t))
	if dir in "UD":
		verts.append((x, sort(y, end_y)))
	else:
		horis.append((y, sort(x, end_x)))
	x = end_x
	y = end_y

assert x == 0 and y == 0
verts.sort()
horis.sort()

print "vert"
print "\n".join(map(str, verts))
print "hori"
print "\n".join(map(str, horis))

def maxima(regions):
	min_x = min(region.left for region in regions)
	max_x = max(region.right for region in regions)
	min_y = min(region.top for region in regions)
	max_y = max(region.bottom for region in regions)
	return min_x, max_x, min_y, max_y

min_x, max_x, min_y, max_y = maxima(outline)
x = min_x
area = 0
while x <= max_x:
	crossings = [
		(y, ex) for y, (sx, ex) in horis
		if sx <= x <= ex
	]
	inside = False
	y = min_y
	length = 0
	next_x = max_x + 1
	for crossing, right in in_line:
		if inside:
			length += region.top - y
		y = region.bottom + 1
		inside = not inside
		next_x = min(next_x, region.right + 1)
	assert not inside
	width = next_x - x
	area += length * width
	x = next_x
