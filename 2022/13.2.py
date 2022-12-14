
import sys
import json
import itertools

def compare(a, b):
	a_list = isinstance(a, list)
	b_list = isinstance(b, list)
	if not (a_list or b_list):
		return cmp(a, b)
	if a_list and b_list:
		for ax, bx in itertools.izip_longest(a, b):
			if ax is None:
				# b was longer, a < b
				return -1
			if bx is None:
				# a was longer, a > b
				return 1
			subcmp = compare(ax, bx)
			if subcmp != 0:
				return subcmp
		# both were identical
		return 0
	if not a_list:
		return compare([a], b)
	if not b_list:
		return compare(a, [b])

packets = [
	json.loads(line)
	for line in sys.stdin.read().strip().split("\n")
	if line
] + [
	[[2]],
	[[6]],
]
packets.sort(cmp=compare)
print (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)
