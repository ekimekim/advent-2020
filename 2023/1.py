import sys
import re
import itertools as it

lines = sys.stdin.read().strip().split("\n")
parts = [line.split() for line in lines]

ds = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

t1 = 0
t2 = 0
for line in lines:
	p1_parts = []
	parts = []
	for i in range(len(line)):
		part = line[i:]
		if part[0].isdigit():
			parts.append(int(part[0]))
			p1_parts.append(int(part[0]))
		for n, d in enumerate(ds):
			if part.startswith(d):
				parts.append(n + 1)
	t1 += 10 * p1_parts[0] + p1_parts[-1]
	t2 += 10 * parts[0] + parts[-1]
print t1, t2
