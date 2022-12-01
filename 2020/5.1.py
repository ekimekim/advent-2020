import sys

def parse(line):
	return sum((c in 'BR') * (512 >> i) for i, c in enumerate(line))

print max(map(parse, sys.stdin.read().strip().split('\n')))
