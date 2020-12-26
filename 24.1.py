
import sys
from collections import namedtuple

class Point(namedtuple('_Point', ['ne', 'se'])):
	def __add__(self, other):
		return Point(self.ne + other.ne, self.se + other.se)

dirs = {
	'ne': Point(1, 0),
	'se': Point(0, 1),
	'sw': Point(-1, 0),
	'nw': Point(0, -1),
	'e': Point(1, 1),
	'w': Point(-1, -1),
}

flipped = set()
for line in sys.stdin:
	line = line.strip()
	buf = ''
	tile = Point(0, 0)
	for c in line:
		buf += c
		if buf not in dirs:
			continue
		tile += dirs[buf]
		buf = ''
	flipped ^= {tile}

print len(flipped)
