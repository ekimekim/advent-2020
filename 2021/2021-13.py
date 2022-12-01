import sys

dots, folds = sys.stdin.read().strip().split("\n\n")
dots = [map(int, line.split(",")) for line in dots.split("\n")]
folds = [(line[11], int(line[13:])) for line in folds.split("\n")]

width = max([x for x, y in dots]) + 1
height = max([y for x, y in dots]) + 1

paper = [
	[False for _ in range(width)]
	for _ in range(height)
]
for x, y in dots:
	paper[y][x] = True

first = True
for axis, num in folds:
	if axis == 'y':
		for y in range(num + 1, height):
			for x in range(width):
				paper[2 * num - y][x] |= paper[y][x]
		height = num
	else:
		for x in range(num + 1, width):
			for y in range(height):
				paper[y][2 * num - x] |= paper[y][x]
		width = num
	if first:
		print sum([
			paper[y][x]
			for x in range(width)
			for y in range(height)
		])
		first = False

for y in range(height):
	print ''.join('#' if paper[y][x] else ' ' for x in range(width))
