import sys
from collections import Counter

reports = [[int(x) for x in line.split()] for line in sys.stdin.read().strip().split("\n")]

def is_safe(report, dampener=False):
	diffs = set(a - b for a, b in zip(report, report[1:]))
	return diffs.issubset({1, 2, 3}) or diffs.issubset({-1, -2, -3})

def is_safe_dampener(report):
	for i in range(len(report)):
		if is_safe(report[:i] + report[i+1:]):
			return True

print("part 1:", len([r for r in reports if is_safe(r)]))
print("part 2:", len([r for r in reports if is_safe_dampener(r)]))
