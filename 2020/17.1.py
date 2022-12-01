import sys
import itertools

active = set()
for x, line in enumerate(sys.stdin):
	line = line.strip()
	for y, char in enumerate(line):
		if char == '#':
			active.add((x, y, 0))

def add(p1, p2):
	return tuple(v1 + v2 for v1, v2 in zip(p1, p2))

DELTAS = [
	p for p in itertools.product(*[(-1, 0, 1) for _ in range(3)])
	if any(v != 0 for v in p)
]

def step(active):
	new_active = active.copy()
	mins = [
		min(p[d] for p in active) - 1
		for d in range(3)
	]
	maxes = [
		max(p[d] for p in active) + 1
		for d in range(3)
	]
	ranges = [range(low, high + 1) for low, high in zip(mins, maxes)]
	points = itertools.product(*ranges)
	for point in points:
		neighbors = sum(
			1 for d in DELTAS
			if add(point, d) in active
		)
		if point in active and neighbors not in (2, 3):
			new_active.remove(point)
		elif point not in active and neighbors == 3:
			new_active.add(point)
	return new_active

def debug(active):
	mins = [
		min(p[d] for p in active)
		for d in range(3)
	]
	maxes = [
		max(p[d] for p in active)
		for d in range(3)
	]
	ranges = [range(low, high + 1) for low, high in zip(mins, maxes)]
	for z in ranges[2]:
		for y in ranges[1]:
			print "".join("#" if (x, y, z) in active else "." for x in ranges[0])
		print


for _ in range(6):
	active = step(active)
#	debug(active)
#	print "===="

print len(active)
