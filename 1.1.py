import itertools
import sys

for a, b in itertools.combinations(map(int, sys.stdin), 2):
	if a + b == 2020:
		print a * b
