
import sys
from itertools import count

map = sys.stdin.read().strip().split('\n')

def is_tree(x, y):
	line = map[y]
	char = line[x % len(line)]
	return char == '#'

mult = 1

for dx, dy in [
	(1, 1),
	(3, 1),
	(5, 1),
	(7, 1),
	(1, 2),
]:
	trees = len(filter(None, [
		is_tree(x, y)
		for x, y in zip(count(0, dx), range(0, len(map), dy))
	]))
	mult *= trees

print mult
