import sys

lines = sys.stdin.read().strip().split("\n")
left, right = zip(*[map(int, line.split()) for line in lines])

print("Part 1:", sum(abs(a - b) for a, b in zip(sorted(left), sorted(right))))

from collections import Counter
counts = Counter(right)
print("Part 2:", sum(n * counts[n] for n in left))
