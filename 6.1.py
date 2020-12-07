import sys

print sum(
	len(set().union(*group.split('\n')))
	for group in sys.stdin.read().strip().split('\n\n')
)
