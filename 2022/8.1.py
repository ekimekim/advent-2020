import sys

grid = [
	map(int, line)
	for line in sys.stdin.read().strip().split("\n")
]

width = len(grid[0])
height = len(grid)

visible = set()

def print_visible():
	print "\n".join(
		"".join(
			"\x1b[{}m{}\x1b[m".format("31" if (x, y) in visible else "", grid[y][x])
			for x in range(width)
		) for y in range(height)
	)

def walk(x, y, dx, dy):
	tallest = -1
	while 0 <= x < width and 0 <= y < height:
		here = grid[y][x]
		if tallest < here:
			visible.add((x, y))
			tallest = here
		x += dx
		y += dy

for y in range(height):
	# walk left along row
	walk(0, y, 1, 0)
	# walk right along row
	walk(width - 1, y, -1, 0)
for x in range(width):
	# walk down along column
	walk(x, 0, 0, 1)
	# walk up along column
	walk(x, height - 1, 0, -1)

print len(visible)
