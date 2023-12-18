
import sys

lines = sys.stdin.read().strip().split("\n")
outline = set() # ((start_x, end_x), (start_y, end_y)), ranges inclusive
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
	outline.add((sort(x, end_x), sort(y, end_y)))
	x = end_x
	y = end_y

assert x == 0 and y == 0

def expand(nodes):
	return set(
		(x, y)
		for (xa, xb), (ya, yb) in nodes
		for x in range(xa, xb + 1)
		for y in range(ya, yb + 1)
	)

def scale(nodes, factor):
	return set(((xa // factor, xb // factor), (ya // factor, yb // factor)) for (xa, xb), (ya, yb) in nodes)

def draw(expanded):
	min_x = min(x for x, y in expanded)
	max_x = max(x for x, y in expanded)
	min_y = min(y for x, y in expanded)
	max_y = max(y for x, y in expanded)
	for y in range(min_y, max_y + 1):
		print "".join(
			"#" if (x, y) in expanded else "."
			for x in range(min_x, max_x + 1)
		)

def find_inside(outline):
	min_x = min(x for x, y in outline)
	max_x = max(x for x, y in outline)
	min_y = min(y for x, y in outline)
	max_y = max(y for x, y in outline)
	inside = set()
	outside = set()
	for x in range(min_x, max_x + 1):
		for y in range(min_y, max_y + 1):
			current = set()
			queue = [(x, y)]
			is_outside = False
			while queue:
				x, y = queue.pop()
				if (x, y) in outside:
					is_outside = True
					continue
				if x < min_x or x > max_x or y < min_y or y > max_y:
					is_outside = True
					continue
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

print outline
print scale(outline, 100000)
print expand(scale(outline, 100000))
draw(expand(scale(outline, 100000)))
