
from collections import namedtuple
import bisect
import sys

Region = namedtuple("Region", ["left", "right", "top", "bottom"])
inf = float("inf")

def point(x, y):
	return Region(x, x, y, y)

def is_finite(region):
	return all(coord not in (inf, -inf) for coord in region)

def intersects(regions, target):
	"""Returns whether target region intersects with any region in regions."""
	for region in regions:
		if (
			(region.left <= target.left and region.right >= target.left)
			or (region.left > target.left and region.left <= target.right)
		) and (
			(region.top <= target.top and region.bottom >= target.top)
			or (region.top > target.top and region.top <= target.bottom)
		):
			return True
	return False

def expand_within_bounds(regions, target):
	"""Returns a new region that is a superset of target, but doesn't intersect regions.
	target must not already intersect regions.
	The new region MAY be infinite.
	"""
	# Expand as far left/right as we can, then as far up/down.
	left, right, top, bottom = target
	left = max([-inf] + [
		region.right for region in regions
		if region.right < left
		and (
			(region.top <= top and region.bottom >= top)
			or (region.top > top and region.top <= bottom)
		)
	]) + 1
	right = min([inf] + [
		region.left for region in regions
		if region.left < right
		and (
			(region.top <= top and region.bottom >= top)
			or (region.top > top and region.top <= bottom)
		)
	]) - 1
	top = max([-inf] + [
		region.bottom for region in regions
		if region.bottom < top
		and (
			(region.left <= left and region.right >= left)
			or (region.left > left and region.left <= right)
		)
	]) + 1
	bottom = min([inf] + [
		region.top for region in regions
		if region.top < bottom
		and (
			(region.left <= left and region.right >= left)
			or (region.left > left and region.left <= right)
		)
	]) - 1
	return Region(left, right, top, bottom)

lines = sys.stdin.read().strip().split("\n")
outline = []
x = 0
y = 0
for line in lines:
	_, _, color = line.split()
	length = int(color[2:7], 16)
	dir = "RDLU"[int(color[7])]
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
	x = end_x
	y = end_y

assert x == 0 and y == 0
outline.sort()

print outline

def find_inside(outline):
	min_x, max_x, min_y, max_y = maxima(outline)
	inside = []
	outside = []
	for x in range(min_x, max_x + 1):
		for y in range(min_y, max_y + 1):
			current = []
			queue = [point(x, y)]
			is_outside = False
			while queue:
				region = queue.pop()
				region = expand_within_bounds(outline, region)
				if not is_finite(region):
					is_outside = True
					outside.append(region)
					continue
				if intersects(outside, region):
					is_outside = True
					continue
				if intersects
					#TODO UPTO
					#this is a mess
				if (x, y) in inside or (x, y) in current or (x, y) in outline:
					continue
				current.add((x, y))
				for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
					queue.append((x + dx, y + dy))
			if is_outside:
				outside |= current
			else:
				inside |= current
	return inside
