

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

Region = namedtuple("Region", ["left", "right", "top", "bottom"])

lines = sys.stdin.read().strip().split("\n")
outline = []
x = 0
y = 0
outline_area = 0
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
	outline.append(Region(*(sort(x, end_x) + sort(y, end_y))))
	outline_area += length
	x = end_x
	y = end_y

assert x == 0 and y == 0
outline.sort()

print "OUTLINE"
print "\n".join(map(str, outline))

def maxima(regions):
	min_x = min(region.left for region in regions)
	max_x = max(region.right for region in regions)
	min_y = min(region.top for region in regions)
	max_y = max(region.bottom for region in regions)
	return min_x, max_x, min_y, max_y

min_x, max_x, min_y, max_y = maxima(outline)
x = min_x
area = 0
DEBUG_X = -163
def d(*args):
	if x == DEBUG_X:
		print args
while x <= max_x:
	in_line = [
		region for region in outline
		if region.left <= x <= region.right
	]
	in_line.sort(key = lambda r: (r.top, r.bottom))
	inside = False
	y = min_y - 1
	total = 0
	next_x = min([max_x + 1] + [
		region.left for region in outline
		if region.left > x
	] + [
		region.right + 1 for region in outline
		if region.right >= x
	])
	for region in in_line:
		if region.left == region.right:
			y = region.bottom
			continue
		length = region.top - y
		d(y, "to", region, "(length", length, "), inside = ", inside)
		y = region.bottom + 1
		if inside:
			total += length
		inside = not inside
	width = next_x - x
	print "x = {} to {}: {} length * {} width = {}".format(x, next_x, total, width, total * width)
	area += total * width
	x = next_x
print "inside", area
print "outline", outline_area
print area + outline_area
