import sys
import itertools

lines = sys.stdin.read().strip().split("\n")

expanded = []
for line in lines:
	if set(line) == {"."}:
		expanded += [line, line]
	else:
		expanded.append(line)

for y in range(len(lines[0]))[::-1]:
	if all(line[y] == "." for line in lines):
		expanded = [
			line[:y] + "." + line[y:]
			for line in expanded
		]

galaxies = set()
for y, line in enumerate(expanded):
	for x, c in enumerate(line):
		if c == "#":
			galaxies.add((x, y))

print sum(
	abs(ax - bx) + abs(ay - by)
	for (ax, ay), (bx, by) in itertools.combinations(galaxies, 2)
)
