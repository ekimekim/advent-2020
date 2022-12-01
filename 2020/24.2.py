
import sys
from collections import namedtuple, defaultdict

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

active = set()
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
	active ^= {tile}

for _ in range(100):
	counts = defaultdict(lambda: 0)
	for tile in active:
		for dir in dirs.values():
			counts[tile + dir] += 1
	for tile in set(counts) | active:
		if tile in active and counts[tile] not in (1,2):
			active.remove(tile)
		elif tile not in active and counts[tile] == 2:
			active.add(tile)

print len(active)
