
import sys
from collections import Counter
from itertools import product

# [(start, end)]
lines = [
	[
		map(int, coord.split(","))
		for coord in line.split(" -> ")
	] for line in sys.stdin.read().strip().split('\n')
]

ortho = [
	line for line in lines
	if line[0][0] == line[1][0] or line[0][1] == line[1][1]
]

overlap = Counter()
for (sx, sy), (ex, ey) in ortho:
	print sx, sy, ex, ey
	rx = range(min([sx, ex]), max([sx, ex])+1)
	ry = range(min([sy, ey]), max([sy, ey])+1)
	print len(rx), len(ry)
	for x, y in product(rx, ry):
		overlap.update([(x, y)])

result = 0
for point, count in overlap.items():
	if count >= 2:
		print point
		result += 1

print result
