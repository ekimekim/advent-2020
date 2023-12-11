import sys
import itertools

lines = sys.stdin.read().strip().split("\n")

expand_y = [y for y, line in enumerate(lines) if set(line) == {"."}]
expand_x = [x for x in range(len(lines[0])) if all(line[x] == "." for line in lines)]

galaxies = set()
for by, line in enumerate(lines):
	for bx, c in enumerate(line):
		dx = sum([999999 for x in expand_x if x < bx])
		dy = sum([999999 for y in expand_y if y < by])
		if c == "#":
			galaxies.add((bx + dx, by + dy))

print sum(
	abs(ax - bx) + abs(ay - by)
	for (ax, ay), (bx, by) in itertools.combinations(galaxies, 2)
)
