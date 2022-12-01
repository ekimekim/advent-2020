import itertools
import sys

for a, b, c in itertools.combinations(map(int, sys.stdin), 3):
	if a + b + c == 2020:
		print a * b * c
