import sys
from collections import Counter

ages = Counter(map(int, sys.stdin.read().split(",")))

for day in range(256):
	new = ages.get(0, 0)
	ages = {k-1: v for k, v in ages.items() if k > 0}
	ages[6] = ages.get(6, 0) + new
	ages[8] = new

print sum(ages.values())
