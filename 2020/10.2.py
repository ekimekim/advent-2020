import sys
from itertools import count

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
	for next_index in range(index+1, len(joltages)):
		if joltages[next_index] - current > 3:
			break
		found += memo(next_index)
	return found

print combinations(0)
