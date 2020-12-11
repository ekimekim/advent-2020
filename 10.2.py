import sys
from collections import Counter

joltages = map(int, sys.stdin)
joltages = [0] + sorted(joltages) + [max(joltages) + 3]

known = {}
def memo(index):
	if index not in known:
		known[index] = combinations(index)
	return known[index]

def combinations(index):
	if index == len(joltages) - 1:
		# we've reached a valid end point
		return 1
	current = joltages[index]
	found = 0
	for i, next in enumerate(joltages[index+1:]):
		if next - current > 3:
			break
		found += memo(index + i + 1)
	return found

print combinations(0)
