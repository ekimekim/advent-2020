
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

overlap = Counter()
for (sx, sy), (ex, ey) in lines:
	rx = range(min([sx, ex]), max([sx, ex])+1)
	ry = range(min([sy, ey]), max([sy, ey])+1)
	if 1 in (len(rx), len(ry)):
		points = list(product(rx, ry))
	else:
		assert len(rx) == len(ry)
		# flip one axis if needed
		if (sx < ex) ^ (sy < ey):
			ry = ry[::-1]
		points = zip(rx, ry)
	print sx, sy, ex, ey, points
	for x, y in points:
		overlap.update([(x, y)])

result = 0
for point, count in overlap.items():
	if count >= 2:
		result += 1

print result
