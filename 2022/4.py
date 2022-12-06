import sys

input = []
for line in sys.stdin.read().strip().split("\n"):
	parts = []
	for part in line.split(","):
		start, end = map(int, part.split("-"))
		parts.append(set(range(start, end + 1)))
	input.append(parts)

print len([
	1 for a, b in input
	if a.issubset(b) or b.issubset(a)
])
print len([
	1 for a, b in input
	if a & b
])
