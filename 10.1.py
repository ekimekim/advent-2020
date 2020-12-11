import sys
from collections import Counter

joltages = map(int, sys.stdin)
joltages = [0] + sorted(joltages) + [max(joltages) + 3]

c = Counter(b - a for a, b in zip(joltages, joltages[1:]))

print c[1] * c[3]
