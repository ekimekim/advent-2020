import sys

def parse(line):
	return sum((c in 'BR') * (512 >> i) for i, c in enumerate(line))

seats = map(parse, sys.stdin.read().strip().split())
all_seats = range(min(seats), max(seats))
mine = set(all_seats) - set(seats)
assert len(mine) == 1
print list(mine)[0]
