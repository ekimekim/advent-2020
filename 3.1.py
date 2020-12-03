
import sys
from itertools import count

map = sys.stdin.read().strip().split('\n')

def is_tree(x, y):
	line = map[y]
	char = line[x % len(line)]
	return char == '#'

trees = len(filter(None, [
	is_tree(x, y)
	for x, y in zip(count(0, 3), range(len(map)))
]))

print trees
