import sys
import itertools

window = []
for line in sys.stdin:
	value = int(line)
	if len(window) == 25 and not any(
		v1 + v2 == value
		for v1, v2 in itertools.combinations(window, 2)
		if v1 != v2
	):
		print value
		break
	window = window[-24:] + [value]
