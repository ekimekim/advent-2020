import sys

starting = map(int, sys.stdin.read().split(','))
seen = {v: i for i, v in enumerate(starting[:-1])}

prev = starting[-1]
for turn in xrange(len(starting) - 1, 30000000 - 1):
	if prev in seen:
		ago = turn - seen[prev]
	else:
		ago = 0
	seen[prev] = turn
	prev = ago

print prev
