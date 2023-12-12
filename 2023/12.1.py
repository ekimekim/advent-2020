import sys
import re

def solve(values, runs):
	if "?" in values:
		i = values.index("?")
		return sum(solve(values[:i] + value + values[i+1:], runs) for value in ".#")
	found = [len(match) for match in re.findall("#+", values)]
	if found != runs:
		return 0
	return 1

total = 0
for line in sys.stdin.read().strip().split("\n"):
	values, runs = line.split()
	runs = map(int, runs.split(","))
	count = solve(values, runs)
	total += count
	print line, count

print total
